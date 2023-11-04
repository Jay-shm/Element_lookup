# Element Information Web Service

This is a Python application that provides information about chemical elements via a web service. It uses the Mendeleev library to retrieve element properties and returns them as JSON responses when accessed through specific routes.

## Installation

1. Make sure you have Python installed on your system. If not, you can download it from [Python's official website](https://www.python.org/downloads/).

2. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/yourusername/element-info-web-service.git
   cd element-info-web-service
   ```

3. Install the required Python packages using pip:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

Start the web service by running the following command:

```shell
python app.py
```

Once the service is running, you can access element information by using the following routes:

### Route 1: `/data/<element>`

- Retrieve element information by providing the element's name.

Example:

```shell
http://localhost:5000/data/hydrogen
```

### Route 2: `/data2/<sym>`

- Retrieve element information by providing the element's symbol.

Example:

```shell
http://localhost:5000/data2/H
```

### Route 3: `/data1/<num>`

- Retrieve element information by providing the element's atomic number.

Example:

```shell
http://localhost:5000/data1/1
```

The service will return element properties in JSON format, including the element's name, symbol, atomic number, atomic weight, density, melting point, boiling point, atomic radius, heat of fusion, specific heat capacity, thermal conductivity, discovered by, and a description.

## Example Usage

You can access the element information through your web browser or use tools like cURL or Python's `requests` library to make HTTP GET requests programmatically.

Here's a Python example using the `requests` library:

```python
import requests

element_name = "hydrogen"
response = requests.get(f"http://localhost:5000/data/{element_name}")
data = response.json()
print(data)
```

## Contribution

If you want to contribute to this project, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
