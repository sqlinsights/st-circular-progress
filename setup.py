import setuptools

setuptools.setup(
    name="st_circular_progress",
    version="0.3.4",
    author="Carlos D Serrano",
    author_email="sqlinsights@gmail.com",
    description="Circular progress wheel for Streamlit",
    long_description="Streamlit custom component based in VanillaJs that generates a Circular Shaped progress bar.",
    long_description_content_type="text/plain",
    url="https://github.com/sqlinsights/st-circular-progress",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 1.20.0",
    ],
)
