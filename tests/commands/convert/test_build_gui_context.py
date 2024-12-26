def test_overrides_are_used(convert_command):
    overrides = {"gui_framework": "Toga", "console_app": "true"}
    out = convert_command.build_gui_context({}, overrides)
    assert out["gui_framework"] == "None"
    assert overrides["gui_framework"] == "Toga"
    assert out["console_app"] == "true"
