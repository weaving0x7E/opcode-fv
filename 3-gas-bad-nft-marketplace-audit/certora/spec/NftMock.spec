methods {
    function totalSupply() external returns uint256 envfree;
    function mint() external;
    function balanceOf(address) external returns uint256 envfree;
}

// invariant totalSupplyIsNotNegative()
//     totalSupply() >= 0;

// rule minting_mints_one_nft() {
//     // arrange
//     env e;
//     address minter;

//     require e.msg.value == 0;
//     require e.msg.sender == minter;
//     mathint balanceBefore = balanceOf(minter);

//     // act
//     currentContract.mint(e);

//     // assert
//     assert to_mathint(balanceOf(minter)) == balanceBefore + 1, "Only 1 NFT should be mint";

// }

// rule sanity {
//     satisfy true;
// }

// 这种方法类似于Stateful Fuzz，可以让certora传入任意method f
// 来检查是否会打破不变性
// rule no_change_to_total_supply(method f) {
//     uint256 totalSupplyBefore = totalSupply();

//     env e;
//     calldataarg arg;
//     f(e,arg);

//     assert totalSupply() == totalSupplyBefore, "supply should not change";
// }