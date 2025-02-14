/*
* verification of mulwad
*/
methods {
    function mulWadUp(uint256 x, uint256 y) external returns uint256 envfree;
}

definition WAD() returns uint256 = 1000000000000000000;

/*
*Counterexample: 
    p_x_uint256 = 0x00000000000000000000000000000000f19866de987215df6dfe42db8fad1f57 (321135262548273312133946758132849778519)
    p_y_uint256 = 0x00000000000000000000000000000000eaffffc303b831f805285ead2c118378 (312368574177688450113665034893724320632)
*/

rule check_MulWadUpFuzz(uint256 x, uint256 y) {
    require (x == 0 || y == 0 || y <= assert_uint256(max_uint256 / x));
    uint256 result = mulWadUp(x, y);
    mathint expected = x * y == 0 ? 0 : (x * y - 1) / WAD() + 1;
    assert(result == assert_uint256(expected));
}

invariant mulWadUpInvariant(uint256 x, uint256 y)
    mulWadUp(x, y) == assert_uint256(x * y == 0 ? 0 : (x * y - 1) / WAD() + 1)
    {
            preserved {
                require (x == 0 || y == 0 || y <= assert_uint256(max_uint256 / x));
            }
    }