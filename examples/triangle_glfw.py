"""
Import the viz from triangle.py and run it in a glfw window.
The glfw library can be installed using ``pip install glfw``.
"""

import glfw
from wgpu.gui.glfw import WgpuCanvas  # WgpuCanvas wraps a glfw window
import wgpu.backend.rs  # noqa: F401, Select Rust backend

# Import the (async) function that we must call to run the visualization
from triangle import main


glfw.init()
canvas = WgpuCanvas(size=(640, 480), title="wgpu triangle with GLFW")

main(canvas)
while not canvas.isClosed():
    glfw.poll_events()
glfw.terminate()
