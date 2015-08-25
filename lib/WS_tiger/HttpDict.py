#!/usr/bin/python

###########################
#
# tiger 1.0 HttpDict
# (C) 2014 WatsonSoft
# made by JamesWatson
#
###########################

from interface.HttpApplication import *

class HttpLang(object):
	def __init__(self):
		self.State = dict()
		self.State["100"] = "Continue"
		self.State["101"] = "Switching Protocols"
		self.State["102"] = "Processing"
		self.State["200"] = "OK"
		self.State["201"] = "Created"
		self.State["202"] = "Accepted"
		self.State["203"] = "Non-Authoritative Information"
		self.State["204"] = "No Content"
		self.State["205"] = "Reset Content"
		self.State["206"] = "Partial Content"
		self.State["207"] = "Multi-Status"
		self.State["300"] = "Multiple Choices"
		self.State["301"] = "Moved Permanently"
		self.State["302"] = "Found"
		self.State["303"] = "See Other"
		self.State["304"] = "Not Modified"
		self.State["305"] = "Use Proxy"
		self.State["306"] = "Switch Proxy"
		self.State["307"] = "Temporary Redirect"
		self.State["400"] = "Bad Request"
		self.State["401"] = "Unauthorized"
		self.State["402"] = "Payment Required"
		self.State["403"] = "Forbidden"
		self.State["404"] = "Not Found"
		self.State["405"] = "Method Not Allowed"
		self.State["406"] = "Not Acceptable"
		self.State["408"] = "Request Timeout"
		self.State["409"] = "Conflict"
		self.State["410"] = "Gone"
		self.State["411"] = "Length Required"
		self.State["412"] = "Precondition Failed"
		self.State["414"] = "Request-URI Too Long"
		self.State["417"] = "Expectation Failed"
		self.State["422"] = "Unprocessable Entity"
		self.State["423"] = "Locked"
		self.State["424"] = "Failed Dependency"
		self.State["425"] = "Unordered Collection"
		self.State["426"] = "Upgrade Required"
		self.State["449"] = "Retry With"
		self.State["500"] = "Internal Server Error"
		self.State["501"] = "Not Implemented"
		self.State["502"] = "Bad Gateway"
		self.State["503"] = "Service Unavailable"
		self.State["504"] = "Gateway Timeout"
		self.State["507"] = "Insufficient Storage"
		self.State["508"] = "Loop Detected"
		self.State["510"] = "Not Extended"

		self.Mime = dict()
		self.Mime[".323"]   = "text/h323"
		self.Mime[".3gp"]   = "video/3gpp"
		self.Mime[".aab"]   = "application/x-authoware-bin"
		self.Mime[".aam"]   = "application/x-authoware-map"
		self.Mime[".aas"]   = "application/x-authoware-seg"
		self.Mime[".acx"]   = "application/internet-property-stream"
		self.Mime[".ai"]    = "application/postscript"
		self.Mime[".aif"]   = "audio/x-aiff"
		self.Mime[".aifc"]  = "audio/x-aiff"
		self.Mime[".aiff"]  = "audio/x-aiff"
		self.Mime[".als"]   = "audio/X-Alpha5"
		self.Mime[".amc"]   = "application/x-mpeg"
		self.Mime[".ani"]   = "application/octet-stream"
		self.Mime[".apk"]   = "application/vnd.android.package-archive"
		self.Mime[".asc"]   = "text/plain"
		self.Mime[".asd"]   = "application/astound"
		self.Mime[".asf"]   = "video/x-ms-asf"
		self.Mime[".asn"]   = "application/astound"
		self.Mime[".asp"]   = "application/x-asap"
		self.Mime[".asr"]   = "video/x-ms-asf"
		self.Mime[".asx"]   = "video/x-ms-asf"
		self.Mime[".au"]    = "audio/basic"
		self.Mime[".avb"]   = "application/octet-stream"
		self.Mime[".avi"]   = "video/x-msvideo"
		self.Mime[".awb"]   = "audio/amr-wb"
		self.Mime[".axs"]   = "application/olescript"
		self.Mime[".bas"]   = "text/plain"
		self.Mime[".bcpio"] = "application/x-bcpio"
		self.Mime[".bin"]  = "application/octet-stream"
		self.Mime[".bld"]   = "application/bld"
		self.Mime[".bld2"]  = "application/bld2"
		self.Mime[".bmp"]   = "image/bmp"
		self.Mime[".bpk"]   = "application/octet-stream"
		self.Mime[".bz2"]   = "application/x-bzip2"
		self.Mime[".c"]     = "text/plain"
		self.Mime[".cal"]   = "image/x-cals"
		self.Mime[".cat"]   = "application/vnd.ms-pkiseccat"
		self.Mime[".ccn"]   = "application/x-cnc"
		self.Mime[".cco"]   = "application/x-cocoa"
		self.Mime[".cdf"]   = "application/x-cdf"
		self.Mime[".cer"]   = "application/x-x509-ca-cert"
		self.Mime[".cgi"]   = "magnus-internal/cgi"
		self.Mime[".chat"]  = "application/x-chat"
		self.Mime[".class"] = "application/octet-stream"
		self.Mime[".clp"]   = "application/x-msclip"
		self.Mime[".cmx"]   = "image/x-cmx"
		self.Mime[".co"]    = "application/x-cult3d-object"
		self.Mime[".cod"]   = "image/cis-cod"
		self.Mime[".conf"]  = "text/plain"
		self.Mime[".cpio"]  = "application/x-cpio"
		self.Mime[".cpp"]   = "text/plain"
		self.Mime[".cpt"]   = "application/mac-compactpro"
		self.Mime[".crd"]   = "application/x-mscardfile"
		self.Mime[".crl"]   = "application/pkix-crl"
		self.Mime[".crt"]   = "application/x-x509-ca-cert"
		self.Mime[".csh"]   = "application/x-csh"
		self.Mime[".csm"]   = "chemical/x-csml"
		self.Mime[".csml"]  = "chemical/x-csml"
		self.Mime[".css"]   = "text/css"
		self.Mime[".cur"]   = "application/octet-stream"
		self.Mime[".dcm"]   = "x-lml/x-evm"
		self.Mime[".dcr"]   = "application/x-director"
		self.Mime[".dcx"]   = "image/x-dcx"
		self.Mime[".der"]   = "application/x-x509-ca-cert"
		self.Mime[".dhtml"] = "text/html"
		self.Mime[".dir"]   = "application/x-director"
		self.Mime[".dll"]   = "application/x-msdownload"
		self.Mime[".dmg"]   = "application/octet-stream"
		self.Mime[".dms"] = "application/octet-stream"
		self.Mime[".doc"] = "application/msword"
		self.Mime[".docx"] = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
		self.Mime[".dot"] = "application/msword"
		self.Mime[".dvi"] = "application/x-dvi"
		self.Mime[".dwf"] = "drawing/x-dwf"
		self.Mime[".dwg"] = "application/x-autocad"
		self.Mime[".dxf"] = "application/x-autocad"
		self.Mime[".dxr"] = "application/x-director"
		self.Mime[".ebk"] = "application/x-expandedbook"
		self.Mime[".emb"] = "chemical/x-embl-dl-nucleotide"
		self.Mime[".embl"] = "chemical/x-embl-dl-nucleotide"
		self.Mime[".eps"] = "application/postscript"
		self.Mime[".epub"] = "application/epub+zip"
		self.Mime[".eri"] = "image/x-eri"
		self.Mime[".es"] = "audio/echospeech"
		self.Mime[".esl"] = "audio/echospeech"
		self.Mime[".etc"] = "application/x-earthtime"
		self.Mime[".etx"] = "text/x-setext"
		self.Mime[".evm"] = "x-lml/x-evm"
		self.Mime[".evy"] = "application/envoy"
		self.Mime[".exe"] = "application/octet-stream"
		self.Mime[".fh4"] = "image/x-freehand"
		self.Mime[".fh5"] = "image/x-freehand"
		self.Mime[".fhc"] = "image/x-freehand"
		self.Mime[".fif"] = "application/fractals"
		self.Mime[".flr"] = "x-world/x-vrml"
		self.Mime[".flv"] = "flv-application/octet-stream"
		self.Mime[".fm"] = "application/x-maker"
		self.Mime[".fpx"] = "image/x-fpx"
		self.Mime[".fvi"] = "video/isivideo"
		self.Mime[".gau"] = "chemical/x-gaussian-input"
		self.Mime[".gca"] = "application/x-gca-compressed"
		self.Mime[".gdb"] = "x-lml/x-gdb"
		self.Mime[".gif"] = "image/gif"
		self.Mime[".gps"] = "application/x-gps"
		self.Mime[".gtar"] = "application/x-gtar"
		self.Mime[".gz"] = "application/x-gzip"
		self.Mime[".h"] = "text/plain"
		self.Mime[".hdf"] = "application/x-hdf"
		self.Mime[".hdm"] = "text/x-hdml"
		self.Mime[".hdml"] = "text/x-hdml"
		self.Mime[".hlp"] = "application/winhlp"
		self.Mime[".hqx"] = "application/mac-binhex40"
		self.Mime[".hta"] = "application/hta"
		self.Mime[".htc"] = "text/x-component"
		self.Mime[".htm"] = "text/html"
		self.Mime[".html"] = "text/html"
		self.Mime[".hts"] = "text/html"
		self.Mime[".htt"] = "text/webviewhtml"
		self.Mime[".ice"] = "x-conference/x-cooltalk"
		self.Mime[".ico"] = "image/x-icon"
		self.Mime[".ief"] = "image/ief"
		self.Mime[".ifm"] = "image/gif"
		self.Mime[".ifs"] = "image/ifs"
		self.Mime[".iii"] = "application/x-iphone"
		self.Mime[".imy"] = "audio/melody"
		self.Mime[".ins"] = "application/x-internet-signup"
		self.Mime[".ips"] = "application/x-ipscript"
		self.Mime[".ipx"] = "application/x-ipix"
		self.Mime[".isp"] = "application/x-internet-signup"
		self.Mime[".it"] = "audio/x-mod"
		self.Mime[".itz"] = "audio/x-mod"
		self.Mime[".ivr"] = "i-world/i-vrml"
		self.Mime[".j2k"] = "image/j2k"
		self.Mime[".jad"] = "text/vnd.sun.j2me.app-descriptor"
		self.Mime[".jam"] = "application/x-jam"
		self.Mime[".jar"] = "application/java-archive"
		self.Mime[".java"] = "text/plain"
		self.Mime[".jfif"] = "image/pipeg"
		self.Mime[".jnlp"] = "application/x-java-jnlp-file"
		self.Mime[".jpe"] = "image/jpeg"
		self.Mime[".jpeg"] = "image/jpeg"
		self.Mime[".jpg"] = "image/jpeg"
		self.Mime[".jpz"] = "image/jpeg"
		self.Mime[".js"] = "application/x-javascript"
		self.Mime[".jwc"] = "application/jwc"
		self.Mime[".kjx"] = "application/x-kjx"
		self.Mime[".lak"] = "x-lml/x-lak"
		self.Mime[".latex"] = "application/x-latex"
		self.Mime[".lcc"] = "application/fastman"
		self.Mime[".lcl"] = "application/x-digitalloca"
		self.Mime[".lcr"] = "application/x-digitalloca"
		self.Mime[".lgh"] = "application/lgh"
		self.Mime[".lha"] = "application/octet-stream"
		self.Mime[".lml"] = "x-lml/x-lml"
		self.Mime[".lmlpack"] = "x-lml/x-lmlpack"
		self.Mime[".log"] = "text/plain"
		self.Mime[".lsf"] = "video/x-la-asf"
		self.Mime[".lsx"] = "video/x-la-asf"
		self.Mime[".lzh"] = "application/octet-stream"
		self.Mime[".m13"] = "application/x-msmediaview"
		self.Mime[".m14"] = "application/x-msmediaview"
		self.Mime[".m15"] = "audio/x-mod"
		self.Mime[".m3u"] = "audio/x-mpegurl"
		self.Mime[".m3url"] = "audio/x-mpegurl"
		self.Mime[".m4a"] = "audio/mp4a-latm"
		self.Mime[".m4b"] = "audio/mp4a-latm"
		self.Mime[".m4p"] = "audio/mp4a-latm"
		self.Mime[".m4u"] = "video/vnd.mpegurl"
		self.Mime[".m4v"] = "video/x-m4v"
		self.Mime[".ma1"] = "audio/ma1"
		self.Mime[".ma2"] = "audio/ma2"
		self.Mime[".ma3"] = "audio/ma3"
		self.Mime[".ma5"] = "audio/ma5"
		self.Mime[".man"] = "application/x-troff-man"
		self.Mime[".map"] = "magnus-internal/imagemap"
		self.Mime[".mbd"] = "application/mbedlet"
		self.Mime[".mct"] = "application/x-mascot"
		self.Mime[".mdb"] = "application/x-msaccess"
		self.Mime[".mdz"] = "audio/x-mod"
		self.Mime[".me"] = "application/x-troff-me"
		self.Mime[".mel"] = "text/x-vmel"
		self.Mime[".mht"] = "message/rfc822"
		self.Mime[".mhtml"] = "message/rfc822"
		self.Mime[".mi"] = "application/x-mif"
		self.Mime[".mid"] = "audio/mid"
		self.Mime[".midi"] = "audio/midi"
		self.Mime[".mif"] = "application/x-mif"
		self.Mime[".mil"] = "image/x-cals"
		self.Mime[".mio"] = "audio/x-mio"
		self.Mime[".mmf"] = "application/x-skt-lbs"
		self.Mime[".mng"] = "video/x-mng"
		self.Mime[".mny"] = "application/x-msmoney"
		self.Mime[".moc"] = "application/x-mocha"
		self.Mime[".mocha"] = "application/x-mocha"
		self.Mime[".mod"] = "audio/x-mod"
		self.Mime[".mof"] = "application/x-yumekara"
		self.Mime[".mol"] = "chemical/x-mdl-molfile"
		self.Mime[".mop"] = "chemical/x-mopac-input"
		self.Mime[".mov"] = "video/quicktime"
		self.Mime[".movie"] = "video/x-sgi-movie"
		self.Mime[".mp2"] = "video/mpeg"
		self.Mime[".mp3"] = "audio/mpeg"
		self.Mime[".mp4"] = "video/mp4"
		self.Mime[".mpa"] = "video/mpeg"
		self.Mime[".mpc"] = "application/vnd.mpohun.certificate"
		self.Mime[".mpe"] = "video/mpeg"
		self.Mime[".mpeg"] = "video/mpeg"
		self.Mime[".mpg"] = "video/mpeg"
		self.Mime[".mpg4"] = "video/mp4"
		self.Mime[".mpga"] = "audio/mpeg"
		self.Mime[".mpn"] = "application/vnd.mophun.application"
		self.Mime[".mpp"] = "application/vnd.ms-project"
		self.Mime[".mps"] = "application/x-mapserver"
		self.Mime[".mpv2"] = "video/mpeg"
		self.Mime[".mrl"] = "text/x-mrml"
		self.Mime[".mrm"] = "application/x-mrm"
		self.Mime[".ms"] = "application/x-troff-ms"
		self.Mime[".msg"] = "application/vnd.ms-outlook"
		self.Mime[".mts"] = "application/metastream"
		self.Mime[".mtx"] = "application/metastream"
		self.Mime[".mtz"] = "application/metastream"
		self.Mime[".mvb"] = "application/x-msmediaview"
		self.Mime[".mzv"] = "application/metastream"
		self.Mime[".nar"] = "application/zip"
		self.Mime[".nbmp"] = "image/nbmp"
		self.Mime[".nc"] = "application/x-netcdf"
		self.Mime[".ndb"] = "x-lml/x-ndb"
		self.Mime[".ndwn"] = "application/ndwn"
		self.Mime[".nif"] = "application/x-nif"
		self.Mime[".nmz"] = "application/x-scream"
		self.Mime[".nokia-op-logo"] = "image/vnd.nok-oplogo-color"
		self.Mime[".npx"] = "application/x-netfpx"
		self.Mime[".nsnd"] = "audio/nsnd"
		self.Mime[".nva"] = "application/x-neva1"
		self.Mime[".nws"] = "message/rfc822"
		self.Mime[".oda"] = "application/oda"
		self.Mime[".ogg"] = "audio/ogg"
		self.Mime[".oom"] = "application/x-AtlasMate-Plugin"
		self.Mime[".p10"] = "application/pkcs10"
		self.Mime[".p12"] = "application/x-pkcs12"
		self.Mime[".p7b"] = "application/x-pkcs7-certificates"
		self.Mime[".p7c"] = "application/x-pkcs7-mime"
		self.Mime[".p7m"] = "application/x-pkcs7-mime"
		self.Mime[".p7r"] = "application/x-pkcs7-certreqresp"
		self.Mime[".p7s"] = "application/x-pkcs7-signature"
		self.Mime[".pac"] = "audio/x-pac"
		self.Mime[".pae"] = "audio/x-epac"
		self.Mime[".pan"] = "application/x-pan"
		self.Mime[".pbm"] = "image/x-portable-bitmap"
		self.Mime[".pcx"] = "image/x-pcx"
		self.Mime[".pda"] = "image/x-pda"
		self.Mime[".pdb"] = "chemical/x-pdb"
		self.Mime[".pdf"] = "application/pdf"
		self.Mime[".pfr"] = "application/font-tdpfr"
		self.Mime[".pfx"] = "application/x-pkcs12"
		self.Mime[".pgm"] = "image/x-portable-graymap"
		self.Mime[".pict"] = "image/x-pict"
		self.Mime[".pko"] = "application/ynd.ms-pkipko"
		self.Mime[".pm"] = "application/x-perl"
		self.Mime[".pma"] = "application/x-perfmon"
		self.Mime[".pmc"] = "application/x-perfmon"
		self.Mime[".pmd"] = "application/x-pmd"
		self.Mime[".pml"] = "application/x-perfmon"
		self.Mime[".pmr"] = "application/x-perfmon"
		self.Mime[".pmw"] = "application/x-perfmon"
		self.Mime[".png"] = "image/png"
		self.Mime[".pnm"] = "image/x-portable-anymap"
		self.Mime[".pnz"] = "image/png"
		self.Mime[".pot,"] = "application/vnd.ms-powerpoint"
		self.Mime[".ppm"] = "image/x-portable-pixmap"
		self.Mime[".pps"] = "application/vnd.ms-powerpoint"
		self.Mime[".ppt"] = "application/vnd.ms-powerpoint"
		self.Mime[".pptx"] = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
		self.Mime[".pqf"] = "application/x-cprplayer"
		self.Mime[".pqi"] = "application/cprplayer"
		self.Mime[".prc"] = "application/x-prc"
		self.Mime[".prf"] = "application/pics-rules"
		self.Mime[".prop"] = "text/plain"
		self.Mime[".proxy"] = "application/x-ns-proxy-autoconfig"
		self.Mime[".ps"] = "application/postscript"
		self.Mime[".ptlk"] = "application/listenup"
		self.Mime[".pub"] = "application/x-mspublisher"
		self.Mime[".pvx"] = "video/x-pv-pvx"
		self.Mime[".qcp"] = "audio/vnd.qcelp"
		self.Mime[".qt"] = "video/quicktime"
		self.Mime[".qti"] = "image/x-quicktime"
		self.Mime[".qtif"] = "image/x-quicktime"
		self.Mime[".r3t"] = "text/vnd.rn-realtext3d"
		self.Mime[".ra"] = "audio/x-pn-realaudio"
		self.Mime[".ram"] = "audio/x-pn-realaudio"
		self.Mime[".rar"] = "application/octet-stream"
		self.Mime[".ras"] = "image/x-cmu-raster"
		self.Mime[".rc"] = "text/plain"
		self.Mime[".rdf"] = "application/rdf+xml"
		self.Mime[".rf"] = "image/vnd.rn-realflash"
		self.Mime[".rgb"] = "image/x-rgb"
		self.Mime[".rlf"] = "application/x-richlink"
		self.Mime[".rm"] = "audio/x-pn-realaudio"
		self.Mime[".rmf"] = "audio/x-rmf"
		self.Mime[".rmi"] = "audio/mid"
		self.Mime[".rmm"] = "audio/x-pn-realaudio"
		self.Mime[".rmvb"] = "audio/x-pn-realaudio"
		self.Mime[".rnx"] = "application/vnd.rn-realplayer"
		self.Mime[".roff"] = "application/x-troff"
		self.Mime[".rp"] = "image/vnd.rn-realpix"
		self.Mime[".rpm"] = "audio/x-pn-realaudio-plugin"
		self.Mime[".rt"] = "text/vnd.rn-realtext"
		self.Mime[".rte"] = "x-lml/x-gps"
		self.Mime[".rtf"] = "application/rtf"
		self.Mime[".rtg"] = "application/metastream"
		self.Mime[".rtx"] = "text/richtext"
		self.Mime[".rv"] = "video/vnd.rn-realvideo"
		self.Mime[".rwc"] = "application/x-rogerwilco"
		self.Mime[".s3m"] = "audio/x-mod"
		self.Mime[".s3z"] = "audio/x-mod"
		self.Mime[".sca"] = "application/x-supercard"
		self.Mime[".scd"] = "application/x-msschedule"
		self.Mime[".sct"] = "text/scriptlet"
		self.Mime[".sdf"] = "application/e-score"
		self.Mime[".sea"] = "application/x-stuffit"
		self.Mime[".setpay"] = "application/set-payment-initiation"
		self.Mime[".setreg"] = "application/set-registration-initiation"
		self.Mime[".sgm"] = "text/x-sgml"
		self.Mime[".sgml"] = "text/x-sgml"
		self.Mime[".sh"] = "application/x-sh"
		self.Mime[".shar"] = "application/x-shar"
		self.Mime[".shtml"] = "magnus-internal/parsed-html"
		self.Mime[".shw"] = "application/presentations"
		self.Mime[".si6"] = "image/si6"
		self.Mime[".si7"] = "image/vnd.stiwap.sis"
		self.Mime[".si9"] = "image/vnd.lgtwap.sis"
		self.Mime[".sis"] = "application/vnd.symbian.install"
		self.Mime[".sit"] = "application/x-stuffit"
		self.Mime[".skd"] = "application/x-Koan"
		self.Mime[".skm"] = "application/x-Koan"
		self.Mime[".skp"] = "application/x-Koan"
		self.Mime[".skt"] = "application/x-Koan"
		self.Mime[".slc"] = "application/x-salsa"
		self.Mime[".smd"] = "audio/x-smd"
		self.Mime[".smi"] = "application/smil"
		self.Mime[".smil"] = "application/smil"
		self.Mime[".smp"] = "application/studiom"
		self.Mime[".smz"] = "audio/x-smd"
		self.Mime[".snd"] = "audio/basic"
		self.Mime[".spc"] = "application/x-pkcs7-certificates"
		self.Mime[".spl"] = "application/futuresplash"
		self.Mime[".spr"] = "application/x-sprite"
		self.Mime[".sprite"] = "application/x-sprite"
		self.Mime[".sdp"] = "application/sdp"
		self.Mime[".spt"] = "application/x-spt"
		self.Mime[".src"] = "application/x-wais-source"
		self.Mime[".sst"] = "application/vnd.ms-pkicertstore"
		self.Mime[".stk"] = "application/hyperstudio"
		self.Mime[".stl"] = "application/vnd.ms-pkistl"
		self.Mime[".stm"] = "text/html"
		self.Mime[".svg"] = "image/svg+xml"
		self.Mime[".sv4cpio"] = "application/x-sv4cpio"
		self.Mime[".sv4crc"] = "application/x-sv4crc"
		self.Mime[".svf"] = "image/vnd"
		self.Mime[".svg"] = "image/svg+xml"
		self.Mime[".svh"] = "image/svh"
		self.Mime[".svr"] = "x-world/x-svr"
		self.Mime[".swf"] = "application/x-shockwave-flash"
		self.Mime[".swfl"] = "application/x-shockwave-flash"
		self.Mime[".t"] = "application/x-troff"
		self.Mime[".tad"] = "application/octet-stream"
		self.Mime[".talk"] = "text/x-speech"
		self.Mime[".tar"] = "application/x-tar"
		self.Mime[".taz"] = "application/x-tar"
		self.Mime[".tbp"] = "application/x-timbuktu"
		self.Mime[".tbt"] = "application/x-timbuktu"
		self.Mime[".tcl"] = "application/x-tcl"
		self.Mime[".tex"] = "application/x-tex"
		self.Mime[".texi"] = "application/x-texinfo"
		self.Mime[".texinfo"] = "application/x-texinfo"
		self.Mime[".tgz"] = "application/x-compressed"
		self.Mime[".thm"] = "application/vnd.eri.thm"
		self.Mime[".tif"] = "image/tiff"
		self.Mime[".tiff"] = "image/tiff"
		self.Mime[".tki"] = "application/x-tkined"
		self.Mime[".tkined"] = "application/x-tkined"
		self.Mime[".toc"] = "application/toc"
		self.Mime[".toy"] = "image/toy"
		self.Mime[".tr"] = "application/x-troff"
		self.Mime[".trk"] = "x-lml/x-gps"
		self.Mime[".trm"] = "application/x-msterminal"
		self.Mime[".tsi"] = "audio/tsplayer"
		self.Mime[".tsp"] = "application/dsptype"
		self.Mime[".tsv"] = "text/tab-separated-values"
		self.Mime[".ttf"] = "application/octet-stream"
		self.Mime[".ttz"] = "application/t-time"
		self.Mime[".txt"] = "text/plain"
		self.Mime[".uls"] = "text/iuls"
		self.Mime[".ult"] = "audio/x-mod"
		self.Mime[".ustar"] = "application/x-ustar"
		self.Mime[".uu"] = "application/x-uuencode"
		self.Mime[".uue"] = "application/x-uuencode"
		self.Mime[".vcd"] = "application/x-cdlink"
		self.Mime[".vcf"] = "text/x-vcard"
		self.Mime[".vdo"] = "video/vdo"
		self.Mime[".vib"] = "audio/vib"
		self.Mime[".viv"] = "video/vivo"
		self.Mime[".vivo"] = "video/vivo"
		self.Mime[".vmd"] = "application/vocaltec-media-desc"
		self.Mime[".vmf"] = "application/vocaltec-media-file"
		self.Mime[".vmi"] = "application/x-dreamcast-vms-info"
		self.Mime[".vms"] = "application/x-dreamcast-vms"
		self.Mime[".vox"] = "audio/voxware"
		self.Mime[".vqe"] = "audio/x-twinvq-plugin"
		self.Mime[".vqf"] = "audio/x-twinvq"
		self.Mime[".vql"] = "audio/x-twinvq"
		self.Mime[".vre"] = "x-world/x-vream"
		self.Mime[".vrml"] = "x-world/x-vrml"
		self.Mime[".vrt"] = "x-world/x-vrt"
		self.Mime[".vrw"] = "x-world/x-vream"
		self.Mime[".vts"] = "workbook/formulaone"
		self.Mime[".wav"] = "audio/x-wav"
		self.Mime[".wax"] = "audio/x-ms-wax"
		self.Mime[".wbmp"] = "image/vnd.wap.wbmp"
		self.Mime[".wcm"] = "application/vnd.ms-works"
		self.Mime[".wdb"] = "application/vnd.ms-works"
		self.Mime[".web"] = "application/vnd.xara"
		self.Mime[".wi"] = "image/wavelet"
		self.Mime[".wis"] = "application/x-InstallShield"
		self.Mime[".wks"] = "application/vnd.ms-works"
		self.Mime[".wm"] = "video/x-ms-wm"
		self.Mime[".wma"] = "audio/x-ms-wma"
		self.Mime[".wmd"] = "application/x-ms-wmd"
		self.Mime[".wmf"] = "application/x-msmetafile"
		self.Mime[".wml"] = "text/vnd.wap.wml"
		self.Mime[".wmlc"] = "application/vnd.wap.wmlc"
		self.Mime[".wmls"] = "text/vnd.wap.wmlscript"
		self.Mime[".wmlsc"] = "application/vnd.wap.wmlscriptc"
		self.Mime[".wmlscript"] = "text/vnd.wap.wmlscript"
		self.Mime[".wmv"] = "audio/x-ms-wmv"
		self.Mime[".wmx"] = "video/x-ms-wmx"
		self.Mime[".wmz"] = "application/x-ms-wmz"
		self.Mime[".wpng"] = "image/x-up-wpng"
		self.Mime[".wps"] = "application/vnd.ms-works"
		self.Mime[".wpt"] = "x-lml/x-gps"
		self.Mime[".wri"] = "application/x-mswrite"
		self.Mime[".wrl"] = "x-world/x-vrml"
		self.Mime[".wrz"] = "x-world/x-vrml"
		self.Mime[".ws"] = "text/vnd.wap.wmlscript"
		self.Mime[".wsc"] = "application/vnd.wap.wmlscriptc"
		self.Mime[".wv"] = "video/wavelet"
		self.Mime[".wvx"] = "video/x-ms-wvx"
		self.Mime[".wxl"] = "application/x-wxl"
		self.Mime[".x-gzip"] = "application/x-gzip"
		self.Mime[".xaf"] = "x-world/x-vrml"
		self.Mime[".xar"] = "application/vnd.xara"
		self.Mime[".xbm"] = "image/x-xbitmap"
		self.Mime[".xdm"] = "application/x-xdma"
		self.Mime[".xdma"] = "application/x-xdma"
		self.Mime[".xdw"] = "application/vnd.fujixerox.docuworks"
		self.Mime[".xht"] = "application/xhtml+xml"
		self.Mime[".xhtm"] = "application/xhtml+xml"
		self.Mime[".xhtml"] = "application/xhtml+xml"
		self.Mime[".xla"] = "application/vnd.ms-excel"
		self.Mime[".xlc"] = "application/vnd.ms-excel"
		self.Mime[".xll"] = "application/x-excel"
		self.Mime[".xlm"] = "application/vnd.ms-excel"
		self.Mime[".xls"] = "application/vnd.ms-excel"
		self.Mime[".xlsx"] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
		self.Mime[".xlt"] = "application/vnd.ms-excel"
		self.Mime[".xlw"] = "application/vnd.ms-excel"
		self.Mime[".xm"] = "audio/x-mod"
		self.Mime[".xml"] = "text/plain"
		self.Mime[".xmz"] = "audio/x-mod"
		self.Mime[".xof"] = "x-world/x-vrml"
		self.Mime[".xpi"] = "application/x-xpinstall"
		self.Mime[".xpm"] = "image/x-xpixmap"
		self.Mime[".xsit"] = "text/xml"
		self.Mime[".xsl"] = "text/xml"
		self.Mime[".xul"] = "text/xul"
		self.Mime[".xwd"] = "image/x-xwindowdump"
		self.Mime[".xyz"] = "chemical/x-pdb"
		self.Mime[".yz1"] = "application/x-yz1"
		self.Mime[".z"] = "application/x-compress"
		self.Mime[".zac"] = "application/x-zaurus-zac"
		self.Mime[".zip"] = "application/zip"
		self.Mime[".json"] = "application/json"

	def getMIME(self, name):
		try:
			return self.Mime[name]
		except KeyError:
			return "application/octet-stream"

	def getState(self, StateNum):
		try:
			return (StateNum, self.State[repr(StateNum)])
		except KeyError:
			return None

webLang = HttpLang()

application = HttpApplication()
application.setAttr('ServState', "normal")

cfg = dict()
cfg['shutTime'] = "10"
cfg['proPort'] = "80"
cfg['prosPort'] = "443"
cfg['ctrlPort'] = "8086"
cfg['ctrlAddr'] = "127.0.0.1"
cfg['webApp'] = "webApp"
cfg['ROOT'] = "ROOT"
cfg['index'] = "index.py_html"
cfg['WEB'] = "true"
cfg['SSL'] = "false"

def getInfoPage(num, message):
	return "<!DOCTYPE html>\r\n<html>\r\n<head>\r\n</head>\r\n<body>\r\n\t<h1>"+str(num)+"&nbsp;"+webLang.getState(num)[1]+"</h1>\r\n"+message+"\r\n</body>\r\n</html>\r\n\0"
