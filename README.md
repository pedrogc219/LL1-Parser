# Gramática revisada

## Regras de produção

1. FORMULA -> CONSTANTE<br>
2. FORMULA -> PROPOSICAO<br>
3. FORMULA -> ABREPAREN FORMULAINDEFINIDA FECHAPAREN

4. CONSTANTE -> true<br>
5. CONSTANTE -> false

6. PROPOSICAO -> [0-9][0-9a-z]*

7. FORMULAINDEFINIDA -> OPERATORUNARIO FORMULA<br>
8. FORMULAINDEFINIDA -> OPERATORBINARIO FORMULA FORMULA

9. ABREPAREN -> (<br>
10. FECHAPAREN -> )

11. OPERATORUNARIO -> \neg<br>
12. OPERATORBINARIO -> \wedge<br>
13. OPERATORBINARIO -> \vee<br>
14. OPERATORBINARIO -> \rightarrow<br>
15. OPERATORBINARIO -> \leftrightarrow

Nas tabelas utilizo prop=[0-9][0-9a-z]* e operadores em simbolo para não ficar muito texto

<table>
    <tr>
        <td></td>
        <td>FIRST( )</td>
        <td>FOLLOW( )</td>
    </tr>
    <tr>
        <td>FORMULA</td>
        <td>{ true , false , prop , ( }</td>
        <td>{ $ , true , false , prop , ) , ( }</td>
    </tr>
    <tr>
        <td>CONSTANTE</td>
        <td>{ true , false }</td>
        <td>{ $ , true , false , prop , ) , ( }</td>
    </tr>
    <tr>
        <td>PROPOSICAO</td>
        <td>{ prop }</td>
        <td>{ $ , true , false , prop , ) , ( }</td>
    </tr>
    <tr>
        <td>FORMULAINDEFINIDA</td>
        <td>{ ¬ , ⋀ , ⋁ , ⟶ , ⟷ }</td>
        <td>{ ) }</td>
    </tr>
    <tr>
        <td>ABREPAREN</td>
        <td>{ ( }</td>
        <td>{ ¬ , ⋀ , ⋁ , ⟶ , ⟷ }</td>
    </tr>
    <tr>
        <td>FECHAPAREN</td>
        <td>{ ) }</td>
        <td>{ $ , true , false , op , ) , ( }</td>
    </tr>
    <tr>
        <td>OPERATORUNARIO</td>
        <td>{ ¬ }</td>
        <td>{ true , false , op , ( }</td>
    </tr>
    <tr>
        <td>OPERATORBINARIO</td>
        <td>{ ⋀ , ⋁ , ⟶ , ⟷ }</td>
        <td>{ true , false , op , ( }</td>
    </tr>
</table>

<table>
    <tr>
        <td></td>
        <td>true</td>
        <td>false</td>
        <td>prop</td>
        <td>(</td>
        <td>)</td>
        <td>¬</td>
        <td>⋀</td>
        <td>⋁</td>
        <td>⟶</td>
        <td>⟷</td>
        <td>$</td>
    </tr>
    <tr>
        <td>FORMULA</td>
        <td>1</td>
        <td>1</td>
        <td>2</td>
        <td>3</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>CONSTANTE</td>
        <td>4</td>
        <td>5</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>PROPOSICAO</td>
        <td></td>
        <td></td>
        <td>6</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>FORMULAINDEFININDA</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>7</td>
        <td>8</td>
        <td>8</td>
        <td>8</td>
        <td>8</td>
        <td></td>
    </tr>
    <tr>
        <td>ABREPAREN</td>
        <td></td>
        <td></td>
        <td></td>
        <td>9</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>FECHAPAREN</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>10</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>OPERATORUNARIO</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>11</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>OPERATORBINARIO</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>12</td>
        <td>13</td>
        <td>14</td>
        <td>15</td>
        <td></td>
    </tr>
</table>
<hr>