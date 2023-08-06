"""Cell conversion methods.

Convert/read notebook cells to/from python, R and Rmd cells
"""

import re
from nbformat.v4.nbbase import new_code_cell, new_raw_cell, new_markdown_cell
from .languages import cell_language, is_code
from .cell_metadata import metadata_to_rmd_options, rmd_options_to_metadata, \
    json_options_to_metadata, metadata_to_json_options


def code_to_rmd(source, metadata, default_language):
    """
    Represent a code cell with given source and metadata as a rmd cell
    :param source:
    :param metadata:
    :param default_language:
    :return:
    """
    lines = []
    language = cell_language(source) or default_language
    if 'Rmd' not in re.split('\\.|,', metadata.get('active', 'Rmd')):
        metadata['eval'] = False
    options = metadata_to_rmd_options(language, metadata)
    lines.append(u'```{{{}}}'.format(options))
    lines.extend(source)
    lines.append(u'```')
    return lines


def code_to_text(self,
                 source,
                 metadata,
                 default_language,
                 next_cell_is_code):
    """
    Represent a code cell with given source and metadata as text
    :param self:
    :param source:
    :param metadata:
    :param default_language:
    :param next_cell_is_code:
    :return:
    """
    if self.ext == '.Rmd':
        return code_to_rmd(source, metadata, default_language)
    else:
        lines = []
        language = cell_language(source) or default_language
        if language == default_language:
            if self.ext == '.R':
                options = metadata_to_rmd_options(language, metadata)[2:]
                if options != '':
                    lines.append('#+ ' + options)
            else:
                options = metadata_to_json_options(metadata)
                if options != '{}':
                    lines.append('# + ' + options)
            lines.extend(source)
        else:
            lines.extend(self.markdown_escape(
                code_to_rmd(source, metadata, default_language)))

        # Two blank lines before next code cell
        if next_cell_is_code:
            lines.append('')

        return lines


def cell_to_text(self,
                 cell,
                 next_cell=None,
                 default_language='python'):
    """
    Represent a notebook cell as a text cell, in either
    py, R or rmd format
    :param self: TextNotebookWriter object
    :param cell: current cell
    :param next_cell: next cell
    :param default_language: default language for the current notebook
    :return:
    """
    source = cell.get('source').splitlines()
    metadata = cell.get('metadata', {})
    skipline = True
    if 'noskipline' in metadata:
        skipline = not metadata['noskipline']
        del metadata['noskipline']

    lines = []
    if is_code(cell):
        lines.extend(code_to_text(self, source, metadata, default_language,
                                  next_cell and is_code(next_cell)))
    else:
        if source == []:
            source = ['']
        lines.extend(self.markdown_escape(source))

        # Two blank lines between consecutive markdown cells in Rmd
        if self.ext == '.Rmd' and next_cell \
                and next_cell.cell_type == 'markdown':
            lines.append('')

    if skipline and next_cell:
        lines.append('')

    return lines


_START_CODE_RMD = re.compile(r"^```\{(.*)\}\s*$")
_END_CODE_MD = re.compile(r"^```\s*$")
_CODE_OPTION_RPY = re.compile(r"^(#|# )\+(.*)$")
_BLANK_LINE = re.compile(r"^\s*$")


def start_code_rmd(line):
    """
    Line indicates that a code cell starts, in a rmd file
    :param line:
    :return:
    """
    return _START_CODE_RMD.match(line)


def start_code_rpy(line):
    """
    A code cell starts here, in a py or R file
    :param line:
    :return:
    """
    return _CODE_OPTION_RPY.match(line)


def next_uncommented_is_code(lines):
    """
    Next non-commented line is code
    :param lines:
    :return:
    """
    for line in lines:
        if line.startswith('#'):
            continue
        return not _BLANK_LINE.match(line)

    return False


def text_to_cell(self, lines):
    """
    Parse text to a cell
    :param self:
    :param lines:
    :return: cell, cursor
    """
    if self.start_code(lines[0]):
        return self.code_to_cell(lines, parse_opt=True)
    elif self.prefix != '' and not lines[0].startswith(self.prefix):
        return self.code_to_cell(lines, parse_opt=False)
    elif self.ext == '.py' and next_uncommented_is_code(lines):
        return self.code_to_cell(lines, parse_opt=False)

    return self.markdown_to_cell(lines)


def parse_code_options(line, ext):
    """
    Parse code options on the given line
    :param line:
    :param ext:
    :return:
    """
    if ext == '.Rmd':
        return rmd_options_to_metadata(_START_CODE_RMD.findall(line)[0])
    elif ext == '.R':
        return rmd_options_to_metadata(_CODE_OPTION_RPY.match(line).group(2))

    return 'python', json_options_to_metadata(
        _CODE_OPTION_RPY.match(line).group(2))


def next_code_is_indented(lines):
    """
    Is next code line indented?
    :param lines:
    :return:
    """
    for line in lines:
        if line.startswith('#'):
            continue
        if _BLANK_LINE.match(line):
            continue
        return line.startswith(' ')

    return False


