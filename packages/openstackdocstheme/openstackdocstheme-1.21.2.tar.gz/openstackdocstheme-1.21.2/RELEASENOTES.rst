==================
openstackdocstheme
==================

.. _openstackdocstheme_1.20.0:

1.20.0
======

.. _openstackdocstheme_1.20.0_New Features:

New Features
------------

.. releasenotes/notes/autoconfigure-settings-7083fdeeb121da89.yaml @ b'3c8b2a698864afea55bf2247d6c50baadaf4fb72'

- The following configuration variables, normally defined in ``conf.py``,
  can now be configured automatically.
  
  - ``project``
  - ``version``
  - ``release``
  - ``html_last_updated_fmt``
  - ``latex_engine``
  - ``latex_elements``
  
  It is not necessary to retain any configuration in ``conf.py`` and, in most
  cases, such configuration will be ignored. The sole exceptions to this rule
  are ``version`` and ``release`` which, if set to ``''`` will not be
  overridden. This allows for unversioned documentation.


.. _openstackdocstheme_1.18.0:

1.18.0
======

.. _openstackdocstheme_1.18.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/double-backticks-not-red-5ce6dbc828221929.yaml @ b'e99cf6d96c0c79805ad2c155948e55d89704ce90'

- The double backticks (``) markup caused text to be displayed in red with
  a pinkish background colour. The text is now displayed in black and bold.


.. _openstackdocstheme_1.17.0:

1.17.0
======

.. _openstackdocstheme_1.17.0_Prelude:

Prelude
-------

.. releasenotes/notes/local-project-search-e6f00a84f2eed0a6.yaml @ b'a5ceb6f15d3d0a177efd016aad5e148d42f50247'

Adds scoped search so that readers can search within project documentation only.


.. _openstackdocstheme_1.17.0_New Features:

New Features
------------

.. releasenotes/notes/local-project-search-e6f00a84f2eed0a6.yaml @ b'a5ceb6f15d3d0a177efd016aad5e148d42f50247'

- Adds ability to use the Sphinx search implementation only for the content
  for the project, such as nova or keystone. The default settings set the
  search scope to within the built version and only for .html files.

.. releasenotes/notes/local-project-search-e6f00a84f2eed0a6.yaml @ b'a5ceb6f15d3d0a177efd016aad5e148d42f50247'

- Readers access the search functionality through a link to Search from the top-most landing page for the project documentation.


.. _openstackdocstheme_1.13.0:

1.13.0
======

.. _openstackdocstheme_1.13.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/do-not-display-local-toc-title-without-subtitles-4e1fc48705d66289.yaml @ b'd9bc11a97920bc1eeb1dba394f4fef6be502eed3'

- The title "Contents" of the page local TOC is now displayed
  only when a page has sub-titles.

.. releasenotes/notes/strip-html-tags-from-navigation-titles-929c92a339413015.yaml @ b'd727e522b910e29b245d394cb8199a67477dd157'

- The navigation links now correctly strip HTML from titles, allowing for
  use of markup like literal backticks in titles.


.. _openstackdocstheme_1.12.0:

1.12.0
======

.. _openstackdocstheme_1.12.0_Prelude:

Prelude
-------

.. releasenotes/notes/version-dropdown-1aa39974f524dd75.yaml @ b'1b63fd10c5e2f4cbca91661eec5dabd682da7606'

Adds ability to show up to the last five versions of the documentation, based on the available git tags for the repository. Use the theme variable, ``show_other_versions`` to chose to display the available versions in a dropdown menu.


.. _openstackdocstheme_1.12.0_New Features:

New Features
------------

.. releasenotes/notes/storyboard-5f67da8941aec6ae.yaml @ b'9a6159a529d9f7951c29844d5d5d8d84d718c8a3'

- Initial integration of storyboard.openstack.org for report a bug, set ``bug_project`` to the number of the project to use it.

.. releasenotes/notes/version-dropdown-1aa39974f524dd75.yaml @ b'1b63fd10c5e2f4cbca91661eec5dabd682da7606'

- Adds the option to configure the display of a version selector dropdown
  menu for the most recent five git tags used as release indicators for the repository.
  By default, in ``theme.conf``, the ``show_other_versions`` value is set to
  False.
  In ``conf.py``, set the theme variable, ``html_theme_options`` to
  include the parameter, ``show_other_versions`` as ``True``. For
  example:
  
  ::
  
    html_theme_options = {'show_other_versions': True}

