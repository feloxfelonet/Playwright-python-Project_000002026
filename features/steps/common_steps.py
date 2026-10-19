import re

from behave import given, when, then
from playwright.sync_api import expect

BASE_URL = "https://www.saucedemo.com/"


@given("I open the SauceDemo website")
def step_open_saucedemo(context):
    context.page.goto(BASE_URL, wait_until="domcontentloaded")


@given('I log in as "{username}" with password "{password}"')
def step_login_as(context, username, password):
    context.page.goto(BASE_URL, wait_until="domcontentloaded")
    context.page.locator('[data-test="username"]').fill(username)
    context.page.locator('[data-test="password"]').fill(password)
    context.page.locator('[data-test="login-button"]').click()


@when('I enter username "{username}" and password "{password}"')
def step_enter_credentials(context, username, password):
    context.page.locator('[data-test="username"]').fill(username)
    context.page.locator('[data-test="password"]').fill(password)


@when("I click the login button")
def step_click_login(context):
    context.page.locator('[data-test="login-button"]').click()


@then("I should see the products page")
def step_products_page(context):
    expect(context.page).to_have_url(re.compile(r".*/inventory\.html$"))
    expect(context.page.locator(".inventory_list")).to_be_visible()


@then('I should see a login error containing "{message}"')
def step_login_error(context, message):
    error = context.page.locator('[data-test="error"]')
    expect(error).to_be_visible()
    expect(error).to_contain_text(message)


@then("I should see at least one product")
def step_at_least_one_product(context):
    expect(context.page.locator(".inventory_item").first).to_be_visible()


@when('I sort products by "{sort_option}"')
def step_sort_products(context, sort_option):
    options = {
        "Name (A to Z)": "az",
        "Name (Z to A)": "za",
        "Price (low to high)": "lohi",
        "Price (high to low)": "hilo",
    }
    if sort_option not in options:
        raise AssertionError(f"Unsupported sort option: {sort_option}")
    context.page.locator('[data-test="product-sort-container"]').select_option(
        options[sort_option]
    )


@then("product prices should be sorted from low to high")
def step_prices_low_to_high(context):
    price_texts = context.page.locator(".inventory_item_price").all_text_contents()
    prices = [float(re.sub(r"[^0-9.]", "", price)) for price in price_texts]
    assert prices == sorted(prices), f"Prices are not sorted low-to-high: {prices}"


@when('I add "{product_name}" to the cart')
def step_add_product_to_cart(context, product_name):
    product = context.page.locator(".inventory_item").filter(
        has=context.page.get_by_text(product_name, exact=True)
    )
    expect(product).to_have_count(1)
    product.locator("button").click()


@when('I remove "{product_name}" from the cart')
def step_remove_product_from_cart(context, product_name):
    product = context.page.locator(".inventory_item").filter(
        has=context.page.get_by_text(product_name, exact=True)
    )
    expect(product).to_have_count(1)
    product.locator("button").click()


@then("the cart badge should show {count:d} item")
@then("the cart badge should show {count:d} items")
def step_cart_badge_count(context, count):
    badge = context.page.locator(".shopping_cart_badge")
    if count == 0:
        expect(badge).to_have_count(0)
    else:
        expect(badge).to_have_text(str(count))


@when('I open the product "{product_name}"')
def step_open_product(context, product_name):
    context.page.get_by_text(product_name, exact=True).first.click()


@then('the product details should show "{product_name}"')
def step_product_details(context, product_name):
    expect(context.page.locator(".inventory_details_name")).to_have_text(product_name)
    expect(context.page.locator(".inventory_details_price")).to_be_visible()


@when("I open the shopping cart")
def step_open_cart(context):
    context.page.locator(".shopping_cart_link").click()


@then('the cart should contain "{product_name}"')
def step_cart_contains(context, product_name):
    expect(
        context.page.locator(".cart_item").get_by_text(product_name, exact=True)
    ).to_be_visible()


@when("I start checkout")
def step_start_checkout(context):
    context.page.locator('[data-test="checkout"]').click()


@when('I enter checkout details "{first_name}", "{last_name}", "{postal_code}"')
def step_enter_checkout_details(context, first_name, last_name, postal_code):
    context.page.locator('[data-test="firstName"]').fill(first_name)
    context.page.locator('[data-test="lastName"]').fill(last_name)
    context.page.locator('[data-test="postalCode"]').fill(postal_code)


@when("I continue checkout")
def step_continue_checkout(context):
    context.page.locator('[data-test="continue"]').click()


@then("the checkout information error should be visible")
def step_checkout_error_visible(context):
    expect(context.page.locator('[data-test="error"]')).to_be_visible()


@then("the checkout overview should be displayed")
def step_checkout_overview(context):
    expect(context.page.locator(".checkout_summary_container")).to_be_visible()


@when("I finish checkout")
def step_finish_checkout(context):
    context.page.locator('[data-test="finish"]').click()


@then("the order confirmation should be displayed")
def step_order_confirmation(context):
    expect(context.page.locator(".complete-header")).to_contain_text(
        "Thank you for your order"
    )


@when("I open the navigation menu")
def step_open_menu(context):
    context.page.locator("#react-burger-menu-btn").click()
    expect(context.page.locator("#logout_sidebar_link")).to_be_visible()


@when("I log out")
def step_logout(context):
    context.page.locator("#logout_sidebar_link").click()


@then("I should be logged out")
def step_logged_out(context):
    expect(context.page.locator('[data-test="login-button"]')).to_be_visible()
    expect(context.page.locator('[data-test="username"]')).to_be_visible()
