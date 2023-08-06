.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

========================
visaplan.recipe.symlinks
========================

**Not working yet - resource detection missing**

Creates symbolic links to the resources which are registered by the installed
Zope products / packages.  Allows to exclude all ``/++resource++*`` paths from the
RewriteRule which hands the requests over to ZServer.
This serves two purposes:

- The ``/++resource++*`` paths can be handled by your front http server, e.g. Apache,
  instead of the Zope server, which is likely to be better in this task
- All changes to those resources are effective immediately when they are next requested,
  not requiring a Zope restart nor a refresh of the compilation,
  which is useful during develoment.

Currently this recipe requires an operating system which provides native
symbolic links support via the ``os.symlink`` function.

Features
--------

- Creates symbolic links for every resource which is registered to a Zope
  instance.

  This allows those resources to be served by the front http server rather than
  proceeding them to the Zope server and thus unburden the Python threads.

  It also allows to use ``/++resource++*`` paths in error pages including those
  which are used by the front-end server to indicate the Zope process to be
  down (HTTP status codes 5xx).


Usage
-----

Add a visaplan.recipe.symlinks part to your buildout::

    [buildout]

    ...
    parts =
        ...
        symlinks

    [symlinks]
    recipe = visaplan.recipe.symlinks
    document-root = ${buildout:parts-directory}/htdocs
    eggs = ${instance:eggs}

and then run ``bin/buildout``.


Options
-------

document-root
    The ``DocumentRoot`` of your ``VirtualHost`` (in Apache-speak),
    which is the location your http server will start looking for the files to
    serve.

    The default is a ``htdocs`` subdirectory of ``${buildout:parts-directory}``;
    it will be created unless already present.

eggs
    The list of eggs which are installed to your Zope instance;
    if you have an ``[instance]`` section in your buildout script,
    ``${instance:eggs}`` will be the default.

    *(not yet implemented)*

relative-links
    Determines whether relative links will be created.
    Allowed values are:

    yes, on
        use paths relative to ``document-root`` (or to the created
        directories, respectively).

        Might fail in cases the use of relative paths is not possible or not
        advisable, e.g. if the path to ``document-root`` contains symbolic links.

        *(No such checks implemented currently)*

    no, off
        use absolute paths as link targets

link-leaves
    Allowed values are:

    yes, on
        For products which register a resource directory, create a matching
        directory below ``document-root`` and create a dedicated symbolic link
        for each single resource ("leaf").  This can be considered a little bit
        more safe, as it won't make available any resource which was added
        after built time.

    no, off
        For products which register a resource directory, simply create a
        symbolic link to that directory.

        This comes in handy for development.

    auto
        Create symbolic links to resource directories for development packages
        (like ``yes``), and leaf links for all other packages.

        Once implemented, this will likely become the default.

    For now, the ``auto`` choice is not yet implemented.


Contribute
----------

- Issue Tracker: https://github.com/visaplan/visaplan.recipe.symlinks/issues
- Source Code: https://github.com/visaplan/visaplan.recipe.symlinks


Support
-------

If you are having issues, please let us know;
please use the issue tracker mentioned above.


License
-------

The project is licensed under the GPLv2.

.. vim: tw=79 cc=+1 sw=4 sts=4 si et
