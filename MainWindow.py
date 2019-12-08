import pyglet, sys, os

from Window import Window


# def reexec_with_pythonw():
#     if sys.platform == 'darwin' and\
#            not sys.executable.endswith('MacOS/Python'):
#         print >>sys.stderr,'re-executing using pythonw'
#         os.execvp('pythonw',['pythonw',__file__] + sys.argv[1:])
#

if __name__ == '__main__':
    window = Window()
    pyglet.clock.schedule_interval(window.update, 1 // 60)
    pyglet.app.run()

