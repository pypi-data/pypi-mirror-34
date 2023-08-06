Here's a nice little example for you to use. So far this project is in it's infancy, 
but It does have a few features. It has a working depth buffer, a simple surface rasterizer, and clipping. 
So far, that's all it has, but I am getting to the cool stuff like montecarlo path tracing and the ability to load in models.
I still have a few kinks and bugs to work out, like when the triangles get close to the camera or are rotated artifacts appear on the surfaces,
but those should be an easy fix. I will slowly begin releases more features.

Pillow3f get's it's name from the 'Pillow' fork of PIL (Python Imaging Library), which is a library I use to load the geometry,
and OpenGL's suffix, '3f' meaning it's an array of size 3, containing floats, the default of my library. However, it is slightly misleading
This library doesn't use OpenGL for graphics, but uses advantages provided by the python language and my own math.

Pillow3f offers advantages that OpenGL does not have. It offers the ability to manipulate images pixel by pixel, 
It offers all the advantages of Pillow through the RenderPipeline.parent_map and RenderPipeline.bitmap, and also allows special features
that couldn't be done otherwise. One big feature is that images are output in RGBA, and that when rasterizing images, the alpha
is also put on a color gradient. 

Currently, there is only one module, Pillow3f.Renderer, but I plan on seperating some methods into other modules.

I also plan on adding documentation by version 1.0, which will be an offical release.
By version 2.0, I will declare the Library out of it's infancy. I don't really recommend using this right now,
unless you don't mind artifacts and limited features. For now, I will provide an example I used to test the Depth-Buffer.

from Pillow3f.Renderer import RenderPipeline

for x in range(-10, 30):
	print('%s/40'%(x+11))
        time.sleep(1)
        
        Pipe = RenderPipeline(600, 800)
        Pipe.camera = [[0, 0, -5], [0, 0, 0]]
        Pipe.triangle([[-1+(x/10), 0, 0], [-3+(x/10), 0, 0], [-2+(x/10), 2, 0]], ((0.4, 0.6, 0, 1), (1, 0.3, 0.6, 1), (0.75, 0.5, 0, 1)))
        Pipe.triangle([[1-(x/10), 0, -1], [3-(x/10), 0, 1], [2-(x/10), 2, 0]], ((0, 1, 1, 1), (1, 1, 0, 1), (1, 0, 1, 1)))
        
        Pipe.update()

        Pipe.parent_map.show()