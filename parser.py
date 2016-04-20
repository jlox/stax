from display import *
from matrix import *
from draw import *



ARG_COMMANDS = [ 'line', 'scale', 'translate', 'xrotate', 'yrotate', 'zrotate', 'circle', 'bezier', 'hermite', 'sphere', 'box', 'torus', 'color']

def parse_file( f, points, stack, screen, col ):

    commands = f.readlines()

    color = col
    
    c = 0
    while c  <  len(commands):
        cmd = commands[c].strip()
        if cmd in ARG_COMMANDS:
            c+= 1
            args = commands[c].strip().split(' ')
            i = 0
            while i < len( args ):
                args[i] = float( args[i] )
                i+= 1

            if cmd == 'line':
                temp = []
                add_edge( points, args[0], args[1], args[2], args[3], args[4], args[5] )
                matrix_mult( stack[len(stack) - 1], temp )
                draw_lines( temp, screen, color )
                
                
            elif cmd == 'circle':
                temp = []
                add_circle( points, args[0], args[1], 0, args[2], .01 )
                matrix_mult( stack[len(stack) - 1], temp )
                draw_lines( temp, screen, color )
                
            
            elif cmd == 'bezier':
                temp = []
                add_curve( points, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], .01, 'bezier' )
                matrix_mult( stack[len(stack) - 1], temp )
                draw_lines( temp, screen, color )
                
            
            elif cmd == 'hermite':
                temp = []
                add_curve( points, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], .01, 'hermite' )
                matrix_mult( stack[len(stack) - 1], temp )
                draw_lines( temp, screen, color )
                

            elif cmd == 'sphere':
                temp = []
                add_sphere( temp, args[0], args[1], 0, args[2], 7 )
                matrix_mult( stack[len(stack) - 1], temp )
                draw_polygons( temp, screen, color )
                
                
            elif cmd == 'torus':
                temp = []
                add_torus( temp, args[0], args[1], 0, args[2], args[3], 5 )
                matrix_mult( stack[len(stack) - 1], temp )
                draw_polygons( temp, screen, [255, 0 ,0] )
                
                
            elif cmd == 'box':
                temp = []
                add_box( temp, args[0], args[1], args[2], args[3], args[4], args[5] )
                matrix_mult( stack[len(stack) - 1], temp )
                draw_polygons( temp, screen, color )
                
                
            elif cmd == 'scale':
                s = make_scale( args[0], args[1], args[2] )
                matrix_mult( s, stack[len(stack) - 1] )

            elif cmd == 'translate':
                t = make_translate( args[0], args[1], args[2] )
                matrix_mult( t, stack[len(stack) - 1]  )
                
            else:
                angle = args[0] * ( math.pi / 180 )
                if cmd == 'xrotate':
                    r = make_rotX( angle )
                elif cmd == 'yrotate':
                    r = make_rotY( angle )
                elif cmd == 'zrotate':
                    r = make_rotZ( angle )
                matrix_mult( r, stack[len(stack) - 1] )

        elif cmd == 'ident':
            ident( stack[len(stack) - 1] )
            
        elif cmd == 'apply':
            matrix_mult(  stack[len(stack) - 1], points )

        elif cmd in ['display', 'save', 'push', 'pop']:
            
            #draw_polygons( points, screen, color )
            
            if cmd == 'display':
                display( screen )

            elif cmd == 'save':
                c+= 1
                save_extension( screen, commands[c].strip() )

            elif cmd == 'push':
                stack.append(stack[len(stack) - 1])

            elif cmd == 'pop':
                stack.pop()
            
        elif cmd == 'quit':
            return    
        elif cmd[0] != '#':
            print 'Invalid command: ' + cmd
        c+= 1
