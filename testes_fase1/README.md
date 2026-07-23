# Testes — Fase 1

Implementação de algoritmos clássicos com testes automatizados em pytest.

## Algoritmos

| Módulo | Algoritmo | Complexidade |
|---|---|---|
| [`app/busca_binaria.py`](app/busca_binaria.py) | Busca binária iterativa sobre lista ordenada | O(log n) |
| [`app/bubble_sort.py`](app/bubble_sort.py) | Ordenação por bolha com parada antecipada | O(n²) — O(n) no melhor caso |

- `buscaBinaria(arr, baixo, alto, x)` retorna o índice de `x`, ou `-1` quando o elemento não está presente.
- `bubbleSort(arr)` ordena a lista **in-place** e não retorna valor.

## Executando os testes

```bash
cd testes_fase1
pytest
```

Os testes cobrem os casos de borda de cada algoritmo: lista vazia, elemento único, elementos repetidos, lista já ordenada e busca por valor inexistente.
