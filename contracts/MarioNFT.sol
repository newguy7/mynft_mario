// SPDX-License-Identifier: MIT
pragma solidity 0.7.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract MarioNFT is ERC721 {
    uint256 public tokenCounter;
    uint256 public maxLogos = 3;

    enum Logos {
        BOWSER,
        LUIGI,
        MARIO
    }

    mapping(uint256 => Logos) public tokenIdToLogo;
    mapping(uint256 => address) public requestIdToSender;

    event requestedLogo(uint256 indexed requestId, address requester);
    event logoAssigned(uint256 indexed tokenId, Logos logos);

    constructor() public ERC721("1150029", "ANU") {
        tokenCounter = 0;
    }

    function createLogoNFT(string memory _tokenURI) public returns (bytes32) {
        require(tokenCounter <= maxLogos, "Maximun quantity of logos emitted");
        uint256 newTokenID = tokenCounter;

        requestIdToSender[newTokenID] = msg.sender;
        emit requestedLogo(newTokenID, msg.sender);
        Logos logos = Logos(newTokenID);
        emit logoAssigned(newTokenID, logos);

        _safeMint(msg.sender, newTokenID);
        _setTokenURI(newTokenID, _tokenURI);
        tokenCounter += 1;
    }
}
