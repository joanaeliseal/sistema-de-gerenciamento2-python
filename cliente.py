#!/usr/bin/env python3

import sys
import socket
import curses
import multiprocessing
from threading import Thread

HOST = '127.0.0.1'
PORT = 8000

def msg_receive(stdscr, input_box):
    lasty, lastx = stdscr.getmaxyx() 
    msg_box = curses.newwin(lasty-2,lastx,0,0)
    msg_box.scrollok(True)
    while True:
        msg, serv = sock.recvfrom(1024)
        if not serv or serv[0] == 0: 
            # Thread main solicitou encerramento
            break
        lock.acquire()
        try:
            msg_box.addstr(f'Recebido> {msg.decode()}\n')
            msg_box.refresh()
            input_box.refresh()
        finally:
           lock.release()

def main(stdscr):
    stdscr.clear()
    curses.echo()
    lasty, lastx = stdscr.getmaxyx() 
    input_box = curses.newwin(2,lastx,lasty-2,0)    
    Thread(target=msg_receive,args=(stdscr, input_box)).start()
    while True:
        lock.acquire()
        try:
            input_box.clear()
            input_box.addstr('Enviar> ')
            input_box.refresh()
        finally:
            lock.release()
        try:
            msg = input_box.getstr().decode()
            if msg.lower() == 'sair':
                try:
                    # Solicita fechamento do socket
                    sock.shutdown(socket.SHUT_RDWR)
                    sock.close()
                except: pass
                break
            sock.sendto(msg.encode(), servidor)
        except: pass

if len(sys.argv) > 1:
    HOST = sys.argv[1]

cliente  = ('0.0.0.0', 0)
servidor = (HOST, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(cliente)
lock = multiprocessing.Lock()

curses.wrapper(main)
