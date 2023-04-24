import os
from shellextools.getmultifiles import get_all_selected_files
import sys

if len(sys.argv) > 1:
    allmyfiles = get_all_selected_files(sleeptime=4)

from hackyargparser import add_sysargv
from tkinter import *
import pandas as pd
from pandastable import Table
from shellextools import (
    format_folder_drive_path_backslash,
    get_monitors_resolution,
    add_multicommands_files,
)
import lxml  # not needed here - to make sure that nutika includes the dependency
from a_pandas_ex_text_compare import get_text_difference


class TestApp(Frame):
    def __init__(self, df, parent=None):
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        self.resolution = get_monitors_resolution()[0]
        self.monitor_w = self.resolution["width"]
        self.monitor_h = self.resolution["height"]
        self.main.geometry(f"{self.monitor_w - 100}x{self.monitor_h - 100}")
        self.main.title("Results")
        f = Frame(self.main)
        f.pack(fill=BOTH, expand=1)
        self.table = pt = Table(
            f, dataframe=df.copy(), showtoolbar=True, showstatusbar=True
        )
        self.table.autoResizeColumns()
        pt.show()


@add_sysargv
def main(path: str = "", action: str = ""):
    df = pd.DataFrame(
        columns=[
            "no",
            "aa_text",
            "bb_text",
            "aa_added",
            "bb_substracted",
            "aa_changed",
            "bb_changed",
            "aa_diff",
            "bb_diff",
            "aa_parts",
            "bb_parts",
        ]
    )

    lst = [x[x.index("--path") + 1] for x in allmyfiles]
    lst = [format_folder_drive_path_backslash(pa) for pa in lst]
    lst = list(set(lst))
    try:
        df = get_text_difference(lst[0], lst[1], encoding="utf-8")
    except Exception as fe:
        pass

    app = TestApp(df)
    return app


if __name__ == "__main__":
    if len(sys.argv) == 1:
        supported_extensions = list(
            {
                ".email",
                ".rss",
                ".msg",
                ".utf8" ".conf",
                ".js",
                ".xslt",
                ".dok",
                ".txt",
                ".rtx",
                ".java",
                ".vcf",
                ".extra",
                ".xsl",
                ".rtf",
                ".markdown",
                ".log",
                ".tsv",
                ".crash",
                ".reg",
                ".nfo",
                ".md",
                ".sha1",
                ".en",
                ".bat",
                ".full",
                ".xhtml",
                ".c",
                ".nt",
                ".desc",
                ".ini",
                ".csv",
                ".mkd",
                ".gnu",
                ".json",
                ".xsd",
                ".sha512",
                ".html",
                ".htm",
                ".lisp",
                ".readme",
                ".rml",
                ".fpt",
                ".xml",
                ".php",
                ".sbv",
                ".mtx",
                ".curl",
                ".cmd",
                ".html5",
                ".lxfml",
                ".sub",
                ".cs",
                ".srt",
                ".chord",
                ".yml",
                ".h",
                ".wer",
                ".ocr",
                ".vb",
                ".ger",
                ".spec",
                ".css",
                ".cfg",
                ".cpp",
                ".us",
                ".py",
                ".xlog",
                ".sh",
                ".err",
                ".lst",
                ".reg",
            }
        )
        futurnameofcompiledexe = "textcompare.exe"
        multicommands = [
            {
                "mainmenuitem": "TextCompare",
                "submenu": "Compare 2 files",
                "folderinprogramdata": "RCTools",
                "filetypes": supported_extensions,  # typical file extensions with text content
                "additional_arguments": "--action comparetext",  # not really necessary yet since there is only one function
            }
        ]
        add_multicommands_files(multicommands, futurnameofcompiledexe)

    else:
        try:
            app = main()

            app.mainloop()

            try:
                sys.exit(0)

            finally:
                os._exit(0)

        except Exception as fe:
            print(fe)

            try:
                sys.exit(1)

            finally:
                os._exit(1)
