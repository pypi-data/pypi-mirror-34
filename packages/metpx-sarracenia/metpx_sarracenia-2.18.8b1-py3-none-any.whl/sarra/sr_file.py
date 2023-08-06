#!/usr/bin/env python3
#
# This file is part of sarracenia.
# The sarracenia suite is Free and is proudly provided by the Government of Canada
# Copyright (C) Her Majesty The Queen in Right of Canada, Environment Canada, 2008-2015
#
# Questions or bugs report: dps-client@ec.gc.ca
# sarracenia repository: git://git.code.sf.net/p/metpx/git
# Documentation: http://metpx.sourceforge.net/#SarraDocumentation
#
# sr_file.py : python3 utility tools for file processing
#
#
# Code contributed by:
#  Michel Grenier - Shared Services Canada
#  Last Changed   : Sep 22 10:41:32 EDT 2015
#  Last Revision  : Feb  5 09:48:34 EST 2016
#
########################################################################
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful, 
#  but WITHOUT ANY WARRANTY; without even the implied warranty of 
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307  USA
#
#

import os, stat, sys, time

try:
    from sr_util import *
except:
    from sarra.sr_util import *

#============================================================
# file protocol in sarracenia supports/uses :
#
# connect
# close
#
# if a source    : get    (remote,local)
#                  ls     ()
#                  cd     (dir)
#                  delete (path)
#
# require   parent.logger
#           parent.credentials
#           parent.destination 
#           parent.batch 
#           parent.chmod
#           parent.chmod_dir
#     opt   parent.kbytes_ps
#     opt   parent.bufsize

class sr_file():
    def __init__(self, parent) :
        parent.logger.debug("sr_file __init__")

        self.logger      = parent.logger
        self.parent      = parent 

    # cd
    def cd(self, path):
        self.logger.debug("sr_file cd %s" % path)
        os.chdir(path)
        self.path = path

    # chmod
    def chmod(self,perm,path):
        self.logger.debug("sr_file chmod %s %s" % ( "{0:o}".format(perm),path))
        os.chmod(path,perm)

    # close
    def close(self):
        self.logger.debug("sr_file close")
        return

    # connect
    def connect(self):
        self.logger.debug("sr_file connect %s" % self.parent.destination)

        self.recursive   = True
        self.destination = self.parent.destination
        self.timeout     = self.parent.timeout

        self.kbytes_ps = 0
        self.bufsize   = 8192

        if hasattr(self.parent,'kbytes_ps') : self.kbytes_ps = self.parent.kbytes_ps
        if hasattr(self.parent,'bufsize')   : self.bufsize   = self.parent.bufsize

        self.connected   = True

        return True

    # delete
    def delete(self, path):
        self.logger.debug("sr_file rm %s" % path)
        os.unlink(path)

    # ls
    def ls(self):
        self.logger.debug("sr_file ls")
        self.entries  = {}
        self.root = self.path
        self.ls_python(self.path)
        return self.entries

    def ls_python(self,dpath):
        for x in os.listdir(dpath):
            dst = dpath + os.sep + x
            if os.path.isdir(dst):
               if self.recursive : self.ls_python(dst)
               continue
            relpath = dst.replace(self.root,'',1)
            if relpath[0] == '/' : relpath = relpath[1:]

            lstat = os.stat(dst)
            line  = stat.filemode(lstat.st_mode)
            line += ' %d %d %d' % (lstat.st_nlink,lstat.st_uid,lstat.st_gid)
            line += ' %d' % lstat.st_size
            line += ' %s' % time.strftime("%b %d %H:%M", time.localtime(lstat.st_mtime))
            line += ' %s' % relpath
            self.entries[relpath] = line



# file_insert
# called by file_process (general file:// processing)

def file_insert( parent,msg ) :
    parent.logger.debug("file_insert")

    fp = open(msg.relpath,'rb')
    if msg.partflg == 'i' : fp.seek(msg.offset,0)

    ok = file_write_length(fp, msg, parent.bufsize, msg.filesize, parent )

    fp.close()

    return ok


# file_insert_part
# called by file_reassemble : rebuiding file from parts
#
# when inserting, anything that goes wrong means that
# another process is working with this part_file
# so errors are ignored silently 

