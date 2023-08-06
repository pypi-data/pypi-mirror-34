# Pillow3f Documentation
### Was PyOpenGL Giving you headaches? You didn't care about real time, you just wanted 3D? Welcome to Pillow3f.
Currently, Pillow3f only boasts one module, `Renderer.py`, imported using `import Pillow3f.Renderer`

In there, you will find a class named `RenderPipeline`, used like this: `RenderPipeline(width, height)`

___

`RenderPipeline.patch`

Averages between pixels to create a smoother output. 

**Adds 2-5 seconds of rendering time.**

___

`RenderPipeline.triangle`

is used like this:

```Python
Surface = ((1, 0, 0), (-1, 0, 0), (0, 1, 0))
Color = ((1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1))
RenderPipeline(600, 800).triangle(Surface, Color)
```
`RenderPipeline.triangle` takes a tuple of verticies, which size 3 vectors. Numpy arrays, lists, and tuples are all accepted. 

**Adds 0.2 to 2 seconds of render time**

___

`RenderPipeline.quad` 

Much like triangle, except it uses 4 verticies instead of 3. It is used like this.

```Python
Surface = ((-1, 1, 0), (1, 1, 0), (-1, -1, 0), (1, -1, 0))
Color = ((1, 1, 1, 1), (0, 1, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1))
RenderPipeline(600, 800).quad(Surface, Color)
```
**Adds 0.2-3 seconds of render time**
___

`RenderPipeline.vertex(vector, color)` 

Accepts a vector of size 3 and a color, and outputs a pixel at that position of that color

```Python
vec3 = (2, 3, 4)
Color = (0, 1, 0.5, 1)
RenderPipeline(600, 800).vertex(vec3, color)
```
That makes an aqua colored pixel at 3D coordinates 2, 3, 4

**Adds a few miliseconds to render time**

___

`RenderPipeline.update`

Moves data from the buffer to the bitmap. This loads the pixels onto the image. Do this everytime you wish to render something.

___

`RenderPipeline.parent_map`

This is a PIL/Pillow object, the main image. whatever you can do to a Pillow image, you can do to this. Resizing, Rotating, all of that good stuff. 

___

`RenderPipeline.bitmap`

This is also a PIL/Pillow object, recieved using `RenderPipeline.parent_map.load()`. This is the main place for pixel manipulation. 
To learn how to use this, I would read up on Pillow documentation at https://pillow.readthedocs.io/en/5.2.x/ 
or go straight here for this: https://pillow.readthedocs.io/en/5.2.x/reference/PixelAccess.html

___

`RenderPipeline.angle` 

This is not fully done, but this provides a way to get the global rotation of a triangle. Make sure to make the verticies seperate parameters.

___

`RenderPipeline.camera`

This is quite simple. The camera is in the format: `[[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]`  
The first vector is the position of the camera, and the second is the rotation of the camera. This is used when rendering faces and verticies.

___

`RenderPipeline.project` 

Takes 4 parameters, Vertex, Camera position, Camera rotation, and field of view. It is used in this fashion:

```Python
>>> x, y = RenderPipeline(600, 800).project([1, 1, 1], [2, -5, -20], [45, 5, 32], 45)
>>> print(x, y)
-71.68011703864057 -388.2248314209303
```
As you can see, it takes a vertex, camera data, and a field of view and squashes it to a 2D vector. 
It is projected to fit the image.

___

## Problems, Quirks, Bugs.

So far, this is not quite usable. I have not added a fully functioning clipping method, and there are artifacts that appear on widely stretched or rotated qauds/triangles. I plan on fixing all of this.

## The Future

I plan on adding:

- Montecarlo Path tracing
- More Rasterization methods
- 2D Image Filters
- 3D Image Filters
- Normals
- Pixel Shaders
- Vertex Shaders
- .obj and .mtl file loading
- Textures

My whole plan is to reduce headaches. I will do my best to ensure these features are added so that it is most convienent and easy to use for the user.
