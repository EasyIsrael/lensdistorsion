  from distutils.core import setup
    setup(
        name = 'lensdistorsion',
        packages = ['lensdistorsion'], # this must be the same as the name above
        version = '0.1',
        description = 'A lib to create a lens distorsion lookup table. It describes the inner orientation of a camera. Useful to create orthorectified or georeferenced images',
        author = 'Martin Israel',
        author_email = 'martin.israel@dlr.de',
        url = 'https://github.com/EasyIsrael/lensdistorsion',   # use the URL to the github repo
        download_url = 'https://github.com/EasyIsrael/lensdistorsion/tarball/0.1', # I'll explain this in a second
        keywords = ['georeference', 'lens distorsion', 'orthophoto', 'inner orientation', 'camera calibration'], # arbitrary keywords
        classifiers = [],
    )