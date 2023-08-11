import os
import pytest


def test_system_echo(capfd):
    os.system('echo hello')
    captured = capfd.readouterr()
    assert captured.out == "hello\r\n"


def test_system_echo2(capfdbinary):
    os.system('echo hello')
    captured = capfdbinary.readouterr()
    assert captured.out == b"hello\r\n"


def test_output(capsys):
    print("hello")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"


def test_output2(capsysbinary):
    print("hello")
    captured = capsysbinary.readouterr()
    assert captured.out == b"hello\n"


