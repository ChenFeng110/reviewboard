from reviewboard.scmtools.core import SCMClient, SCMTool, HEAD, PRE_CREATION
                                repository.encoding, local_site_name)
    def parse_diff_revision(self, file_str, revision_str, moved=False,
                            *args, **kwargs):
        elif revision != PRE_CREATION and not moved and revision != '':
            # Moved files with no changes has no revision,
            # so don't validate those.
        # Parse the extended header to save the new file, deleted file,
        # mode change, file move, and index.
        elif self._is_moved_file(linenum):
            file_info.data += self.lines[linenum] + "\n"
            file_info.data += self.lines[linenum + 1] + "\n"
            file_info.data += self.lines[linenum + 2] + "\n"
            linenum += 3
            file_info.moved = True
    def _is_moved_file(self, linenum):
        return (self.lines[linenum].startswith("similarity index") and
                self.lines[linenum + 1].startswith("rename from") and
                self.lines[linenum + 2].startswith("rename to"))

class GitClient(SCMClient):
                 encoding='', local_site_name=None):
        super(GitClient, self).__init__(self._normalize_git_url(path),
                                        username=username,
                                        password=password)

        self.encoding = encoding
            return self.get_file_http(self._build_raw_url(path, revision),
                                      path, revision)
                self.get_file(path, revision)
            except Exception:
                return False