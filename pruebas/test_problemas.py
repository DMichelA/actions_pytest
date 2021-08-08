import pytest
import problemas as pro

def test_orden_arreglo():
    numbers = [1, 3, 4, 2, 5]
    assert pro.orden_arreglo(numbers) == [1, 2, 3, 4, 5]

def test_personas_mayores():
    info = [
    {"nombre":"Amairani", "edad":21},
    {"nombre":"Petra", "edad":22},
    {"nombre":"Mario", "edad":17}, 
    {"nombre":"Jaime", "edad":24},
    {"nombre":"Martina", "edad":15},
    {"nombre":"Martina", "edad":18}
    ]
    assert pro.personas_mayores(info) == 4