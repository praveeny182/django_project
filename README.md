# Project Name: Document and Image Converter API

## Overview

This project is a Django REST API-based web application that offers a range of document and image conversion functionalities. Leveraging various Python libraries, the application enables users to convert documents between different formats, such as doc to pdf and pdf to doc. Additionally, it provides image processing capabilities like image resizing and color to black and white conversion. The application is containerized using Docker, ensuring easy deployment and scalability.

## Key Features

### Document Conversion:

- Convert doc to pdf: Users can upload a Word document, and the API will generate a corresponding PDF file.
- Convert pdf to doc: Users can submit a PDF document, and the API will produce a Word document as output.

### Image Processing:

- Image Resizing: Users can upload an image and specify the desired dimensions, and the API will resize the image accordingly.
- Color to Black and White: Users can transform a colored image into a black and white version using the API.

## Technical Stack

- Backend Framework: Django with Django REST framework.
- Document Conversion Libraries: Python libraries like PyPDF2 for PDF handling and python-docx for Word document processing.
- Image Processing Libraries: Python Imaging Library (PIL) or Pillow for image resizing and color manipulation.
- Containerization: Docker is used to create a container image of the application, allowing seamless deployment on various platforms.

## Deployment

The entire application, including all required dependencies, is packaged into a Docker image.

### Docker Image

The Docker image for this project is available on Docker Hub:
docker pull praveeny182/converter


To run the container:
docker run -p 8000:8000 praveeny182/converter

Replace `-p 8000:8000` with the desired port mapping if needed.

## Usage

Once the container is running, the API endpoints can be accessed via HTTP requests. Detailed API documentation with usage instructions is available at [API Documentation URL].

## Contributions

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on [GitHub Repository URL].

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or further information, feel free to contact me:

- Name: Praveen Kumar Yadav
- Email: praveeny182@gmail.com
- LinkedIn: [https://www.linkedin.com/in/praveen-yadav-55020b163/]

Thank you for your interest in this project!



