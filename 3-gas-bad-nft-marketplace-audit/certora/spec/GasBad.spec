using GasBadNftMarketplace as gasBadNftMarketplace;
using NftMarketplace as nftMarketplace;

methods{
    function getListing(address nftAddress, uint256 tokenId) external returns (INftMarketplace.Listing) envfree;
    function getProceeds(address seller) external returns uint256 envfree;
}


// axiom作为一种公理来存在
ghost mathint listingUpdatesCount {
    init_state axiom listingUpdatesCount == 0;
}
ghost mathint log4Count{
    init_state axiom log4Count == 0;
}

// hook用于把opcode与某种触发器绑定
// 也就是s_listings[KEY address nftAddress][KEY uint256 tokenId].price在被Sstore调用时，Hook会执行它的函数体
hook Sstore s_listings[KEY address nftAddress][KEY uint256 tokenId].price
uint256 price {
    listingUpdatesCount = listingUpdatesCount + 1;
}

// 检查map更新时log是否发出
hook LOG4(uint offset, uint length, bytes32 t1, bytes32 t2, bytes32 t3, bytes32 t4) {
    log4Count = log4Count + 1;
}

invariant anytime_mapping_updated_emit_event()
    listingUpdatesCount <= log4Count;

rule calling_any_function_should_result_in_each_contract_having_the_same_state(method f, method f2){
    // 1.调用GasBad和NftMarketPlace中同样的函数来比较返回结果是否不同

    require(f.selector == f2.selector);
    env e;
    calldataarg args;
    address listingAddr;
    uint256 tokenId;
    address seller;

    require(gasBadNftMarketplace.getProceed(e, seller) == nftMarketplace.getProceeds(e, seller));
    require(gasBadNftMarketplace.getListing(e, listingAddr, tokenId).price == nftMarketplace.getListing(e, listingAddr, tokenId).price);
    require(gasBadNftMarketplace.getListing(e, listingAddr, tokenId).seller == nftMarketplace.getListing(e, listingAddr, tokenId).seller);


    gasBadNftMarketplace.f(e, args);
    nftMarketplace.f2(e,args);

    assert(gasBadNftMarketplace.getProceed(e, seller) == nftMarketplace.getProceeds(e, seller));
    assert(gasBadNftMarketplace.getListing(e, listingAddr, tokenId).price == nftMarketplace.getListing(e, listingAddr, tokenId).price);
    assert(gasBadNftMarketplace.getListing(e, listingAddr, tokenId).seller == nftMarketplace.getListing(e, listingAddr, tokenId).seller);

}