import templates
import util
from database_countries import code_to_country
from database_2020 import database

def run():
    print("Creating timeline/2020")
    util.makedirs("../timeline/2020")
    html = templates.get("timeline/2020/index")
    html = templates.initial_replace(html, 1)

    medal_to_template = {
        "G": templates.get("timeline/year/individual_gold"),
        "S": templates.get("timeline/year/individual_silver"),
        "B": templates.get("timeline/year/individual_bronze"),
        "H": templates.get("timeline/year/individual_honourable"),
        "P": "",
    }

    tablehtml = ""
    for row in database:
        rowhtml = templates.get("timeline/year/individual_row")
        rowhtml = rowhtml.replace("__CODE__", row.code)
        rowhtml = rowhtml.replace("__COUNTRY__", code_to_country[row.code])
        if row.website:
            link = templates.get("timeline/year/individual_student_link")
            link = link.replace("__LINK__", row.website)
            link = link.replace("__NAME__", row.name)
            rowhtml = rowhtml.replace("__NAME__", link)
        else:
            rowhtml = rowhtml.replace("__NAME__", row.name)
        rowhtml = rowhtml.replace("__RANK__", row.rank)
        rowhtml = rowhtml.replace("__MEDAL__", medal_to_template[row.medal])
        rowhtml = rowhtml.replace("__POINTS_STYLE__", "display: none;")
        tablehtml += rowhtml
    html = html.replace("__TABLE__", tablehtml)

    html = templates.final_replace(html, "../..")
    util.writefile("../timeline/2020/index.html", html)

if __name__ == "__main__":
    run()
