"""Run with: python3 -m unittest discover -s scripts -p 'test_*.py'."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).with_name('import_research.py')
spec = importlib.util.spec_from_file_location('research_importer', SCRIPT)
importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(importer)


class ResearchFiguresTest(unittest.TestCase):
    def test_all_figures_preserve_surrounding_prose(self):
        figures = importer.load_site_figures()
        for slug, figure in figures.items():
            with self.subTest(slug=slug):
                # Start with reviewed site prose, restoring only the original diagram.
                current = (SCRIPT.parent.parent / 'content/research' / slug / 'index.md').read_text()
                source = current.replace(figure['shortcode'], '```mermaid\n' + figure['source'] + '\n```')
                self.assertEqual(importer.render_site_figures(source, slug, figures), current)

    def test_source_changes_cannot_silently_drop_milestones(self):
        figures = importer.load_site_figures()
        for slug, figure in figures.items():
            body = '```mermaid\n' + figure['source'] + '\n```'
            for changed in ('No diagram', body + '\n' + body, body.replace(figure['source'], figure['source'] + '\nNEW')):
                with self.subTest(slug=slug, change=changed[-20:]):
                    with self.assertRaisesRegex(ValueError, 'source diagram changed'):
                        importer.render_site_figures(changed, slug, figures)
        self.assertEqual(importer.render_site_figures('ordinary prose', 'unmapped', figures), 'ordinary prose')

    def test_reviewed_material_is_preserved(self):
        for marker in ('## From the book\n', 'Checked against the audiobook edition', '<!-- reader-review: 2026-09-15 -->'):
            with self.subTest(marker=marker):
                with self.assertRaisesRegex(ValueError, 'remove book-review material'):
                    importer.validate_review_provenance(marker, 'Older copy', 'example')
                importer.validate_review_provenance(marker, marker + '\nA revised passage', 'example')
        importer.validate_review_provenance('Unreviewed draft', 'A revision', 'example')

    def test_stale_source_fails_before_any_output_is_written(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            page = root / 'content/research/example/index.md'
            page.parent.mkdir(parents=True)
            page.write_text('## From the book\nReviewed material\n')
            index = page.parent.parent / '_index.md'
            index.write_text('Existing transcript\n')
            pages = {'Example': {'slug': 'example', 'title': 'Example', 'body': 'Older draft', 'anchor': 'a01', 'short': 'Summary'}}
            with patch.object(importer, '__file__', str(root / 'scripts/import_research.py')), \
                 patch.object(importer, 'load_pages', return_value=pages), \
                 patch.object(importer, 'parse_transcript', return_value=([], [], None)), \
                 patch.object(importer, 'load_site_figures', return_value={}), \
                 patch('sys.argv', ['import_research.py', '--write']):
                with self.assertRaisesRegex(ValueError, 'remove book-review material'):
                    importer.main()
            self.assertEqual(page.read_text(), '## From the book\nReviewed material\n')
            self.assertEqual(index.read_text(), 'Existing transcript\n')


if __name__ == '__main__':
    unittest.main()
