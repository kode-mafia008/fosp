
# 2018 ||  
#! What is Open Source ?
# Open source software is software with source code that anyone can inspect, modify, and
# enhance."Source code" is the part of software that most computer users don't ever see; 
# it's the code computer programmers can manipulate to change how a piece of software—a "program" or 
# "application"—works. Programmers who have access to a computer program's source code can improve that 
# program by adding features to it or fixing parts that don't always work correctly.
#! Emerging application of FOSS in various sectors.
# Open source philosophy is changing the way people think about technology and society. A couple of years
# ago you had to fork out a lot of money to get a good graphics editing computer program (such as Adobe 
# Photoshop). Now you can just download a free version of GIMP. You can even modify its source code to 
# make it better, or simply different, if you feel so inclined. Collaborative open source software 
# projects such as Linux and Apache (a web server package) have demonstrated that a large and complex 
# system of code can be built, maintained, developed and extended in a non-proprietary environment 
# (Source: Weber 2004, p. 2). Outside of the computer world, people have created open source beer and 
# cola. Vast amounts of informative content are being release as open source on sites such as Wikipedia.
# Blogging is becoming a household term, with people globally sharing their views and thoughts for free
# to anyone who wants to listen, watch or read. Even open source pharmaceutical development is on the 
# horizon.Despite the fact that most people would have never predicted that a system based around people
# working for free would work, open source philosophy is making a big impact. The thing to understand is
# that open source embraces the philosophy of sharing, and because of this, concepts such as piracy are 
# no longer a problem. You are encouraged to share and spread open source products as much as you like.
# You can copy and redistribute, even after modification. This provides users with a freedom that is not
# obtainable from proprietary products (as illustrated right throughout this document), and creates 
# remarkable opportunities for businesses and entrepreneurs around the world, especially in developing 
# countries.

#! Types of licenses
#What are the different types of software licenses?
#Here are five types of common software license models you should know about. Four are examples of open 
# source licenses (which allow you to reuse code to some extent), and one disallows any reuse whatsoever.
#Public domain. This is the most permissive type of software license. When software is in the public 
# domain, anyone can modify and use the software without any restrictions. But you should always make 
# sure it’s secure before adding it to your own codebase. Warning: Code that doesn’t have an explicit 
# license is NOT automatically in the public domain. This includes code snippets you find on the internet.

#Permissive. Permissive licenses are also known as “Apache style” or “BSD style.” They contain minimal 
# requirements about how the software can be modified or redistributed. This type of software license is
# perhaps the most popular license used with free and open source software. Aside from the Apache License
# and the BSD License, another common variant is the MIT License.

#LGPL. The GNU Lesser General Public License allows you to link to open source libraries in your software.
# If you simply compile or link an LGPL-licensed library with your own code, you can release your
# application under any license you want, even a proprietary license. But if you modify the library or
# copy parts of it into your code, you’ll have to release your application under similar terms as the 
# LGPL.

#Copyleft. Copyleft licenses are also known as reciprocal licenses or restrictive licenses. The most
# well-known example of a copyleft or reciprocal license is the GPL. These licenses allow you to modify 
# the licensed code and distribute new works based on it, as long as you distribute any new works or 
# adaptations under the same software license. For example, a component’s license might say the work is 
# free to use and distribute for personal use only. So any derivative you create would also be limited to
# personal use only. (A derivative is any new software you develop that contains the component.)

#The catch here is that the users of your software would also have the right to modify the code. 
# Therefore, you’d have to make your own source code available. But of course, exposing your source code 
# may not be in your best interests.

#Proprietary. Of all types of software licenses, this is the most restrictive. The idea behind it is that
# all rights are reserved. It’s generally used for proprietary software where the work may not be modified
# or redistributed.

#! Web Server | Client-Web Server Configuration
#A web server is software and hardware that uses HTTP (Hypertext Transfer Protocol) and other 
# protocols to respond to client requests made over the World Wide Web. The main job of a web server
# is to display website content through storing, processing and delivering webpages to users. Besides
# HTTP, web servers also support SMTP (Simple Mail Transfer Protocol) and FTP (File Transfer Protocol),
# used for email, file transfer and storage.Web server hardware is connected to the internet and
# allows data to be exchanged with other connected devices, while web server software controls how a
# user accesses hosted files. The web server process is an example of the client/server model. All 
# computers that host websites must have web server software.Web servers are used in web hosting, or
# the hosting of data for websites and web-based applications -- or web applications.


#* Examples of web server uses
# Web servers often come as part of a larger package of internet- and intranet-related programs that
# are used for:

# sending and receiving emails;
# downloading requests for File Transfer Protocol (FTP) files; and
# building and publishing webpages.

#! Tags used for effective webpages
#? 4 Basic tags. 
# <!doctype html>
#? <html lang="en">
#?   <head>
#     <!-- Required meta tags -->
#     <meta charset="utf-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1">

#     <!-- Bootstrap CSS -->
#     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

#?     <title>Hello, world!</title>
#   </head>
#?   <body>
#     <h1>Hello, world!</h1>

#     <!-- Optional JavaScript; choose one of the two! -->

#     <!-- Option 1: Bootstrap Bundle with Popper -->
#     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

#     <!-- Option 2: Separate Popper and Bootstrap JS -->
#     <!--
#     <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
#     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
#     -->
#?   </body>
#? </html>
 
#! Linking documents in webpage
#* Ways 
#? Hyperlink  
# HTML Links - The target Attribute
# By default, the linked page will be displayed in the current browser window. To change this, you 
# must specify another target for the link.

# The target attribute specifies where to open the linked document.

# The target attribute can have one of the following values:
#! Types of targets in href

# _self - Default. Opens the document in the same window/tab as it was clicked
# _blank - Opens the document in a new window or tab
# _parent - Opens the document in the parent frame
# _top - Opens the document in the full body of the window
# <h2>Absolute URLs</h2>
# <p><a href="https://www.w3.org/">W3C</a></p>
# <p><a href="https://www.google.com/">Google</a></p>

# <h2>Relative URLs</h2>
# <p><a href="html_images.asp">HTML Images</a></p>
# <p><a href="/css/default.asp">CSS Tutorial</a></p>