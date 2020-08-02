
![Heroku](https://heroku-badge.herokuapp.com/?app=digit-server)

# diGIT

An API to serve image as numbers.


## Summary

This project was created as a way to add a layer of abstraction on github profile READMEs

The server is hosted on heroku and accessible here:

Link :  [diGit server](https://digit-server.herokuapp.com/)

## Instructions for Use

These are the same instruction available on the server home page.

diGit returns an image with number when a number is passed to the API

For example: 


Digits: <a href="https://digit-server.herokuapp.com/digit?n=420" target="_blank"> Send request for 420</a> :   ![](static/small_420.jpeg)


Scale:  <a href= "https://digit-server.herokuapp.com/digit?n=420&scale=2" target="_blank"> Scale up '420' x2 times </a> :   ![](static/large_420.jpeg)


Blank space: use <a href="https://digit-server.herokuapp.com/spacer" target="_blank"> spacer</a> :     ![](static/_.jpeg)


All responses are base64 encoded and can be directly used for rendering.

-------------------------------


Now, since github does not support base64 encoded images in README yet, 
to use diGit, please use the API to fetch respective images, store it and then refer it in your [README.md](README.md).


## Authors

   - [**Sanjeev Tripathi**](https://www.linkedin.com/in/sanjeev309/)


## License

This project is licensed under the [MIT license](LICENSE.md)
