import sys

class fe_var(object):

    # ----------------------------------------------------------------------------
    # Ensure that the following resolution has been set before starting the execution
    screen_resolution = (1366, 768)
    # ----------------------------------------------------------------------------

    # FE Executable name including path
    executable_name = "C:\TataElxsi\FalconEye\FalconDesktopClient\FalconDesktopClient.exe"
    exe_file_name = "FalconDesktopClient.exe"
    fe_version = "5.1.2.3"

    # username, password
    # fe_username = "fe_auto_user"
    # fe_password = "fe_auto_user"

    fe_username = "fe_auto_user"
    fe_password = "fe_auto_user"

    # incorrect username/password
    fe_wrong_username = "wrong_feuser"
    fe_wrong_password = "wrong_pass"

    # direcroies
    base_dir = "D://01_Projects//0101_FE_AUTO//09_pyautoit//scripts//01_feauto"
    script_dir = base_dir + "//fe_scripts//"
    im_dir = base_dir + "//fe_images//"
    screenshot_dir = base_dir + "//fescreenshots//"
    ocr_dir = base_dir + "//felogs_ocrim//"
    report_dir = base_dir + "//fereports//reports//"
    log_dir = base_dir + "//fereports//logs//"

    fe_win_title = "FalconEye {} ({}) - [{}]"
    check_point_explorer_title = "Checkpoint Explorer "
    new_chkpt_win_title = "Enter the name of the OCR Checkpoint"

    fe_login_win_title = "FalconEye Login"
    fe_home_title_text = "MultiGrid"
    home_identifier_text = "RackView"
    scheduler_title = "SchedulerForm"
    fe_test_job_name = "fe_test_job_{}"
    fe_job_name = "fe_test_job_"
    fe_test_chkpt_name = "fe_test_chkpt_{}"
    no_of_jobs = 2

    #-------------------------------------------------- UI VERIFICATIONS ----------------------------------------------------#
    # MAIN FORM ITEMS   -------------------------------------------------
    # screens ; Screen name -> Title as in the 'FalconEye 5.0.17.3 (FEUser) - [Multigrid]'
    # and the keyboard shotcut to go to the window
    screens = {
        "home" : ("^d","MultiGrid"),
        "script_editor" : ("^q", "Script Editor"),
        "scheduler" : ("^h", "SchedulerForm"),
        "reports" : ("^r", "Reports Form"),
        "configure" : ("^o", "Configure"),
        "users_and_roles" : ("^u", "UsersAndRoles")
    }

    # SCHEDULER WINDOW ITEMS    ----------------------------------------
    # scheduler ui
    scheduler_screen = {
        "createjob": "btn_scheduler_createjob.png",
        "editjob": "btn_scheduler_editjob.png",
        "removejob_inactive": "btn_scheduler_removejob_inactive.png",
        "removejob_active": "btn_scheduler_removejob_active.png",
        "stopexe_inactive": "btn_scheduler_stopexe_inactive.png",
        "stopexe_active" : "btn_scheduler_stopexe_active.png",
        "refresh": "btn_scheduler_refresh.png",
    }

    # MENU BAR ITEMS    --------------------------------------------------
    # FE menu bar and verification items
    # item_name: image to verify, keycode to send if required
    # menubar_old = {
    #     'menu_bar': ('menu_bar.png', None),
    #     'filemenu_logoff': ('filemenu_logoff.png', "{ALT}{DOWN}"),
    #     'filemenu_exit': ('filemenu_exit.png', "{ALT}{DOWN}"),
    #     'editmenu_items': ('editmenu_items.png', "{ALT}{RIGHT}{DOWN}"),
    #     'viewmenu_items': ('viewmenu_items.png', "{ALT}{RIGHT}2{DOWN}"),
    #     'settingsmenu_items': ('settingsmenu_items.png', "{ALT}{RIGHT}3{DOWN}"),
    #     'helpmenu_items': ('helpmenu_items.png', "{ALT}{RIGHT}4{DOWN}")
    # }

    menubar = {
        'menu_bar': ('menu_bar.png', None),
        'filemenu_logoff': ('filemenu_logoff.png', ("{ALT}", "{DOWN}")),
        'filemenu_exit': ('filemenu_exit.png', ("{ALT}", "{DOWN}")),
        'editmenu_items': ('editmenu_items.png', ("{ALT}", "{RIGHT}", "{DOWN}")),
        'viewmenu_items': ('viewmenu_items.png', ("{ALT}", "{RIGHT}2", "{DOWN}")),
        'settingsmenu_items': ('settingsmenu_items.png', ("{ALT}", "{RIGHT}3", "{DOWN}")),
        'helpmenu_items': ('helpmenu_items.png', ("{ALT}", "{RIGHT}4", "{DOWN}"))
    }

    # DUT VIEW ITEMS    ------------------------------------------------------
    dut_view_ui = {
        "properties_window" : ("tab_dut_properties.png", "tab_slot_properties.png"),
        "power_buttons" : ("btn_power_toggle.png", "btn_power_cycle.png"),
        "show_video" : ("btn_show_video.png",),
        "display_log" : ("btn_display_log.png",),
        "record" : ("btn_start_recording.png",),
        "view_macros" : ("btn_view_macros.png",),
        "add_removedevice" : ("btn_add_device_inactive.png", "btn_remove_device.png"),
        "properties_grid" : ("btn_properties_grid.png",),
        "edit_custom_attr" : ("btn_edit_custome_attr.png",)

    }

    #   Keys to launch a window
    dut_type_editor_keys = ("{ALT}", "{RIGHT}", "{DOWN}", "{DOWN}", "{DOWN}", "{ENTER}")

    # DUT TYPE EDITOR UI ITEMS  ----------------------------------------------
    dut_type_editor_ui = {
        "title" : "title_dut_type_editor.png",
        "add" : "btn_add_dut_type_editor.png",
        "delete": "btn_delete_dut_type_editor.png",
        "save": "btn_save_dut_type_editor.png",
        "refresh": "btn_refresh_dut_type_editor.png",
    }

    # CHECKPOINT EXPLORER UI ITEMS  ------------------------------------------
    check_point_explorer_ui = {
        "new" : "btn_chkpt_explr_new.png",
        "delete_inactive" : "btn_chkpt_explr_delete_inactive.png",
        "save_inactive" : "btn_chkpt_explr_save_inactive.png",
        "refresh" : "btn_chkpt_explr_refresh.png",
        "quick_capture" : "btn_chkpt_explr_quick_capture.png",
        "open_frame_inactive" : "btn_chkpt_explr_open_frame_inactive.png",
        "box_type_selector" : "chkpt_explr_box_type_selector.png",
        "search_chkpt" : "txt_search_chkpt.png",
        "chkpt_coordinate_area" : "chkpt_coordinate_area.png",
        "chkpt_test_ocr": "chkpt_test_ocr.png",
        "chkpt_list" : ("chkpt_ic_icon.png", "chkpt_ocr_icon.png")
    }

    # REPORTS UI ITEMS  ------------------------------------------------------
    reports_ui = {
        "tree_view" : "reports_tree_view.png",
        "property_grid" : "reports_property_grid.png",
        "export" : "btn_export_report.png",
        "print" : "btn_print_report.png",
        "refresh" : "btn_refresh_report.png",
        "delete" : "btn_delete_report.png",
        "search" : "txt_search_report.png",
        "context_menu" : ("test_result_context_menu_inactive_option.png", "test_result_context_menu.png")
    }


    # ------------------------------------------------------   IMAGES  -----------------------------------------------------------#
    # SCHEDULER - CREATE JOB -------------------------------
    img_create_job = "btn_scheduler_createjob.png"
    img_search_job_edit_box = "txt_search_job_scheduler.png"
    img_search_job_edit_box_focused = "txt_search_job_scheduler_focused.png"
    img_job_details = "title_job_details.png"
    img_triggers_job_details = "tab_triggers_job_details.png"
    img_testcases_job_details = "btn_testcases_job_details.png"
    img_device_details = "btn_device_details.png"
    img_expand_icon = "btn_expand_icon.png"
    img_select_folder = "tc_folder_to_select.png"
    img_add_tc = "btn_add_tc_right_arrow.png"
    img_select_device = "device_iphone.png"
    img_add_device = "btn_add_device_right_arrow.png"
    img_save_job = "btn_save_job.png"
    img_fe_test_job = "fe_test_job.png"
    img_test_result = "test_result.png"
    img_new_trigger = "btn_new_trigger.png"
    sched_conflict_window_title = "Conflicting Schedules"
    sched_conflict_yes = "btn_yes_schedule_conflict.png"
    btn_login = "btn_login.png"
    btn_delete_report = "btn_delete_report.png"
    confirm_delete_job = "btn_save_job.png"
    start_execution = "start_execution.png"
    choose_dut = "choose_dut.png"

    # CHECKPOINT EXPLORER -------------------------------
    create_new_checkpoint = "btn_new_checkpoint.png"
    checkpoint_dut_type = "dut_type.png"
    checkpoint_select_dut = "select_dut.png"
    checkpoint_quick_capture = "quick_capture.png"
    checkpoint_coordinates = "coord_text_box.png"
    ocr_ref_text_box = "ocr_ref_text.png"
    checkpoint_save_button = "btn_checkpoint_save.png"
    ic_ref_img_btn = "btn_set_ic_ref_img.png"
    checkpoint_search_box = "chkpt_search_box.png"
    search_list_ocr_chkpt = "search_list_ocr_chkpt.png"
    search_list_ic_chkpt = "search_list_ic_chkpt.png"
    filled_checkpoint_search_box = "filled_checkpoint_search_box.png"
	
	
    ocr_checkpoint_name = "FE_test_OCR_{}"
    ic_checkpoint_name = "FE_test_IC_{}"
    chkpt_explr_icon = "btn_chpt_explr.png"
    chkpt_explr_list_header = "chkpt_explr_list_header.png"

    # REPORTS ------------------------------------------
    delete_job_report = "delete_report_context_menu.png"

    # keys
    kbd_keys = {
        "TAB" : "{TAB}",
        "ENTER" : "{ENTER}",
        "BS" : "{BACKSPACE}",
        "DOWN" : "{DOWN}",
        "RIGHT" : "{RIGHT}"
    }


    # waitimes
    t_waittime_for_window = 10 # in seconds

    # Navigation
    nav_test_result = ("{TAB}4", "{DOWN}")
	
    # -------------------------------------   Macro UI  ---------------------------------------------#
    # macro image name
    macro_btn = "btn_view_macros.png"

    # USER MANAGEMENT WINDOW ITEMS    ----------------------------------------
    # user management ui
    user_management_screen = {
        "Add": "btn_add_user.png",
        "Remove": "btn_remove_inactive.png",
        "Refresh": "btn_refresh_user.png"
    }

    usr_grp_management_screen = {
        "Add": "btn_usr_grp_add.png",
        "Remove": "btn_usr_grp_remove.png",
        "Save": "btn_usr_grp_save.png",
        "Refresh": "btn_usr_grp_refresh.png"
    }

    role_grp_management_screen = {
        "Add" : "btn_role_add.png",
        "Remove" : "btn_role_remove.png",
        "Save" : "btn_role_save.png",
        "Refresh" : "btn_role_refresh.png"
    }

	
	
    # -------------------------------------     TRASH   ---------------------------------------------#
    # coordinates
    c_fe_screenshot = (76, 1, 1365, 765)    # x, y, w, h
    # script_editor
    c_check_pt_ex = [403, 91]
    nav_keys_script_editor = ["{ALT}", "{RIGHT}2", "{DOWN}2", "{ENTER}"]

    default_trigger_delay = 4
    wait_until_local_execution = 60    # wait time for completing the execution
    wait_until_schedule_execution = 60



    # -------------------------------------     OCR   ---------------------------------------------#
    basewidth = 1000
    ocr_img_name = "fe_ocr_{}.png"

    c_job_status_props = (1231, 533, 70, 15)
    c_job_status_list = (769, 133, 70, 15)
    c_job_in_report = (127, 133, 170, 15)
    c_reports_test_result = (579, 227, 80, 15)

    ocr_param = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
    possible_test_results = ("Passed", "Failed", "Unknown", "Error")
    export_report_pages = {
        "reports" : (936, 646),
        "script_editor" : (711, 671)
    }

    str_test_result = "TEST_RESULT"
    pattern_test_result = str_test_result +" | {} |"

    class_tree_view = "WindowsForms10.SysTreeView32.app.0.62e449_r13_ad1"
    script_editor_node = "SANITY_CHECK"

    tab = kbd_keys['TAB']
    down = kbd_keys['DOWN']
    right = kbd_keys['RIGHT']
    enter = kbd_keys['ENTER']
    keys_to_open_script = (tab, tab, down, down, right, down, enter)
