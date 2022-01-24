<div id="top"></div>

<h3 align="center">Leaderboard Reader</h3>

  <p align="center">
    Python Project for reading the leaderboard data in Dauntless
    <br />
    <a href="https://github.com/clepag/leaderboardReader"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/clepag/leaderboardReader/issues">Report Bug</a>
    ·
    <a href="https://github.com/clepag/leaderboardReader/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project helps you to keep record of the solo leaderboards in Dauntless by reading the entries from the screen to a csv file

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [python](https://www.python.org/)
* [tesseract](https://github.com/tesseract-ocr/tesseract)
* [pytesseract](https://github.com/madmaze/pytesseract)
* [opencv](https://github.com/opencv/opencv-python)
* [numpy](https://numpy.org/)
* [pillow](https://python-pillow.org/)
* [pynput](https://github.com/moses-palmer/pynput)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To run this project you need to meet following prerequisites
It is recommended to create a [virtual environment](https://docs.python.org/3/tutorial/venv.html) to set up the project dependencies

### Prerequisites

* Python https://www.python.org/downloads/
* Tesseract https://github.com/tesseract-ocr/tesseract#installing-tesseract
Make sure to add the python and tesseract folder paths to your environment variables when using Windows

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/clepag/leaderboardReader.git
   ```
2. Set up the virtual environment
  
  Install virtualenv 
   ```sh
   pip install virtualenv
   ```
   
   In the project directory create a virtualenv
   ```sh
   virtualenv <myenv>
   ```
   
   In the same directory type
   ```sh
   <myenv>\Scripts\activate
   ```
   to activate the virtual environment
   
3. Install requirements according to requirements.txt
   ```sh
   pip install -r /path/to/requirements.txt
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The code currently expects a screen resoution of 2560x1440. If you want to run the project on a different resolution you need to adjust the screen capture region and possibly replace the images for the symbol filtering.

Depending on wheter you already got a placement for the trial week you need to adjust following variable:
   ```py
   already_placed = True|False
   ```
You can run the code by opening the leaderboard and running the code from the console. Make sure the console does not overlap with the ranking display
   ```sh
   python main.py
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Team Trials
- [ ] Omnicell data


See the [open issues](https://github.com/clepag/leaderboardReader/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [othneildrew]https://github.com/othneildrew) README template

<p align="right">(<a href="#top">back to top</a>)</p>