.. releasenotes/notes/version-dropdown-1aa39974f524dd75.yaml @ b'1b63fd10c5e2f4cbca91661eec5dabd682da7606'

- Publishes a version dropdown menu in the "Updated" date row, on both mobile and desktop views, where the version list is imported from git tags on the repository.


.. _openstackdocstheme_1.12.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/bug_project-d26160cfe5324694.yaml @ b'a713646d06a75ebbca7106813d807dbf4e8b4876'

- If ``bug_project`` is not set, the "Report a bug" links are not displayed at all.


.. _openstackdocstheme_1.6.1:

1.6.1
=====

.. _openstackdocstheme_1.6.1_New Features:

New Features
------------

.. releasenotes/notes/doc-bug-template-7234e7f00e0ff599.yaml @ b'58823b338cbeffeacce5b524269a5e6f194bbce9'

- Adds additional information to the doc bug template used on Launchpad when a reader clicks the doc bug icon to report a bug.


.. _openstackdocstheme_1.6.1_Other Notes:

Other Notes
-----------

.. releasenotes/notes/doc-bug-template-7234e7f00e0ff599.yaml @ b'58823b338cbeffeacce5b524269a5e6f194bbce9'

- Implemented intially to guide people to better ways to get end-user support rather than log a doc bug.


.. _openstackdocstheme_1.5.0:

1.5.0
=====

.. _openstackdocstheme_1.5.0_Prelude:

Prelude
-------

.. releasenotes/notes/sidebar_dropdown_apiref-993b4dba4c0369f6.yaml @ b'47149987c169976d8cd4bc34c1f2d7bb02874cc0'

Adds a theme variable, ``sidebar_dropdown`` to configure the display of the new API sidebar dropdown menu.


.. _openstackdocstheme_1.5.0_New Features:

New Features
------------

.. releasenotes/notes/allow-disabling-toc-in-body-d98d3a6e633fa28e.yaml @ b'59072440ab4e44b3e14d3cf6069751e28161503b'

- The automatic table of contents that appears in the body of the
  documentation can be disabled by setting ``display_toc`` to ``False`` in
  the ``html_theme_options`` option in ``conf.py``.
  
  For example:
  
  .. code-block:: python
  
    html_theme_options = {
         "display_toc": False,
    }

.. releasenotes/notes/sidebar_dropdown_apiref-993b4dba4c0369f6.yaml @ b'47149987c169976d8cd4bc34c1f2d7bb02874cc0'

- Adds the option to configure the display of a sidebar dropdown
  menu for published API References and Guides.
  In conf.py, set the theme variable, ``html_theme_options`` to
  include the parameter, ``sidebar_dropdown`` as ``api_ref``. For
  example:
  
  ::
  
    html_theme_options = {
         "sidebar_dropdown": "api_ref",
      }
  
  The extensions parameter should include the sphinx extension,
  ``os_api_ref``.
  
  ::
  
    extensions = [
        'os_api_ref',
    ]

.. releasenotes/notes/sidebar_dropdown_apiref-993b4dba4c0369f6.yaml @ b'47149987c169976d8cd4bc34c1f2d7bb02874cc0'

- Publishes an API Reference demo which is integrated with the API sidebar dropdown menu.


.. _openstackdocstheme_1.4.0:

1.4.0
=====

.. _openstackdocstheme_1.4.0_Prelude:

Prelude
-------

.. releasenotes/notes/custom-bug-link-ec64bdf9ce357d16.yaml @ b'16c47a00a8c7803debfba8ea8af792b9bd94eaf6'

In preparation for releasing updated API reference documentation using this theme, we have a collection of new features and fixes.


.. _openstackdocstheme_1.4.0_New Features:

New Features
------------

.. releasenotes/notes/bug-title-fdbefea0408e2cbf.yaml @ b'13bd97688aa51d6b3a292f0c97b7f1e3ea7cb120'

- The ability to customise the bug title for the 'Report a Bug'
  link is now available. To customise the bug title used add
  the ``bug_title`` key with a value to ``html_context`` in the
  Sphinx configuration.
  
  For example:
  
  ::
  
    html_context = {"bug_title": 'Documentation bug', ...}

.. releasenotes/notes/custom-bug-link-ec64bdf9ce357d16.yaml @ b'16c47a00a8c7803debfba8ea8af792b9bd94eaf6'

- Ensure Javascript and CSS files are pulled in programmatically to enable custom Javascript and CSS files.

.. releasenotes/notes/custom-bug-link-ec64bdf9ce357d16.yaml @ b'16c47a00a8c7803debfba8ea8af792b9bd94eaf6'

