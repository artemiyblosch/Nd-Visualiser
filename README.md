<h1>Nd - visualiser: Visual for nd polytopes</h1>

This library is used to create, visualise and manipulate OFF files.
It supports 4OFF, 5OFF, ...

<h2><i>polytope.py</i></h2>
It has everything to store structure of polytopes and import it from OFF files (import_OFF function is used)
<h3>Polytope:</h3>
<strong>It has two properties:</strong>
<ul>
  <li>structure: stores the structure of the polytope by storing an array of verticies, then faces(an array of indicies of verticies in order), then cells(an array of faces) and etc.</li>
  <li>colors: array of colors of facets in order that they appear in the structure.</li>
</ul>
<strong>Methods:</strong>
<ul>
  <li>draw_on(world, [color]) - draws polytope on world with default color.</li>
  <li>rotate(plane, angle, [around_point]) - rotates angle radians in a plane(a pair of indicies of axis) around an around_point (or center if not provided)</li>
  <li>upcast(dimension) - polytope verticies are upcast from polytope's dimension to the specified one</li>
</ul>

<h3>import_OFF(path):</h3>
Gets polytope from OFF file.

<h2><i>world.py</i></h2>
It describes a World class that is projecting a polytope to a Tkinter window.
<strong>Its algorithm:</strong>
<ol>
  <li>Projects a point using the projections</li>
  <li>Converts its coordinates to the window coordinates and the domain (numerical coordinates of the window's boundaries)</li>
  <li>Stores it in the image as buffer with opacity</li>
  <li>Draws it on Tkinter window when flushed</li>
</ol>
<strong>Its properties:</strong>
<ul>
  <li>projections: List of projections(applying them in reverse order should return 2D point)</li>
  <li>size: The size of the window</li>
  <li>bg: Background of the canvas</li>
  <li>domain: List of two ranges: it describes boundaries of the window in point coordinates</li>
</ul>
<strong>Its methods:</strong>
<ul>
  <li>project_point, convert_point: Does steps 1) and 2)</li>
  <li>draw_face(points, color): Draws a face</li>
  <li>flush(): Flushes the image buffer</li>
  <li>mainloop([frame_f,f_delay]): Does tkinter mainloop, inserting frame_f function calls with the delay of f_delay</li>
  <li>clear(): Clears the canvas</li>
</ul>
<h2><i>projections.py</i></h2>
Projection functions.
<h3><strong>ortho</strong></h3>
Orthogonal projection(stripping last dimension)
<h3><strong>iso(direction)</strong></h3>
Isometric projection of the last dimension.
<h3><strong>center(center_p)</strong></h3>
Central projection of the last dimension from center_p.
