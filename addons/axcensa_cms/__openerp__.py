# -*- coding: utf-8 -*-
{
    "name" : "Axcensa CMS",
    "version" : "1.0",
    "author" : "Axcensa Technolgies Pvt Ltd.",
    "website" : "http://www.axcensa.com",
    "category": "College Management System",
    "complexity": "easy",
    "description": """A module to College Management System.
        A Module support the following functionalities:
        1. Admission Procedure
        2. Student Information
        3. Parent Information
        4. Teacher Information
        5. College Information
        6. Standard, Medium and Division Information
        7. Subject Information
                    """,
    "depends" : ["base", "hr", "email_template", "crm"],
    "data" : [
            "wizard/wiz_send_email_view.xml",
            "security/axcensa_cms_security.xml",
            "axcensa_cms_view.xml",
            "security/ir.model.access.csv",
            "admission_workflow.xml",
            "student_sequence.xml",
            "wizard/assign_roll_no_wizard.xml",
            "wizard/move_standards_view.xml",
            "wizard/wiz_meeting_view.xml",
            "indentity_card_report.xml",
            "wizard/wiz_cardregister_view.xml",
    ],
  'demo': [
           'demo/axcensa_cms_demo.xml'
            ],

    'test': [
        'test/axcensa_cms_test.yml',
        'test/assign_roll_no_test.yml',
        ],

    "installable": True,
    "auto_install": False,
    "application": True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: