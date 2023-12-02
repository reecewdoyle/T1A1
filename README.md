# Reece Doyle T1A1 

**Q1	Identify and explain common and important components and concepts of web development markup languages**

In web development, a markup language is the used to create a website. The markup language itself does not appear on the screen, but it does handle the formatting and structure of the website. The markup language gives the web browser instructions for what each component of the website therefore how and where it should be displayed. (p101 Hirwade)

Hyper Text Markup Language (HTML) is the most common markup language, however, some others that exist include Dynamic HTML (DHTML), Extensible HTML (XHTML) and Extensible Markup Language (XML). (p104 Hirwade)

The common and important components across these markup languages is the use of a combination of symbols and plain text. HTML is mostly written with the angle brackets<>, where there is an opening set < > and a closing set that adds a backslash </ >. 
A H tag with a number would indicate a heading with a size (1 being the largest) while a P tag would indicate a paragraph. A common example would be < h1 >This is a Heading< /h1> or < p>This is a paragraph< /p>. (p6 Cottrell)

XHTML was an upgraded version of HTML created to fix some of the flaws, mostly relating to syntax. Developers now had to pay more attention to making sure all tags were closed and nested properly, all in lowercase. Attributes applied to a tag had to be in quotation marks. For example, <p id=”main-text”>This is the main paragraph.</p> (p6 Cottrell)


DHTML is a markup language that combines elements of HTML for authoring a website, Cascading Style Sheet (CSS) for styling, and Javascript for programming. It allows the developer to create highly interactive websites. It is sometimes referred to as DOM scripting. (p254 Cottrell)



Hirwade, M., & Hirwade, A. W. (2009). Information technology : A practical manual. Global Media. 

Lee M. Cottrell. HTML & XHTML DeMYSTiFieD. McGraw Hill; 2011. Accessed November 28, 2023. https://search.ebscohost.com/login.aspx?direct=true&AuthType=custuid,ip,uid&custid=ns196358&db=nlebk&AN=347015&authtype=cookie,custuid&custid=ns196358&site=ehost-live




**Q2    Define the features of the following technologies that are essential in terms of the development of the internet:**
 - *packets*



A packet is a small piece of a larger piece of data that has been transmitted across a network from one node to another. The concept was created by a Polish-American researcher named Paul Baran during the cold war (late 1950s to early 1960s). 

His idea was to move away from a centralised ‘hub and spoke’ network topography to a decentralised model. This would remove the central hub as the single point of failure and as a vulnerability. This method would create redundancy should sections of the network be destroyed in a nuclear attack. A piece of data could take many different routes to get from one node to the other. (p14-16 Ryan)

The problem was that digital messages were too large for the network at the time, so bottlenecks and congestion would be frequent, thus making it highly inefficient. To get around the bandwidth limitations, Baran (and at the same time a UK Computer Scientist Donald Davies) worked out that a digital message could be broken into multiple small and efficient ‘packets’ of data that could be sent from one node and reassembled at the other end upon arrival. Each packet could take its own independent route based on whatever was the most efficient path at the time of transmission. (p17 Ryan)

Due to great resistance to the idea, it would ultimately take until 1976 before the first ever packet data transmission occurred, and it was in the car park of a beer garden no less. (p34 Ryan)

