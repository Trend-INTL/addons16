# See LICENSE file for full copyright and licensing details.

{
    'name': 'Whatsapp POS',
    'version': '16.0.0.1.0',
    'license': 'OPL-1',
    'author': "Alphasoft",
    'sequence': 1,
    'website': 'https://www.alphasoft.co.id/',
    'images':  ['images/main_screenshot.png'],
    'summary': 'This module is used for Whatsapp Point of Sales',
    'category': 'Extra Tools',
    'depends': ['base_automation', 'point_of_sale', 'aos_whatsapp'],
    'data': [
        #'report/point_of_sale_report.xml',
        'data/pos_data.xml',
        # 'views/pos_order_view.xml',
        'views/pos_config_view.xml',
        'views/templates.xml',
        #'wizard/whatsapp_compose_view.xml',
    ],
    'external_dependencies': {'python': ['html2text']},
    # 'qweb': [
    #     'static/src/xml/mobile_widget.xml',
    #     'static/src/xml/pos_whatsapp.xml',
    #     'static/src/xml/ClientListScreen/ClientLine.xml',
    #     'static/src/xml/ClientListScreen/ClientDetailsEdit.xml',
    #     'static/src/xml/ClientListScreen/ClientListScreen.xml',
    # ],
    'assets': {
        # 'web.report_assets_common': [
        #     'web/static/src/legacy/scss/views.scss',
        #     'web/static/src/legacy/scss/graph_view.scss',
        #     'stock/static/src/scss/report_stock_forecasted.scss',
        #     'stock/static/src/scss/report_stock_reception.scss',
        #     'stock/static/src/scss/report_stock_rule.scss',
        # ],
        # 'web.assets_common': [
        #     'stock/static/src/scss/stock_traceability_report.scss',
        # ],
        'point_of_sale.assets': [
            #'aos_whatsapp_pos/static/src/js/models.js',
            #'aos_whatsapp_pos/static/src/js/ReceiptScreen/ReceiptScreen.js',
            'aos_whatsapp_pos/static/src/js/**/*.js',
            'aos_whatsapp_pos/static/src/xml/**/*.xml',
        ],
        # 'web.assets_qweb': [
        #     'aos_whatsapp_pos/static/src/xml/**/*',
        # ],
        # 'web.assets_tests': [
        #     'stock/static/tests/tours/stock_report_tests.js',
        # ],
        # 'web.qunit_suite_tests': [
        #     'stock/static/tests/singleton_list_tests.js',
        #     'stock/static/tests/popover_widget_tests.js',
        #     'stock/static/tests/lazy_column_list_tests.js',
        #     'stock/static/tests/stock_traceability_report_backend_tests.js',
        # ],
        # 'web.assets_qweb': [
        #     'stock/static/src/xml/inventory_report.xml',
        #     'stock/static/src/xml/inventory_lines.xml',
        #     'stock/static/src/xml/popover_widget.xml',
        #     'stock/static/src/xml/forecast_widget.xml',
        #     'stock/static/src/xml/report_stock_forecasted.xml',
        #     'stock/static/src/xml/report_stock_reception.xml',
        #     'stock/static/src/xml/stock_orderpoint.xml',
        #     'stock/static/src/xml/stock_traceability_report_backend.xml',
        # ],
    },
    'demo': [],
    'test': [],
    'css': [],
    'js': [],
    'price': 0,
    'currency': 'EUR',
    'installable': True,
    'application': False,
    'auto_install': False,
}
