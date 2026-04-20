from setuptools import find_packages,setup 

def get_requirements():
    try:
        requirements = []
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.replace('\n','').strip()
                requirements.append(line)
            if '-e .' in requirements:
                requirements.remove('-e .')
            return requirements 
    except Exception as e:
        print(e)

setup(
    name='networksecurity',
    version='0.0.1',
    author='vittal bharadwaj',
    author_email='t.vittalbharadwaj@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)
    
        