Packet switching has become standard practice for the entire internet. The ability for small packets of data to switch routes to the quickest path between nodes, and then reassembling has proven to be the most efficient way to use the available bandwidth on the network, and the best way to get around inevitable faults and shutdowns. (10:10, Harrison et al, CrashCourse Computer Science #28)

 - *IP addresses (IPv4 and IPv6)*

An Internet Protocol (IP) Address is a unique number that is assigned to every device on the internet. It is used to keep track of internet activity of billions of users every day. It functions somewhat like the address of your house, or the address of a business. 

IP addresses are needed for the same reason that you need both a send and return address when posting a physical item. When browsing the internet, your device requests the website held on a server at a particular IP address. The server then sends the website back to your device’s IP address. 

Originally in 1983 IP addresses were created using the IPv4 numbering format. This is a 32-bit numbering system containing 4 sets of numbers separated by dots which allows for 4.3 billion unique combinations that can be used as IP addresses. The true scope of what the internet would grow to become would’ve been impossible to predict. The idea of there being 4.3 billion devices connected to the internet would likely have felt like the stuff of science fiction. (Cloudflare, What is my IP address?, 2023)


The introduction of Smart devices and Wifi means we have an “internet of things” and need far more unique IP addresses than ever would’ve seemed possible in 1983. It’s estimated that there are currently more than 10 billion devices connected to the internet and growing. (11:13, Harrison et al, CrashCourse Computer Science #28)

To solve this problem, IPv6 was created. IPv6 is a 128-bit format number consisting of 8 groupings of 4 letters or numbers separated by colons. This allows for a 39 digit number of unique IP addresses, as well as some upgrades in security and privacy. (Cloudflare, What is my IP address?, 2003)

 - *routers and routing*

In the context of a network, routing is the path that data packets take to get from one device to another. Routers are the network hardware that forwards and receives the data packets. They determine the most efficient path to send data packets. In small networks, there might be a static path that is always the same. However, for larger and wider spanning networks routers use routing tables to determine the most efficient route for data to get to its destination, not unlike how a GPS navigator will dynamically direct a car based on its location. This could be through multiple servers, across multiple networks, even across multiple countries involving millions of data packets and millions of decisions per second. (CloudFlare, What is routing?, 2023)

 - *domains and DNS*

“The Domain Name System (DNS) is the phonebook of the Internet.” (CloudFlare, What is DNS?, 2023)

DNS allows people to remember a domain name rather than memorise and IP address. When attempting to load a webpage into a browser, the user will likely use a Uniform Resource Locator (URL) consisting of the Scheme (http:// or https://) and at least the domain name (www.example.com). (MDN, What is a URL?, 2023)

This sends a request to the organisations DNS Server, which consists of multiple machines and multiple processes that delivers the IP address of the website the user requested. Using the user’s IP address as the destination, the DNS server sends back the IP address of the website. This IP address is then used to retrieve and display the website the end user was looking for. This is an entirely different server from the DNS server. (CloudFlare, DNS server types, 2023)


**Explain how each technology has contributed to the development of the internet.**


Each of these technologies has contributed significantly to the development of the internet. Packet switching in conjunction with routers and routing has made transferring packets of data efficient and fast over inexpensive and fault-resistant networks. Without them, congestion would make the internet unusable. IP addresses have created an efficient method for devices to find each other on the internet quickly. DNS has made the internet user friendly to the largest possible number of people. Without it, people would have needed to remember many complex IP addresses which would’ve slowed down the adoption of the internet’s development. 




Ryan, Johnny. A History of the Internet and the Digital Future, Reaktion Books, Limited, 2010. ProQuest Ebook Central, https://ebookcentral.proquest.com/lib/redhill-ebooks/detail.action?docID=618772.

Harrison, Dr. Chris and Ogan, Dr. Amy, Computer Networks: Crash Course Computer Science #28, CrashCourse, 14 September 2017, https://www.youtube.com/watch?v=3QhU9jd03a0

Cloudflare, What is my IP address, What is an IP address and why does it matter?, 2023, https://www.cloudflare.com/en-au/learning/dns/glossary/what-is-my-ip-address/
Cloudflare, What is DNS? | How DNS works, 2023, https://www.cloudflare.com/en-au/learning/dns/what-is-dns/
MDN Web Docs, What is a URL?, 2023, https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_URL
CloudFlare, DNS Server Types, What are the different types of DNS server?, 2023, https://www.cloudflare.com/en-au/learning/dns/dns-server-types/
CloudFlare, What is routing? |IP routing, 2023, https://www.cloudflare.com/en-au/learning/network-layer/what-is-routing/



**Q3	Define the features of the following technologies that are essential in terms of the development of the internet:**
 - *TCP*
 - *HTTP and HTTPS*
 - *web browsers (requests, rendering and developer tools)*

**Explain how each technology has contributed to the development of client and server communication over the internet (50 - 150 words for each technology)**

**Q4	Identify THREE data structures used in the Python programming language and explain the reasons for using each.**

**Q5	Describe the features of interpreters and compilers and how they are different.**

**Q6	Identify TWO commonly used programming languages and explain the benefits and drawbacks of each.**

**Q7	Identify TWO ethical issues from the areas below and discuss the extent to which an IT professional is ethically responsible in terms of the issue.

List of topics containing ethical issues:
 - access to a user’s personal information (medical, family, financial, personal attributes such as sexuality, religion, or beliefs)
 - intellectual property, copyright, and acknowledgement.
 - criminal acts such as theft, fraud, trafficking and distribution of prohibited substances, terrorism
 - GPS tracking data and other types of metadata, MAC addresses, hardware fingerprints
 - freedom of thought, conscience, speech and the media
 - aggressive sales and marketing practices designed to mislead and deceive consumers
 - trading of shares on the stock exchange OR crypto-currencies

For each ethical issue identify a source of legal information relating to the ethical issue and discuss whether the law is helpful in assisting a developer to act in an ethical way. (Word count guide: 200 words max)

Conduct research into a case study of ONE of the ethical issues you have chosen discuss how an ethical IT professional should respond to the case study and how they might mitigate or prevent ethical breaches. (Word count guide: 400 - 600 words)