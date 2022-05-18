<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/kinshukdua/gUPI-recon">
    <img src="./logo.png" alt="Logo" width="250" height="250">
  </a>

<h2 align="center">gUPI-recon</h2>

  <p align="center">
A GUI for reconnaissance using virtual payment address (VPA).<br />
This tool leverages the openness available with the UPI platform to find :<br />
UPI ID and name associated with a mobile number.<br />
UPI ID and name associated with a gmail account.<br />
UPI ID and name associated with a vehicle registration number.<br />
Leveraging UPI id associated with a FASTag.<br />
This project is a GUI port of upi-recon by @squeal.<br />
    <br />
    <a href="https://github.com/kinshukdua/gUPI-recon"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/kinshukdua/gUPI-recon">View Demo</a>
    ·
    <a href="https://github.com/kinshukdua/gUPI-recon/issues">Report Bug</a>
    ·
    <a href="https://github.com/kinshukdua/gUPI-recon/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <li>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#requirements">Requirements</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#disclaimer">Disclaimer</a></li>
  </li>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]]()



<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [upi-recon](https://github.com/qurbat/upi-recon/)
* [PyQt5](https://pypi.org/project/PyQt5/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Requirements

* Install all the requirments

  ```sh
  pip install -r requirements.txt
  ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
* STEP 1: Enter the mobile number or gmail address or vehicle registration number
     
[![Step 1][usage-1]]()
    
* STEP 2: Select the API to use and the UPI to Query
    
[![Step 2][usage-2]]()
   
* STEP 3: Click on the Query button
      
[![Step 3][usage-3]]()


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap
- [ ] Finish remaining features
- [ ] RazorPay API
- [ ] Custom API
- [ ] gmail recon


See the [open issues](https://github.com/kinshukdua/gUPI-recon/issues) for a full list of proposed features (and known issues).

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



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Kinshuk Dua - [@linkedIn](https://linkedin.com/in/dua)

Project Link: [https://github.com/kinshukdua/gUPI-recon](https://github.com/kinshukdua/gUPI-recon)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Disclaimer
Note: Unified Payment Interface ("UPI") Virtual Payment Addresses ("VPAs") do not carry a data security classification by virtue of their usage in practice, and should as such be considered to be public information, similar to how email addresses may be considered to be public information.

This tool allows users to 1) check the existence of UPI payment addresses, and 2) fetch associated information about the account holder, in an automated manner based on provided input. This functionality is already available (however, not in an automated fashion) through most UPI payment applications available on the Android and/or iOS platforms.

This tool is provided "AS IS" without any warranty of any kind, either expressed, implied, or statutory, to the extent permitted by applicable law.
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/kinshukdua/gUPI-recon.svg?style=for-the-badge
[contributors-url]: https://github.com/kinshukdua/gUPI-recon/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kinshukdua/gUPI-recon.svg?style=for-the-badge
[forks-url]: https://github.com/kinshukdua/gUPI-recon/network/members
[stars-shield]: https://img.shields.io/github/stars/kinshukdua/gUPI-recon.svg?style=for-the-badge
[stars-url]: https://github.com/kinshukdua/gUPI-recon/stargazers
[issues-shield]: https://img.shields.io/github/issues/kinshukdua/gUPI-recon.svg?style=for-the-badge
[issues-url]: https://github.com/kinshukdua/gUPI-recon/issues
[license-shield]: https://img.shields.io/github/license/kinshukdua/gUPI-recon.svg?style=for-the-badge
[license-url]: https://github.com/kinshukdua/gUPI-recon/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/dua
[product-screenshot]: screenshots/screenshot.png
[usage-1]: screenshots/usage1.png
[usage-2]: screenshots/usage2.PNG
[usage-3]: screenshots/usage3.PNG