def file_insert_part(parent,msg,part_file):
    parent.logger.debug("file_insert_part %s" % part_file)
    chk = msg.sumalgo
    try :
             # file disappeared ...
             # probably inserted by another process in parallel
             if not os.path.isfile(part_file):
                parent.logger.debug("file doesnt exist %s" % part_file)
                return False

             # file with wrong size
             # probably being written now by another process in parallel

             lstat    = os.stat(part_file)
             fsiz     = lstat[stat.ST_SIZE] 
             if fsiz != msg.length : 
                parent.logger.debug("file wrong size %s %d %d" % (part_file,fsiz,msg.length))
                return False

             # proceed with insertion

             fp = open(part_file,'rb')
             ft = open(msg.target_file,'r+b')
             ft.seek(msg.offset,0)

             # no worry with length, read all of part_file
             # compute onfly_checksum ...

             bufsize = parent.bufsize
             if bufsize > msg.length : bufsize = msg.length

             if chk : chk.set_path(os.path.basename(msg.target_file))

             i  = 0
             while i<msg.length :
                   buf = fp.read(bufsize)
                   if not buf: break
                   ft.write(buf)
                   if chk : chk.update(buf)
                   i  += len(buf)

             if ft.tell() >= msg.filesize:
                 ft.truncate()

             ft.close() 
             fp.close()

             if i != msg.length :
                msg.logger.error("file_insert_part file currupted %s" % part_file)
                msg.logger.error("read up to  %d of %d " % (i,msg.length) )
                lstat   = os.stat(part_file)
                fsiz    = lstat[stat.ST_SIZE] 
                msg.logger.error("part filesize  %d " % (fsiz) )

             # set checksum in msg
             if chk : msg.onfly_checksum = chk.get_value()

             # remove inserted part file

             try    : os.unlink(part_file)
             except : pass

             # run on part... if provided

             if parent.on_part :
                ok = parent.on_part(parent)
                if not ok : 
                   msg.logger.warning("inserted but rejected by on_part %s " % part_file)
                   msg.logger.warning("the file may not be correctly reassemble %s " % msg.target_file)
                   return ok

    # oops something went wrong

    except :
             (stype, svalue, tb) = sys.exc_info()
             msg.logger.debug("sr_file/file_insert_part Type: %s, Value: %s,  ..." % (stype, svalue))
             msg.logger.debug("did not insert %s " % part_file)
             return False

    # success: log insertion

    msg.report_publish(201,'Inserted')

    # publish now, if needed, that it is inserted

    if msg.publisher : 
       msg.set_topic('v02.post',msg.target_relpath)
       msg.set_notice(msg.new_baseurl,msg.target_relpath,msg.time)
       if chk :
          if    msg.sumflg == 'z' :
                msg.set_sum(msg.checksum,msg.onfly_checksum)
          else: msg.set_sum(msg.sumflg,  msg.onfly_checksum)

       parent.__on_post__()
       msg.report_publish(201,'Publish')

    # if lastchunk, check if file needs to be truncated
    file_truncate(parent,msg)

    # ok we reassembled the file and it is the last chunk... call on_file
    if msg.lastchunk : 
       msg.logger.warning("file assumed complete with last part %s" % msg.target_file)
       #if parent.on_file:
       #   ok = parent.on_file(parent)
       for plugin in parent.on_file_list:
          ok = plugin(parent)
          if not ok: return False

    return True


# file_link
# called by file_process (general file:// processing)

def file_link( msg ) :

    try    : os.unlink(msg.new_file)
    except : pass
    try    : os.link(msg.relpath,msg.new_file)
    except : return False

    msg.compute_local_checksum()
    msg.onfly_checksum = msg.local_checksum

    msg.report_publish( 201, 'Linked')

    return True

# file_process (general file:// processing)

def file_process( parent ) :
    parent.logger.debug("file_process")

    msg = parent.msg

    # FIXME - MG - DOMINIC's LOCAL FILE MIRRORING BUG CASE
    # say file.txt does not exist
    # sequential commands in script
    # touch file.txt
    # mv file.txt newfile.txt
    # under libsrshim generate 3 amqp messages : 
    # 1- download/copy file.txt
    # 2- move message 1 :  remove file.txt with newname newfile.txt
    # 3- move message 2 :  download newfile.txt with oldname file.txt
    # message (1) will never be processed fast enough ... and will fail
    # message (2) removing of a file not there is considered successfull
    # message (3) is the one that will guaranty the the newfile.txt is there and mirroring is ok.
    #
    # message (1) fails.. in previous version a bug was preventing an error (and causing file.txt rebirth with size 0)
    # In current version, returning that this message fails would put it under the retry process for ever and for nothing.
    # I decided for the moment to warn and to return success... it preserves old behavior without the 0 byte file generated

    if not os.path.isfile(msg.relpath): 
       parent.logger.warning("%s moved or removed since announced" % msg.relpath)
       return True

    try:    curdir = os.getcwd()
    except: curdir = None

    if curdir != parent.msg.new_dir:
       os.chdir(parent.msg.new_dir)

    # try link if no inserts

    if msg.partflg == '1' or \
       (msg.partflg == 'p' and  msg.in_partfile) :
       ok = file_link(msg)
       if ok :
          if parent.delete :
              try: 
                  os.unlink(msg.relpath)
              except: 
                  msg.logger.error("delete of link to %s failed"%(msg.relpath))
          return ok

    # This part is for 2 reasons : insert part
    # or copy file if preceeding link did not work
    try :
             ok = file_insert(parent,msg)
             if parent.delete :
                if msg.partflg.startswith('i'):
                   msg.logger.info("delete unimplemented for in-place part files %s" %(msg.relpath))
                else:
                   try: 
                       os.unlink(msg.relpath)
                   except: 
                       msg.logger.error("delete of %s after copy failed"%(msg.relpath))

             if ok : return ok

    except : 
             (stype, svalue, tb) = sys.exc_info()
             msg.logger.debug("sr_file/file_process Type: %s, Value: %s,  ..." % (stype, svalue))

    msg.report_publish(499,'Not Copied')
    msg.logger.error("could not copy %s in %s"%(msg.relpath,msg.new_file))

    return False