def no_code_before_next_blank_line(lines):
    """
    Do we find code before next blank line?
    :param lines:
    :return:
    """
    for line in lines:
        if line.startswith('#'):
            continue
        return _BLANK_LINE.match(line)

    return True


def code_or_raw_cell(source, metadata):
    if 'ipynb' not in re.split('\\.|,', metadata.get('active', 'ipynb')):
        return new_raw_cell(source=source, metadata=metadata)
    return new_code_cell(source=source, metadata=metadata)


def code_to_cell(self, lines, parse_opt):
    """
    Parse code to a notebook cell
    :param self:
    :param lines:
    :param parse_opt:
    :return: cell, cursor
    """
    # Parse options
    if parse_opt:
        language, metadata = parse_code_options(lines[0], self.ext)
        if self.ext == '.Rmd':
            metadata['language'] = language
    else:
        metadata = {}

    # Find end of cell and return
    if self.ext == '.Rmd':
        for pos, line in enumerate(lines):
            if pos > 0 and _END_CODE_MD.match(line):
                next_line_blank = pos + 1 == len(lines) or \
                                  _BLANK_LINE.match(lines[pos + 1])
                if next_line_blank and pos + 2 != len(lines):
                    return code_or_raw_cell(
                        source='\n'.join(lines[1:pos]), metadata=metadata), \
                           pos + 2
                cell = code_or_raw_cell(
                    source='\n'.join(lines[1:pos]),
                    metadata=metadata)
                cell.metadata['noskipline'] = True
                return cell, pos + 1
    else:
        prev_blank = False
        triple = None
        for pos, line in enumerate(lines):
            if parse_opt and pos == 0:
                continue

            if self.ext == '.R' and line.startswith(self.prefix):
                if prev_blank:
                    return code_or_raw_cell(
                        source='\n'.join(lines[parse_opt:(pos - 1)]),
                        metadata=metadata), pos
                cell = code_or_raw_cell(
                    source='\n'.join(lines[parse_opt:pos]),
                    metadata=metadata)
                cell.metadata['noskipline'] = True
                return cell, pos

            if self.ext == '.py':
                single = None
                for i, char in enumerate(line):
                    if char not in ['"', "'"]:
                        continue

                    if single == char:
                        single = None
                        continue
                    if single is not None:
                        continue
                    if triple == char:
                        if line[i - 2:i + 1] == 3 * char:
                            triple = None
                            continue
                    if triple is not None:
                        continue
                    if line[i - 2:i + 1] == 3 * char:
                        triple = char

                if triple:
                    continue

            if prev_blank:
                if _BLANK_LINE.match(line):
                    # Two blank lines => end of cell
                    # (unless next code is indented)
                    # Two blank lines at the end == empty code cell

                    if self.ext == '.py':
                        if next_code_is_indented(lines[pos:]):
                            continue

                    return code_or_raw_cell(
                        source='\n'.join(lines[parse_opt:(pos - 1)]),
                        metadata=metadata), min(pos + 1,
                                                len(lines) - 1)

                # are all the lines from here to next blank
                # escaped with the prefix?
                if self.ext == '.py':
                    if no_code_before_next_blank_line(lines[pos:]):
                        return code_or_raw_cell(
                            source='\n'.join(lines[parse_opt:(pos - 1)]),
                            metadata=metadata), pos

            prev_blank = _BLANK_LINE.match(line)

    # Unterminated cell?
    return code_or_raw_cell(
        source='\n'.join(lines[parse_opt:]),
        metadata=metadata), len(lines)


def markdown_to_cell(self, lines):
    """
    Parse text and return a markdown cell
    :param self:
    :param lines:
    :return: cell, cursor
    """
    markdown = []
    for pos, line in enumerate(lines):
        # Markdown stops with the end of comments
        if line.startswith(self.prefix):
            markdown.append(self.markdown_unescape(line))
        elif _BLANK_LINE.match(line):
            return new_markdown_cell(source='\n'.join(markdown)), pos + 1
        else:
            cell = new_markdown_cell(source='\n'.join(markdown))
            cell.metadata['noskipline'] = True
            return cell, pos

    # still here => unterminated markdown
    return new_markdown_cell(source='\n'.join(markdown)), len(lines)


def markdown_to_cell_rmd(lines):
    """
    Parse text, in case of a rmd file, and return a markdown cell
    :param lines:
    :return: cell, cursor
    """
    prev_blank = False
    for pos, line in enumerate(lines):
        if start_code_rmd(line):
            if prev_blank and pos > 1:
                return new_markdown_cell(
                    source='\n'.join(lines[:(pos - 1)])), pos
            cell = new_markdown_cell(
                source='\n'.join(lines[:pos]))
            cell.metadata['noskipline'] = True
            return cell, pos

        if _BLANK_LINE.match(line) and prev_blank:
            return new_markdown_cell(
                source='\n'.join(lines[:(pos - 1)])), pos + 1
        prev_blank = _BLANK_LINE.match(line)

    # Unterminated cell?
    return new_markdown_cell(source='\n'.join(lines)), len(lines)
