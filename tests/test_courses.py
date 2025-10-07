from playwright.sync_api import Page, expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    page = chromium_page_with_state

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    there_is_no_results_block = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(there_is_no_results_block).to_be_visible()
    expect(there_is_no_results_block).to_have_text('There is no results')

    icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icon).to_be_visible()

    block_description = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(block_description).to_be_visible()
    expect(block_description).to_have_text('Results from the load test pipeline will be displayed here')