- CSS adjustments to ``inline`` markup and contents indentation.

.. releasenotes/notes/custom-bug-link-ec64bdf9ce357d16.yaml @ b'16c47a00a8c7803debfba8ea8af792b9bd94eaf6'

- Enable custom bug title link.

.. releasenotes/notes/custom-bug-link-ec64bdf9ce357d16.yaml @ b'16c47a00a8c7803debfba8ea8af792b9bd94eaf6'

- Adds sidebar_mode for table of contents as an option for html_theme_options in conf.py.

.. releasenotes/notes/side-bar-config-d7e66388e252cadf.yaml @ b'75e8fc6e800b0da5b152de64cbce79f47c6938d6'

- The sidebar Table of Contents can now be set to the full ``toc`` directive,
  or remain as the ``toctree`` directive.
  
  This can be set by setting ``"sidebar_mode"`` to ``"toc"`` in the
  ``html_theme_options`` option in ``conf.py``.
  
  For example:
  
  ::
  
    html_theme_options = {
         "sidebar_mode": "toc",
      }


.. _openstackdocstheme_1.4.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/custom-bug-link-ec64bdf9ce357d16.yaml @ b'16c47a00a8c7803debfba8ea8af792b9bd94eaf6'

- Use HTTPS for external dependencies.

.. releasenotes/notes/custom-bug-link-ec64bdf9ce357d16.yaml @ b'16c47a00a8c7803debfba8ea8af792b9bd94eaf6'

- Replace deprecated library function os.popen() with subprocess. (1529836)

.. releasenotes/notes/custom-bug-link-ec64bdf9ce357d16.yaml @ b'16c47a00a8c7803debfba8ea8af792b9bd94eaf6'

- Update contribute link in footer. (1421814)

.. releasenotes/notes/custom-bug-link-ec64bdf9ce357d16.yaml @ b'16c47a00a8c7803debfba8ea8af792b9bd94eaf6'

- Hide duplicate titles and empty tocs in generated content.


.. _openstackdocstheme_1.3.0:

1.3.0
=====

.. _openstackdocstheme_1.3.0_Other Notes:

Other Notes
-----------

.. releasenotes/notes/norelease-ccd7722c078a73a2.yaml @ b'acbab4cd804c7b4e43572be52106a1bb7c0e439a'

- The sidebar is not version dependent anymore, it always links to the main page.


.. _openstackdocstheme_1.2.7:

1.2.7
=====

.. _openstackdocstheme_1.2.7_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/sidebarlinks-db0a8463f32ab95d.yaml @ b'343e6bf59501e416877fc547efdcde327ec31ad0'

- Fix links on sidebar to go to docs.openstack.org instead of non-existing places (Launchpad bug


.. _openstackdocstheme_1.2.6:

1.2.6
=====

.. _openstackdocstheme_1.2.6_New Features:

New Features
------------

.. releasenotes/notes/bug-project-e9ff50f6149d2be1.yaml @ b'119f9888b9d4832a976c440f517043d946cd833c'

- Some teams use openstackdocstheme which have each launchpad project. To report a bug to the appropriate project directly, enable each project to define the bug report project.

.. releasenotes/notes/disable_analytics-45d98d6fab71d2b1.yaml @ b'89b0475539ac6763baa27f5fc334639ee3853ebf'

- Google Analytics tracking may now be controlled by setting the ``analytics_tracking_code`` option, or removed entirely by leaving that option blank.


.. _openstackdocstheme_1.2.5:

1.2.5
=====

.. _openstackdocstheme_1.2.5_New Features:

New Features
------------

.. releasenotes/notes/sidebar-top-page-link-252532ddf42a5acf.yaml @ b'9ad2bfb2713e090ac98f43315b080fa53bfadf2d'

- Contents in the sidebar TOC is now a link to a top page of a document which contains a toc of the document. Now readers can easily move back to a full toc of a document.


.. _openstackdocstheme_1.2.5_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/lp1516819-b4bb7b0f10004cef.yaml @ b'f235ad6b54fb24432a713094201b3c6e372ccb2c'

- Add Google Analytics JavaScript tracking snippet code to resolve Launchpad bug


.. _openstackdocstheme_1.2.5_Other Notes:

Other Notes
-----------

.. releasenotes/notes/add-reno-8da9bd3ccb7bbeab.yaml @ b'7ab7dbe186e7c8ae37175b6388ba764faf3ccc21'

- Use reno for release note management.

