import json
import random
import string

def genR():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

topics_file = open("topics.json", "r")
topics = json.loads(topics_file.read())

final_index = open("tmpl/index_header.html", "r").read()

for i in topics["topics"]:
    print("Generating HTML for %s" % i)

    final_html = open("tmpl/topic_header.html", "r").read()

    topic_file = open("%s.json" % i, "r")
    topic = json.loads(topic_file.read())

    final_html += "<strong>Current topic: %s</strong><br /><br />" % i

    links = topic["links"]
    for j in links:
        if "notes" in j.keys():
            key = genR()
            final_html += "<a href=\"" + j["link"] + "\">"+j["title"] +"</a>"+\
                            "<a href=\"#"+str(key)+"\" "+\
                                "class=\"\" " +\
                                "data-toggle=\"collapse\"><sup>(Notes)</sup></a><br />"+\
                            "<div id=\""+str(key)+"\" class=\"collapse\">"+ \
                            j["notes"] +\
                            "</div>" 
        else:
            final_html += "<a href=\"%s\">%s</a> <br />" % (j["link"], j["title"])

    final_html += open("tmpl/topic_footer.html").read()
    open("_site/%s.html" % i, "w+").write(final_html)

    final_index += "<a href=\"%s.html\">%s</a><br />" % (i, i)

final_index += open("tmpl/index_footer.html", "r").read()
open("_site/index.html", "w+").write(final_index)
