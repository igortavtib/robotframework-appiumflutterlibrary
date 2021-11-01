# -*- coding: utf-8 -*-

from AppiumFlutterLibrary.keywords.keywordgroup import KeywordGroup


class _RunOnFailureKeyWords(KeywordGroup):
    def __init__(self):
        self._run_on_failure_keyword = None
        self._running_on_failure_routine = None
    
    def register_keyword_to_run_on_failure(self, keyword):
        old_keyword = self._run_on_failure_keyword
        old_keyword_text = old_keyword if old_keyword is not None else "Nothing"

        new_keyword = keyword if keyword.strip().lower() != "nothing" else "Nothing"
        new_keyword_text = new_keyword if new_keyword is not None else "Nothing"

        self._run_on_failure_keyword = new_keyword

        return old_keyword