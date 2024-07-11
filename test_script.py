import subprocess

url = "https://rr2---sn-oxu8pnpvo-ua8z.googlevideo.com/videoplayback?expire=1720755989&ei=tVKQZtCCNK_Ep-oPkpa12As&ip=95.35.111.25&id=o-AJUpxkmfaEQq_-eiPaHE9Ml0LyrVWbgGfwRYqhHInkE6&itag=251&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=ev&mm=31%2C29&mn=sn-oxu8pnpvo-ua8z%2Csn-ua87zn7l&ms=au%2Crdu&mv=m&mvi=2&pl=26&gcr=il&initcwndbps=621250&bui=AXc671LoJw10GdH5QR3Tqwrjo7nIZoLxvNHWZ3A649aTqqA4KzPsurDWIGYj_fn1GSBlgPOu2SPTIWOR&spc=NO7bAedl6qhbpXmHq6lyfACDfvXjFLj0EOYvT_G-M-T-8xRAAa12SdtmwyKM&vprv=1&svpuc=1&mime=audio%2Fwebm&ns=STQfEBUk6iWXiw_xM7My-hEQ&rqh=1&gir=yes&clen=3501218&dur=210.361&lmt=1719543087310827&mt=1720733826&fvip=1&keepalive=yes&c=WEB&sefc=1&txp=5532434&n=kIrzFfciu3xoQw&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cgcr%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AHlkHjAwRgIhALoabq--tJdA241oAjCVj1I8JdVYeIYDMZn4d1U4-WwfAiEAoIUCLa5pIcwYXBSjLcFTz1KCz-JXwpRo2UTyw6DNPNI%3D&sig=AJfQdSswRgIhANklPn8Ndp7tDOxR3w8Z8CzE2pjGmEB_kzntXnj-IHLGAiEAvgPox7Agx-xJWl9DqYmOJ5js1kzr6y-hHHAQACzopXM%3D"
command = [
    'ffmpeg',
    '-reconnect', '1',
    '-reconnect_streamed', '1',
    '-reconnect_delay_max', '5',
    '-i', url,
    '-f', 'mp3',
    '-'
]

process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
#print("STDOUT:", stdout.decode('ISO-8859-1'))
print("STDERR:", stderr.decode('ISO-8859-1'))



