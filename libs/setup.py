from distutils.core import setup


setup(
        name='voat_sql',
        version='0.1',
        packages=[
                    'voat_sql', 
                    'voat_sql.schemas',
                    'voat_rest'],

        license='GPL v3'
     )
