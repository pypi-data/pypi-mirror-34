AssetBuilder: Compile, Minify and Bundle CSS, JavaScript and other web assets
=============================================================================

AssetBuilder solves the problem of managing assets — CSS files, JavaScript
bundles, images — in your Python web projects.

An ecosystem of tools exists to optimize these assets for web delivery:
compiling and minifying JS and CSS files, optimizing images, and concatentating
asset files to reduce HTTP requests.

- No more wasting time on bugs caused by stale asset files:
  AssetBuilder helps you by automatically triggering your build system whenever
  dependencies change, never serving stale asset files.

- No more shoehorning JavaScript build tools into Python wrappers:
  AssetBuilder works with your existing pipeline by delegating to
  `Gulp <https://gulpjs.com/>`_,
  `Webpack <https://webpack.js.org/>`_,
  `Make <http://man.openbsd.org/make>`_,
  or any other command-line build tool to handle asset
  compilation, optimization and bundling.

- Already works with **Flask**, **Fresco**, **Django**, **Pyramid** and any
  other Python WSGI compatible web framework.

Links
-----

- `AssetBuilder documentation <https://ollycope.com/software/assetbuilder/>`_
- `Bitbucket repo <https://bitbucket.com/ollyc/assetbuilder/>`_
