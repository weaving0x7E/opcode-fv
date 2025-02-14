methods{
    function mathMastersSqrt(uint256) external returns uint256 envfree;
    function uniSqrt(uint256) external returns uint256 envfree;
}

rule uniSqrtMatchesMathMastersSqrt(uint256 x) {
    assert(mathMastersSqrt(x) == uniSqrt(x));
}