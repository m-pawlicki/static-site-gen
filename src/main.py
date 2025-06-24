from static import *
import sys

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
        outdir = "docs"
        if not basepath.endswith("/"):
            raise Exception("Please make sure your base path ends with a /")
    else:
        basepath = "/"
        outdir = "public"

    copy_static("static", outdir)
    generate_pages_recursive("content", "template.html", outdir, basepath)

if __name__ == "__main__":
    main()