# file_reassemble : rebuiding file from parts
# when ever a part file is processed (inserted or written in part_file)
# this module is called to try inserting any part_file left

def file_reassemble(parent):
    parent.logger.debug("file_reassemble")

    msg = parent.msg

    if not hasattr(msg,'target_file') or msg.target_file == None : return

    try:    curdir = os.getcwd()
    except: curdir = None

    if curdir != parent.msg.new_dir:
       os.chdir(parent.msg.new_dir)

    # target file does not exit yet

    if not os.path.isfile(msg.target_file) :
       msg.logger.debug("insert_from_parts: target_file not found %s" % msg.target_file)
       return

    # check target file size and pick starting part from that

    lstat   = os.stat(msg.target_file)
    fsiz    = lstat[stat.ST_SIZE] 
    i       = int(fsiz /msg.chunksize)

    msg.logger.debug("verify ingestion : block = %d of %d" % (i,msg.block_count))
       
    while i < msg.block_count:

          # setting block i in message

          msg.current_block = i
          msg.set_parts('i',msg.chunksize,msg.block_count,msg.remainder,msg.current_block)
          msg.set_suffix()

          # set part file

          part_file = msg.target_file + msg.suffix
          if not os.path.isfile(part_file) :
             msg.logger.debug("part file %s not found, stop insertion" % part_file)
             # break and not return because we want to check the lastchunk processing
             break

          # check for insertion (size may have changed)

          lstat   = os.stat(msg.target_file)
          fsiz    = lstat[stat.ST_SIZE] 
          if msg.offset > fsiz :
             msg.logger.debug("part file %s no ready for insertion (fsiz %d, offset %d)" % (part_file,fsiz,msg.offset))
             break


          # insertion attempt... should work unless there is some race condition

          ok = file_insert_part(parent,msg,part_file)
          # break and not return because we want to check the lastchunk processing
          if not ok : break
          i = i + 1

    # if lastchunk, check if file needs to be truncated
    file_truncate(parent,msg)



# file_write_length
# called by file_process->file_insert (general file:// processing)

def file_write_length(req,msg,bufsize,filesize,parent):
    msg.logger.debug("file_write_length")

    msg.onfly_checksum = None

    chk = msg.sumalgo
    msg.logger.debug("file_write_length chk = %s" % chk)
    if chk : chk.set_path(msg.new_file)

    # file should exists
    if not os.path.isfile(msg.new_file) :
       fp = open(msg.new_file,'w')
       fp.close()

    # file open read/modify binary
    fp = open(msg.new_file,'r+b')
    if msg.local_offset != 0 : fp.seek(msg.local_offset,0)

    nc = int(msg.length/bufsize)
    r  =     msg.length%bufsize

    # read/write bufsize "nc" times
    i  = 0
    while i < nc :
          chunk = req.read(bufsize)
          fp.write(chunk)
          if chk : chk.update(chunk)
          i = i + 1

    # remaining
    if r > 0 :
       chunk = req.read(r)
       fp.write(chunk)
       if chk : chk.update(chunk)

    if fp.tell() >= msg.filesize:
       fp.truncate()

    fp.close()
  
    h = parent.msg.headers
    if parent.preserve_mode and 'mode' in h :
       try   : mod = int( h['mode'], base=8)
       except: mod = 0
       if mod > 0 : os.chmod(msg.new_file, mod )

    if parent.preserve_time and 'mtime' in h and h['mtime'] :
        os.utime(msg.new_file, times=( timestr2flt( h['atime']), timestr2flt( h[ 'mtime' ] )))

    if chk : msg.onfly_checksum = chk.get_value()

    msg.report_publish(201,'Copied')

    return True

# file_truncate
# called under file_reassemble (itself and its file_insert_part)
# when inserting lastchunk, file may need to be truncated

def file_truncate(parent,msg):

    # will do this when processing the last chunk
    # whenever that is
    if not msg.lastchunk : return

    try :
             lstat   = os.stat(msg.target_file)
             fsiz    = lstat[stat.ST_SIZE] 

             if fsiz > msg.filesize :
                fp = open(msg.target_file,'r+b')
                fp.truncate(msg.filesize)
                fp.close()

                msg.set_topic('v02.post',msg.target_relpath)
                msg.set_notice(msg.new_baseurl,msg.target_relpath,msg.time)
                msg.report_publish(205, 'Reset Content :truncated')

    except : pass
