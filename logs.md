(.venv) PS C:\Users\DELL\Desktop\dashboards> python -m worker.main
2025-12-03 13:48:04,509 - __main__ - INFO - Worker starting. Job will run every 10 minutes.
2025-12-03 13:48:04,511 - __main__ - INFO - Starting P2P data extraction job...
2025-12-03 13:48:04,512 - worker.extractor - INFO - Fetching all trading pairs...
2025-12-03 13:48:06,413 - worker.extractor - ERROR - Error fetching trading pairs: 404 Client Error: Not Found for url: https://p2p.binance.com/bapi/c2c/v2/public/c2c/asset-order/getAllSupportAsset
2025-12-03 13:48:06,416 - worker.extractor - ERROR - No trading pairs found
2025-12-03 13:48:06,416 - __main__ - INFO - P2P data extraction job finished successfully.


# second run 

(.venv) PS C:\Users\DELL\Desktop\dashboards> python -m worker.main 
2025-12-03 13:51:22,910 - __main__ - INFO - Worker starting. Job will run every 10 minutes.
2025-12-03 13:51:22,914 - __main__ - INFO - Starting P2P data extraction job...
2025-12-03 13:51:22,914 - worker.extractor - INFO - Fetching all trading pairs...
2025-12-03 13:51:24,477 - worker.extractor - ERROR - Error fetching trading pairs: 404 Client Error: Not Found for url: https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/asset-item/list
2025-12-03 13:51:24,477 - worker.extractor - ERROR - No trading pairs found
2025-12-03 13:51:24,478 - __main__ - INFO - P2P data extraction job finished successfully.

# Third run (after creating temp_playwright_script)

(.venv) PS C:\Users\DELL\Desktop\dashboards> python -m worker.main 
2025-12-03 14:12:42,761 - __main__ - INFO - Worker starting. Job will run every 10 minutes.
2025-12-03 14:12:42,767 - __main__ - INFO - Starting P2P data extraction job...
2025-12-03 14:12:42,767 - worker.extractor - INFO - Fetching all trading pairs...
2025-12-03 14:12:44,453 - worker.extractor - WARNING - No fiat currencies found from the fiat list endpoint.
2025-12-03 14:12:44,454 - worker.extractor - ERROR - No trading pairs found
2025-12-03 14:12:44,455 - __main__ - INFO - P2P data extraction job finished successfully.

#Fourth Run

2025-12-03 14:34:08,028 - worker.extractor - INFO - Extracted 0 offers for CNY/ETH/SELL
2025-12-03 14:34:08,042 - worker.extractor - INFO - Extracting DKK/USDT/SELL
2025-12-03 14:34:08,688 - worker.extractor - ERROR - Failed to extract CRC/USDT/BUY: illegal parameter
2025-12-03 14:34:08,724 - worker.extractor - INFO - Extracted 0 offers for CRC/USDT/BUY
2025-12-03 14:34:08,725 - worker.extractor - INFO - Extracting DKK/BTC/BUY
2025-12-03 14:34:09,307 - worker.extractor - ERROR - Failed to extract CRC/USDT/SELL: illegal parameter
2025-12-03 14:34:09,311 - worker.extractor - INFO - Extracted 0 offers for CRC/USDT/SELL
2025-12-03 14:34:09,320 - worker.extractor - INFO - Extracting DKK/BTC/SELL
2025-12-03 14:34:09,555 - worker.rate_limiter - WARNING - Rate limiter active: 700 waits, 797 total requests
2025-12-03 14:34:09,871 - worker.extractor - ERROR - Failed to extract CRC/ETH/SELL: illegal parameter
2025-12-03 14:34:09,907 - worker.extractor - INFO - Extracted 0 offers for CRC/ETH/SELL
2025-12-03 14:34:09,908 - worker.extractor - INFO - Extracting DKK/ETH/BUY
2025-12-03 14:34:10,428 - worker.extractor - ERROR - Failed to extract CVE/USDT/SELL: illegal parameter
2025-12-03 14:34:10,442 - worker.extractor - INFO - Extracted 0 offers for CVE/USDT/SELL
2025-12-03 14:34:10,446 - worker.extractor - INFO - Extracting DKK/ETH/SELL
2025-12-03 14:34:11,069 - worker.extractor - ERROR - Failed to extract CRC/ETH/BUY: illegal parameter
2025-12-03 14:34:11,120 - worker.extractor - INFO - Extracted 0 offers for CRC/ETH/BUY
2025-12-03 14:34:11,211 - worker.extractor - INFO - Extracting ERN/USDT/BUY
2025-12-03 14:34:11,926 - worker.extractor - ERROR - Failed to extract CRC/BTC/BUY: illegal parameter
2025-12-03 14:34:11,955 - worker.extractor - INFO - Extracted 0 offers for CRC/BTC/BUY
2025-12-03 14:34:12,053 - worker.extractor - INFO - Extracting ERN/USDT/SELL
2025-12-03 14:34:12,479 - worker.extractor - ERROR - Failed to extract CVE/USDT/BUY: illegal parameter
2025-12-03 14:34:12,519 - worker.extractor - INFO - Extracted 0 offers for CVE/USDT/BUY
2025-12-03 14:34:12,591 - worker.extractor - INFO - Extracting ERN/BTC/BUY
2025-12-03 14:34:13,086 - worker.extractor - ERROR - Failed to extract CRC/BTC/SELL: illegal parameter
2025-12-03 14:34:13,103 - worker.extractor - INFO - Extracted 0 offers for CRC/BTC/SELL
2025-12-03 14:34:13,111 - worker.extractor - INFO - Extracting ERN/BTC/SELL
2025-12-03 14:34:13,677 - worker.extractor - ERROR - Failed to extract CVE/BTC/BUY: illegal parameter
2025-12-03 14:34:13,695 - worker.extractor - INFO - Extracted 0 offers for CVE/BTC/BUY
2025-12-03 14:34:13,696 - worker.extractor - INFO - Extracting ERN/ETH/BUY
2025-12-03 14:34:14,301 - worker.extractor - ERROR - Failed to extract CVE/BTC/SELL: illegal parameter
2025-12-03 14:34:14,307 - worker.extractor - INFO - Extracted 0 offers for CVE/BTC/SELL
2025-12-03 14:34:14,307 - worker.extractor - INFO - Extracting ERN/ETH/SELL
2025-12-03 14:34:14,908 - worker.extractor - ERROR - Failed to extract CVE/ETH/BUY: illegal parameter
2025-12-03 14:34:14,925 - worker.extractor - INFO - Extracted 0 offers for CVE/ETH/BUY
2025-12-03 14:34:14,926 - worker.extractor - INFO - Extracting GMD/USDT/BUY
2025-12-03 14:34:15,602 - worker.extractor - ERROR - Failed to extract CVE/ETH/SELL: illegal parameter
2025-12-03 14:34:15,608 - worker.extractor - INFO - Extracted 0 offers for CVE/ETH/SELL
2025-12-03 14:34:15,609 - worker.extractor - INFO - Extracting GMD/USDT/SELL
2025-12-03 14:34:15,854 - worker.rate_limiter - WARNING - Rate limiter active: 710 waits, 807 total requests
2025-12-03 14:34:16,120 - worker.extractor - ERROR - Failed to extract DJF/USDT/BUY: illegal parameter
2025-12-03 14:34:16,126 - worker.extractor - INFO - Extracted 0 offers for DJF/USDT/BUY
2025-12-03 14:34:16,135 - worker.extractor - INFO - Extracting GMD/BTC/BUY
2025-12-03 14:34:16,887 - worker.extractor - ERROR - Failed to extract DJF/USDT/SELL: illegal parameter
2025-12-03 14:34:16,972 - worker.extractor - INFO - Extracted 0 offers for DJF/USDT/SELL
2025-12-03 14:34:16,973 - worker.extractor - INFO - Extracting GMD/BTC/SELL
2025-12-03 14:34:17,375 - worker.extractor - ERROR - Failed to extract DJF/BTC/BUY: illegal parameter
2025-12-03 14:34:17,440 - worker.extractor - INFO - Extracted 0 offers for DJF/BTC/BUY
2025-12-03 14:34:17,442 - worker.extractor - INFO - Extracting GMD/ETH/BUY
2025-12-03 14:34:18,111 - worker.extractor - ERROR - Failed to extract DJF/BTC/SELL: illegal parameter
2025-12-03 14:34:18,186 - worker.extractor - INFO - Extracted 0 offers for DJF/BTC/SELL
2025-12-03 14:34:18,336 - worker.extractor - INFO - Extracting GMD/ETH/SELL
2025-12-03 14:34:18,783 - worker.extractor - ERROR - Failed to extract DJF/ETH/BUY: illegal parameter
2025-12-03 14:34:18,942 - worker.extractor - INFO - Extracted 0 offers for DJF/ETH/BUY
2025-12-03 14:34:19,310 - worker.extractor - INFO - Extracting GNF/USDT/BUY
2025-12-03 14:34:19,538 - worker.extractor - ERROR - Failed to extract DJF/ETH/SELL: illegal parameter
2025-12-03 14:34:19,604 - worker.extractor - INFO - Extracted 0 offers for DJF/ETH/SELL
2025-12-03 14:34:19,782 - worker.extractor - INFO - Extracting GNF/USDT/SELL
2025-12-03 14:34:20,337 - worker.extractor - ERROR - Failed to extract DKK/USDT/BUY: illegal parameter
2025-12-03 14:34:20,536 - worker.extractor - INFO - Extracted 0 offers for DKK/USDT/BUY
2025-12-03 14:34:20,848 - worker.extractor - INFO - Extracting GNF/BTC/BUY
2025-12-03 14:34:21,037 - worker.extractor - ERROR - Failed to extract DKK/USDT/SELL: illegal parameter
2025-12-03 14:34:21,301 - worker.extractor - INFO - Extracted 0 offers for DKK/USDT/SELL
2025-12-03 14:34:21,458 - worker.extractor - INFO - Extracting GNF/BTC/SELL
2025-12-03 14:34:21,721 - worker.extractor - ERROR - Failed to extract DKK/BTC/BUY: illegal parameter
2025-12-03 14:34:21,739 - worker.extractor - INFO - Extracted 0 offers for DKK/BTC/BUY
2025-12-03 14:34:21,740 - worker.extractor - INFO - Extracting GNF/ETH/BUY
2025-12-03 14:34:22,473 - worker.extractor - ERROR - Failed to extract DKK/BTC/SELL: illegal parameter
2025-12-03 14:34:22,484 - worker.extractor - INFO - Extracted 0 offers for DKK/BTC/SELL
2025-12-03 14:34:22,485 - worker.extractor - INFO - Extracting GNF/ETH/SELL
2025-12-03 14:34:22,684 - worker.rate_limiter - WARNING - Rate limiter active: 720 waits, 817 total requests
2025-12-03 14:34:22,990 - worker.extractor - ERROR - Failed to extract DKK/ETH/BUY: illegal parameter
2025-12-03 14:34:23,107 - worker.extractor - INFO - Extracted 0 offers for DKK/ETH/BUY
2025-12-03 14:34:23,402 - worker.extractor - INFO - Extracting GTQ/USDT/BUY
2025-12-03 14:34:23,669 - worker.extractor - ERROR - Failed to extract DKK/ETH/SELL: illegal parameter
2025-12-03 14:34:23,749 - worker.extractor - INFO - Extracted 0 offers for DKK/ETH/SELL
2025-12-03 14:34:23,750 - worker.extractor - INFO - Extracting GTQ/USDT/SELL
2025-12-03 14:34:24,333 - worker.extractor - ERROR - Failed to extract ERN/USDT/BUY: illegal parameter
2025-12-03 14:34:24,373 - worker.extractor - INFO - Extracted 0 offers for ERN/USDT/BUY
2025-12-03 14:34:24,374 - worker.extractor - INFO - Extracting GTQ/BTC/BUY
2025-12-03 14:34:24,990 - worker.extractor - ERROR - Failed to extract ERN/USDT/SELL: illegal parameter
2025-12-03 14:34:25,016 - worker.extractor - INFO - Extracted 0 offers for ERN/USDT/SELL
2025-12-03 14:34:25,017 - worker.extractor - INFO - Extracting GTQ/BTC/SELL
2025-12-03 14:34:25,606 - worker.extractor - ERROR - Failed to extract ERN/BTC/BUY: illegal parameter
2025-12-03 14:34:25,637 - worker.extractor - INFO - Extracted 0 offers for ERN/BTC/BUY
2025-12-03 14:34:25,673 - worker.extractor - INFO - Extracting GTQ/ETH/BUY
2025-12-03 14:34:26,248 - worker.extractor - ERROR - Failed to extract ERN/BTC/SELL: illegal parameter
2025-12-03 14:34:26,268 - worker.extractor - INFO - Extracted 0 offers for ERN/BTC/SELL
2025-12-03 14:34:26,288 - worker.extractor - INFO - Extracting GTQ/ETH/SELL
2025-12-03 14:34:26,832 - worker.extractor - ERROR - Failed to extract ERN/ETH/BUY: illegal parameter
2025-12-03 14:34:26,857 - worker.extractor - INFO - Extracted 0 offers for ERN/ETH/BUY
2025-12-03 14:34:26,984 - worker.extractor - INFO - Extracting HNL/USDT/BUY
2025-12-03 14:34:27,457 - worker.extractor - ERROR - Failed to extract ERN/ETH/SELL: illegal parameter
2025-12-03 14:34:27,503 - worker.extractor - INFO - Extracted 0 offers for ERN/ETH/SELL
2025-12-03 14:34:27,521 - worker.extractor - INFO - Extracting HNL/USDT/SELL
2025-12-03 14:34:28,066 - worker.extractor - ERROR - Failed to extract GMD/USDT/BUY: illegal parameter
2025-12-03 14:34:28,087 - worker.extractor - INFO - Extracted 0 offers for GMD/USDT/BUY
2025-12-03 14:34:28,120 - worker.extractor - INFO - Extracting HNL/BTC/BUY
2025-12-03 14:34:28,727 - worker.extractor - ERROR - Failed to extract GMD/USDT/SELL: illegal parameter
2025-12-03 14:34:28,757 - worker.extractor - INFO - Extracted 0 offers for GMD/USDT/SELL
2025-12-03 14:34:28,757 - worker.extractor - INFO - Extracting HNL/BTC/SELL
2025-12-03 14:34:29,039 - worker.rate_limiter - WARNING - Rate limiter active: 730 waits, 827 total requests
2025-12-03 14:34:29,325 - worker.extractor - ERROR - Failed to extract GMD/BTC/BUY: illegal parameter
2025-12-03 14:34:29,369 - worker.extractor - INFO - Extracted 0 offers for GMD/BTC/BUY
2025-12-03 14:34:29,370 - worker.extractor - INFO - Extracting HNL/ETH/BUY
2025-12-03 14:34:30,118 - worker.extractor - ERROR - Failed to extract GMD/BTC/SELL: illegal parameter
2025-12-03 14:34:30,148 - worker.extractor - INFO - Extracted 0 offers for GMD/BTC/SELL
2025-12-03 14:34:30,149 - worker.extractor - INFO - Extracting HNL/ETH/SELL
2025-12-03 14:34:30,787 - worker.extractor - ERROR - Failed to extract GMD/ETH/BUY: illegal parameter
2025-12-03 14:34:30,820 - worker.extractor - INFO - Extracted 0 offers for GMD/ETH/BUY
2025-12-03 14:34:30,821 - worker.extractor - INFO - Extracting HTG/USDT/BUY
2025-12-03 14:34:31,350 - worker.extractor - ERROR - Failed to extract GMD/ETH/SELL: illegal parameter
2025-12-03 14:34:31,456 - worker.extractor - INFO - Extracted 0 offers for GMD/ETH/SELL
2025-12-03 14:34:31,457 - worker.extractor - INFO - Extracting HTG/USDT/SELL
2025-12-03 14:34:32,523 - worker.extractor - ERROR - Failed to extract GNF/USDT/BUY: illegal parameter
2025-12-03 14:34:32,565 - worker.extractor - INFO - Extracted 0 offers for GNF/USDT/BUY
2025-12-03 14:34:32,566 - worker.extractor - INFO - Extracting HTG/BTC/BUY
2025-12-03 14:34:32,637 - worker.extractor - ERROR - Failed to extract GNF/USDT/SELL: illegal parameter
2025-12-03 14:34:32,655 - worker.extractor - INFO - Extracted 0 offers for GNF/USDT/SELL
2025-12-03 14:34:32,668 - worker.extractor - INFO - Extracting HTG/BTC/SELL
2025-12-03 14:34:33,232 - worker.extractor - ERROR - Failed to extract GNF/BTC/BUY: illegal parameter
2025-12-03 14:34:33,252 - worker.extractor - INFO - Extracted 0 offers for GNF/BTC/BUY
2025-12-03 14:34:33,253 - worker.extractor - INFO - Extracting HTG/ETH/BUY
2025-12-03 14:34:33,851 - worker.extractor - ERROR - Failed to extract GNF/BTC/SELL: illegal parameter
2025-12-03 14:34:33,854 - worker.extractor - INFO - Extracted 0 offers for GNF/BTC/SELL
2025-12-03 14:34:33,855 - worker.extractor - INFO - Extracting HTG/ETH/SELL
2025-12-03 14:34:34,535 - worker.extractor - ERROR - Failed to extract GNF/ETH/BUY: illegal parameter
2025-12-03 14:34:34,580 - worker.extractor - INFO - Extracted 0 offers for GNF/ETH/BUY
2025-12-03 14:34:34,581 - worker.extractor - INFO - Extracting HUF/USDT/BUY
2025-12-03 14:34:35,116 - worker.extractor - ERROR - Failed to extract GNF/ETH/SELL: illegal parameter
2025-12-03 14:34:35,124 - worker.extractor - INFO - Extracted 0 offers for GNF/ETH/SELL
2025-12-03 14:34:35,132 - worker.extractor - INFO - Extracting HUF/USDT/SELL
2025-12-03 14:34:35,470 - worker.rate_limiter - WARNING - Rate limiter active: 740 waits, 837 total requests
2025-12-03 14:34:35,764 - worker.extractor - ERROR - Failed to extract GTQ/USDT/BUY: illegal parameter
2025-12-03 14:34:35,770 - worker.extractor - INFO - Extracted 0 offers for GTQ/USDT/BUY
2025-12-03 14:34:35,771 - worker.extractor - INFO - Extracting HUF/BTC/BUY
2025-12-03 14:34:36,387 - worker.extractor - ERROR - Failed to extract GTQ/USDT/SELL: illegal parameter
2025-12-03 14:34:36,434 - worker.extractor - INFO - Extracted 0 offers for GTQ/USDT/SELL
2025-12-03 14:34:36,466 - worker.extractor - INFO - Extracting HUF/BTC/SELL
2025-12-03 14:34:37,079 - worker.extractor - ERROR - Failed to extract GTQ/BTC/BUY: illegal parameter
2025-12-03 14:34:37,104 - worker.extractor - INFO - Extracted 0 offers for GTQ/BTC/BUY
2025-12-03 14:34:37,105 - worker.extractor - INFO - Extracting HUF/ETH/BUY
2025-12-03 14:34:37,714 - worker.extractor - ERROR - Failed to extract GTQ/BTC/SELL: illegal parameter
2025-12-03 14:34:37,731 - worker.extractor - INFO - Extracted 0 offers for GTQ/BTC/SELL
2025-12-03 14:34:37,748 - worker.extractor - INFO - Extracting HUF/ETH/SELL
2025-12-03 14:34:38,350 - worker.extractor - ERROR - Failed to extract GTQ/ETH/BUY: illegal parameter
2025-12-03 14:34:38,389 - worker.extractor - INFO - Extracted 0 offers for GTQ/ETH/BUY
2025-12-03 14:34:38,400 - worker.extractor - INFO - Extracting IQD/USDT/BUY
2025-12-03 14:34:38,983 - worker.extractor - ERROR - Failed to extract GTQ/ETH/SELL: illegal parameter
2025-12-03 14:34:39,005 - worker.extractor - INFO - Extracted 0 offers for GTQ/ETH/SELL
2025-12-03 14:34:39,067 - worker.extractor - INFO - Extracting IQD/USDT/SELL
2025-12-03 14:34:39,597 - worker.extractor - ERROR - Failed to extract HNL/USDT/BUY: illegal parameter
2025-12-03 14:34:39,617 - worker.extractor - INFO - Extracted 0 offers for HNL/USDT/BUY
2025-12-03 14:34:39,637 - worker.extractor - INFO - Extracting IQD/BTC/BUY
2025-12-03 14:34:40,216 - worker.extractor - ERROR - Failed to extract HNL/USDT/SELL: illegal parameter
2025-12-03 14:34:40,237 - worker.extractor - INFO - Extracted 0 offers for HNL/USDT/SELL
2025-12-03 14:34:40,238 - worker.extractor - INFO - Extracting IQD/BTC/SELL
2025-12-03 14:34:40,866 - worker.extractor - ERROR - Failed to extract HNL/BTC/BUY: illegal parameter
2025-12-03 14:34:40,929 - worker.extractor - INFO - Extracted 0 offers for HNL/BTC/BUY
2025-12-03 14:34:40,930 - worker.extractor - INFO - Extracting IQD/ETH/BUY
2025-12-03 14:34:41,486 - worker.extractor - ERROR - Failed to extract HNL/BTC/SELL: illegal parameter
2025-12-03 14:34:41,518 - worker.extractor - INFO - Extracted 0 offers for HNL/BTC/SELL
2025-12-03 14:34:41,661 - worker.extractor - INFO - Extracting IQD/ETH/SELL
2025-12-03 14:34:41,829 - worker.rate_limiter - WARNING - Rate limiter active: 750 waits, 847 total requests
2025-12-03 14:34:42,137 - worker.extractor - ERROR - Failed to extract HNL/ETH/BUY: illegal parameter
2025-12-03 14:34:42,279 - worker.extractor - INFO - Extracted 0 offers for HNL/ETH/BUY
2025-12-03 14:34:42,794 - worker.extractor - INFO - Extracting ISK/USDT/BUY
2025-12-03 14:34:43,015 - worker.extractor - ERROR - Failed to extract HNL/ETH/SELL: illegal parameter
2025-12-03 14:34:43,183 - worker.extractor - INFO - Extracted 0 offers for HNL/ETH/SELL
2025-12-03 14:34:43,183 - worker.extractor - INFO - Extracting ISK/USDT/SELL
2025-12-03 14:34:43,706 - worker.extractor - ERROR - Failed to extract HTG/USDT/BUY: illegal parameter
2025-12-03 14:34:43,797 - worker.extractor - INFO - Extracted 0 offers for HTG/USDT/BUY
2025-12-03 14:34:44,014 - worker.extractor - INFO - Extracting ISK/BTC/BUY
2025-12-03 14:34:44,365 - worker.extractor - ERROR - Failed to extract HTG/USDT/SELL: illegal parameter
2025-12-03 14:34:44,370 - worker.extractor - INFO - Extracted 0 offers for HTG/USDT/SELL
2025-12-03 14:34:44,371 - worker.extractor - INFO - Extracting ISK/BTC/SELL
2025-12-03 14:34:44,932 - worker.extractor - ERROR - Failed to extract HTG/BTC/BUY: illegal parameter
2025-12-03 14:34:44,956 - worker.extractor - INFO - Extracted 0 offers for HTG/BTC/BUY
2025-12-03 14:34:45,105 - worker.extractor - INFO - Extracting ISK/ETH/BUY
2025-12-03 14:34:45,583 - worker.extractor - ERROR - Failed to extract HTG/BTC/SELL: illegal parameter
2025-12-03 14:34:45,636 - worker.extractor - INFO - Extracted 0 offers for HTG/BTC/SELL
2025-12-03 14:34:45,636 - worker.extractor - INFO - Extracting ISK/ETH/SELL
2025-12-03 14:34:46,230 - worker.extractor - ERROR - Failed to extract HTG/ETH/BUY: illegal parameter
2025-12-03 14:34:46,253 - worker.extractor - INFO - Extracted 0 offers for HTG/ETH/BUY
2025-12-03 14:34:46,254 - worker.extractor - INFO - Extracting JMD/USDT/BUY
2025-12-03 14:34:46,862 - worker.extractor - ERROR - Failed to extract HTG/ETH/SELL: illegal parameter
2025-12-03 14:34:46,900 - worker.extractor - INFO - Extracted 0 offers for HTG/ETH/SELL
2025-12-03 14:34:46,985 - worker.extractor - INFO - Extracting JMD/USDT/SELL
2025-12-03 14:34:47,531 - worker.extractor - ERROR - Failed to extract HUF/USDT/BUY: illegal parameter
2025-12-03 14:34:47,560 - worker.extractor - INFO - Extracted 0 offers for HUF/USDT/BUY
2025-12-03 14:34:47,560 - worker.extractor - INFO - Extracting JMD/BTC/BUY
2025-12-03 14:34:48,145 - worker.extractor - ERROR - Failed to extract HUF/USDT/SELL: illegal parameter
2025-12-03 14:34:48,162 - worker.extractor - INFO - Extracted 0 offers for HUF/USDT/SELL
2025-12-03 14:34:48,162 - worker.extractor - INFO - Extracting JMD/BTC/SELL
2025-12-03 14:34:48,505 - worker.rate_limiter - WARNING - Rate limiter active: 760 waits, 857 total requests
2025-12-03 14:34:48,812 - worker.extractor - ERROR - Failed to extract HUF/BTC/BUY: illegal parameter
2025-12-03 14:34:48,827 - worker.extractor - INFO - Extracted 0 offers for HUF/BTC/BUY
2025-12-03 14:34:48,833 - worker.extractor - INFO - Extracting JMD/ETH/BUY
2025-12-03 14:34:49,413 - worker.extractor - ERROR - Failed to extract HUF/BTC/SELL: illegal parameter
2025-12-03 14:34:49,416 - worker.extractor - INFO - Extracted 0 offers for HUF/BTC/SELL
2025-12-03 14:34:49,419 - worker.extractor - INFO - Extracting JMD/ETH/SELL
2025-12-03 14:34:50,048 - worker.extractor - ERROR - Failed to extract HUF/ETH/BUY: illegal parameter
2025-12-03 14:34:50,078 - worker.extractor - INFO - Extracted 0 offers for HUF/ETH/BUY
2025-12-03 14:34:50,147 - worker.extractor - INFO - Extracting JOD/USDT/BUY
2025-12-03 14:34:50,685 - worker.extractor - ERROR - Failed to extract HUF/ETH/SELL: illegal parameter
2025-12-03 14:34:50,709 - worker.extractor - INFO - Extracted 0 offers for HUF/ETH/SELL
2025-12-03 14:34:50,710 - worker.extractor - INFO - Extracting JOD/USDT/SELL
2025-12-03 14:34:51,283 - worker.extractor - ERROR - Failed to extract IQD/USDT/BUY: illegal parameter
2025-12-03 14:34:51,284 - worker.extractor - INFO - Extracted 0 offers for IQD/USDT/BUY
2025-12-03 14:34:51,285 - worker.extractor - INFO - Extracting JOD/BTC/BUY
2025-12-03 14:34:51,900 - worker.extractor - ERROR - Failed to extract IQD/USDT/SELL: illegal parameter
2025-12-03 14:34:51,913 - worker.extractor - INFO - Extracted 0 offers for IQD/USDT/SELL
2025-12-03 14:34:51,918 - worker.extractor - INFO - Extracting JOD/BTC/SELL
2025-12-03 14:34:52,511 - worker.extractor - ERROR - Failed to extract IQD/BTC/BUY: illegal parameter
2025-12-03 14:34:52,512 - worker.extractor - INFO - Extracted 0 offers for IQD/BTC/BUY
2025-12-03 14:34:52,512 - worker.extractor - INFO - Extracting JOD/ETH/BUY
2025-12-03 14:34:53,095 - worker.extractor - ERROR - Failed to extract IQD/BTC/SELL: illegal parameter
2025-12-03 14:34:53,098 - worker.extractor - INFO - Extracted 0 offers for IQD/BTC/SELL
2025-12-03 14:34:53,103 - worker.extractor - INFO - Extracting JOD/ETH/SELL
2025-12-03 14:34:53,728 - worker.extractor - ERROR - Failed to extract IQD/ETH/BUY: illegal parameter
2025-12-03 14:34:53,746 - worker.extractor - INFO - Extracted 0 offers for IQD/ETH/BUY
2025-12-03 14:34:53,747 - worker.extractor - INFO - Extracting KGS/USDT/BUY
2025-12-03 14:34:54,369 - worker.extractor - ERROR - Failed to extract IQD/ETH/SELL: illegal parameter
2025-12-03 14:34:54,386 - worker.extractor - INFO - Extracted 0 offers for IQD/ETH/SELL
2025-12-03 14:34:54,396 - worker.extractor - INFO - Extracting KGS/USDT/SELL
2025-12-03 14:34:54,717 - worker.rate_limiter - WARNING - Rate limiter active: 770 waits, 867 total requests
2025-12-03 14:34:55,027 - worker.extractor - ERROR - Failed to extract ISK/USDT/BUY: illegal parameter
2025-12-03 14:34:55,062 - worker.extractor - INFO - Extracted 0 offers for ISK/USDT/BUY
2025-12-03 14:34:55,080 - worker.extractor - INFO - Extracting KGS/BTC/BUY
2025-12-03 14:34:55,601 - worker.extractor - ERROR - Failed to extract ISK/USDT/SELL: illegal parameter
2025-12-03 14:34:55,611 - worker.extractor - INFO - Extracted 0 offers for ISK/USDT/SELL
2025-12-03 14:34:55,611 - worker.extractor - INFO - Extracting KGS/BTC/SELL
2025-12-03 14:34:56,227 - worker.extractor - ERROR - Failed to extract ISK/BTC/BUY: illegal parameter
2025-12-03 14:34:56,235 - worker.extractor - INFO - Extracted 0 offers for ISK/BTC/BUY
2025-12-03 14:34:56,236 - worker.extractor - INFO - Extracting KGS/ETH/BUY
2025-12-03 14:34:56,859 - worker.extractor - ERROR - Failed to extract ISK/BTC/SELL: illegal parameter
2025-12-03 14:34:56,864 - worker.extractor - INFO - Extracted 0 offers for ISK/BTC/SELL
2025-12-03 14:34:56,870 - worker.extractor - INFO - Extracting KGS/ETH/SELL
2025-12-03 14:34:57,595 - worker.extractor - ERROR - Failed to extract ISK/ETH/BUY: illegal parameter
2025-12-03 14:34:57,615 - worker.extractor - INFO - Extracted 0 offers for ISK/ETH/BUY
2025-12-03 14:34:57,643 - worker.extractor - INFO - Extracting KMF/USDT/BUY
2025-12-03 14:34:58,161 - worker.extractor - ERROR - Failed to extract ISK/ETH/SELL: illegal parameter
2025-12-03 14:34:58,179 - worker.extractor - INFO - Extracted 0 offers for ISK/ETH/SELL
2025-12-03 14:34:58,201 - worker.extractor - INFO - Extracting KMF/USDT/SELL
2025-12-03 14:34:58,740 - worker.extractor - ERROR - Failed to extract JMD/USDT/BUY: illegal parameter
2025-12-03 14:34:58,752 - worker.extractor - INFO - Extracted 0 offers for JMD/USDT/BUY
2025-12-03 14:34:58,776 - worker.extractor - INFO - Extracting KMF/BTC/BUY
2025-12-03 14:34:59,447 - worker.extractor - ERROR - Failed to extract JMD/USDT/SELL: illegal parameter
2025-12-03 14:34:59,479 - worker.extractor - INFO - Extracted 0 offers for JMD/USDT/SELL
2025-12-03 14:34:59,481 - worker.extractor - INFO - Extracting KMF/BTC/SELL
2025-12-03 14:35:00,052 - worker.extractor - ERROR - Failed to extract JMD/BTC/BUY: illegal parameter
2025-12-03 14:35:00,078 - worker.extractor - INFO - Extracted 0 offers for JMD/BTC/BUY
2025-12-03 14:35:00,081 - worker.extractor - INFO - Extracting KMF/ETH/BUY
2025-12-03 14:35:00,676 - worker.extractor - ERROR - Failed to extract JMD/BTC/SELL: illegal parameter
2025-12-03 14:35:00,678 - worker.extractor - INFO - Extracted 0 offers for JMD/BTC/SELL
2025-12-03 14:35:00,680 - worker.extractor - INFO - Extracting KMF/ETH/SELL
2025-12-03 14:35:00,884 - worker.rate_limiter - WARNING - Rate limiter active: 780 waits, 877 total requests
2025-12-03 14:35:01,162 - worker.extractor - ERROR - Failed to extract JMD/ETH/BUY: illegal parameter
2025-12-03 14:35:01,176 - worker.extractor - INFO - Extracted 0 offers for JMD/ETH/BUY
2025-12-03 14:35:01,201 - worker.extractor - INFO - Extracting KWD/USDT/BUY
2025-12-03 14:35:01,762 - worker.extractor - ERROR - Failed to extract JMD/ETH/SELL: illegal parameter
2025-12-03 14:35:01,763 - worker.extractor - INFO - Extracted 0 offers for JMD/ETH/SELL
2025-12-03 14:35:01,764 - worker.extractor - INFO - Extracting KWD/USDT/SELL
2025-12-03 14:35:02,368 - worker.extractor - ERROR - Failed to extract JOD/USDT/BUY: illegal parameter
2025-12-03 14:35:02,530 - worker.extractor - INFO - Extracted 0 offers for JOD/USDT/BUY
2025-12-03 14:35:02,625 - worker.extractor - INFO - Extracting KWD/BTC/BUY
2025-12-03 14:35:02,983 - worker.extractor - ERROR - Failed to extract JOD/USDT/SELL: illegal parameter
2025-12-03 14:35:03,100 - worker.extractor - INFO - Extracted 0 offers for JOD/USDT/SELL
2025-12-03 14:35:03,251 - worker.extractor - INFO - Extracting KWD/BTC/SELL
2025-12-03 14:35:03,629 - worker.extractor - ERROR - Failed to extract JOD/BTC/BUY: illegal parameter
2025-12-03 14:35:03,645 - worker.extractor - INFO - Extracted 0 offers for JOD/BTC/BUY
2025-12-03 14:35:03,648 - worker.extractor - INFO - Extracting KWD/ETH/BUY
2025-12-03 14:35:04,274 - worker.extractor - ERROR - Failed to extract JOD/BTC/SELL: illegal parameter
2025-12-03 14:35:04,290 - worker.extractor - INFO - Extracted 0 offers for JOD/BTC/SELL
2025-12-03 14:35:04,293 - worker.extractor - INFO - Extracting KWD/ETH/SELL
2025-12-03 14:35:04,874 - worker.extractor - ERROR - Failed to extract JOD/ETH/BUY: illegal parameter
2025-12-03 14:35:04,883 - worker.extractor - INFO - Extracted 0 offers for JOD/ETH/BUY
2025-12-03 14:35:04,911 - worker.extractor - INFO - Extracting KYD/USDT/BUY
2025-12-03 14:35:05,467 - worker.extractor - ERROR - Failed to extract JOD/ETH/SELL: illegal parameter
2025-12-03 14:35:05,472 - worker.extractor - INFO - Extracted 0 offers for JOD/ETH/SELL
2025-12-03 14:35:05,473 - worker.extractor - INFO - Extracting KYD/USDT/SELL
2025-12-03 14:35:06,085 - worker.extractor - ERROR - Failed to extract KGS/USDT/BUY: illegal parameter
2025-12-03 14:35:06,132 - worker.extractor - INFO - Extracted 0 offers for KGS/USDT/BUY
2025-12-03 14:35:06,132 - worker.extractor - INFO - Extracting KYD/BTC/BUY
2025-12-03 14:35:06,695 - worker.extractor - ERROR - Failed to extract KGS/USDT/SELL: illegal parameter
2025-12-03 14:35:06,695 - worker.extractor - INFO - Extracted 0 offers for KGS/USDT/SELL
2025-12-03 14:35:06,696 - worker.extractor - INFO - Extracting KYD/BTC/SELL
2025-12-03 14:35:07,011 - worker.rate_limiter - WARNING - Rate limiter active: 790 waits, 887 total requests
2025-12-03 14:35:07,748 - worker.extractor - ERROR - Failed to extract KGS/BTC/BUY: illegal parameter
2025-12-03 14:35:07,751 - worker.extractor - INFO - Extracted 0 offers for KGS/BTC/BUY
2025-12-03 14:35:07,760 - worker.extractor - INFO - Extracting KYD/ETH/BUY
2025-12-03 14:35:07,886 - worker.extractor - ERROR - Failed to extract KGS/BTC/SELL: illegal parameter
2025-12-03 14:35:07,907 - worker.extractor - INFO - Extracted 0 offers for KGS/BTC/SELL
2025-12-03 14:35:07,908 - worker.extractor - INFO - Extracting KYD/ETH/SELL
2025-12-03 14:35:08,528 - worker.extractor - ERROR - Failed to extract KGS/ETH/BUY: illegal parameter
2025-12-03 14:35:08,549 - worker.extractor - INFO - Extracted 0 offers for KGS/ETH/BUY
2025-12-03 14:35:08,558 - worker.extractor - INFO - Extracting LRD/USDT/BUY
2025-12-03 14:35:09,132 - worker.extractor - ERROR - Failed to extract KGS/ETH/SELL: illegal parameter
2025-12-03 14:35:09,134 - worker.extractor - INFO - Extracted 0 offers for KGS/ETH/SELL
2025-12-03 14:35:09,145 - worker.extractor - INFO - Extracting LRD/USDT/SELL
2025-12-03 14:35:09,716 - worker.extractor - ERROR - Failed to extract KMF/USDT/BUY: illegal parameter
2025-12-03 14:35:09,717 - worker.extractor - INFO - Extracted 0 offers for KMF/USDT/BUY
2025-12-03 14:35:09,717 - worker.extractor - INFO - Extracting LRD/BTC/BUY
2025-12-03 14:35:10,333 - worker.extractor - ERROR - Failed to extract KMF/USDT/SELL: illegal parameter
2025-12-03 14:35:10,334 - worker.extractor - INFO - Extracted 0 offers for KMF/USDT/SELL
2025-12-03 14:35:10,335 - worker.extractor - INFO - Extracting LRD/BTC/SELL
2025-12-03 14:35:10,939 - worker.extractor - ERROR - Failed to extract KMF/BTC/BUY: illegal parameter
2025-12-03 14:35:10,944 - worker.extractor - INFO - Extracted 0 offers for KMF/BTC/BUY
2025-12-03 14:35:10,958 - worker.extractor - INFO - Extracting LRD/ETH/BUY
2025-12-03 14:35:11,528 - worker.extractor - ERROR - Failed to extract KMF/BTC/SELL: illegal parameter
2025-12-03 14:35:11,562 - worker.extractor - INFO - Extracted 0 offers for KMF/BTC/SELL
2025-12-03 14:35:11,577 - worker.extractor - INFO - Extracting LRD/ETH/SELL
2025-12-03 14:35:12,160 - worker.extractor - ERROR - Failed to extract KMF/ETH/BUY: illegal parameter
2025-12-03 14:35:12,162 - worker.extractor - INFO - Extracted 0 offers for KMF/ETH/BUY
2025-12-03 14:35:12,164 - worker.extractor - INFO - Extracting LYD/USDT/BUY
2025-12-03 14:35:12,774 - worker.extractor - ERROR - Failed to extract KMF/ETH/SELL: illegal parameter
2025-12-03 14:35:12,777 - worker.extractor - INFO - Extracted 0 offers for KMF/ETH/SELL
2025-12-03 14:35:12,779 - worker.extractor - INFO - Extracting LYD/USDT/SELL
2025-12-03 14:35:13,093 - worker.rate_limiter - WARNING - Rate limiter active: 800 waits, 897 total requests
2025-12-03 14:35:13,365 - worker.extractor - ERROR - Failed to extract KWD/USDT/BUY: illegal parameter
2025-12-03 14:35:13,389 - worker.extractor - INFO - Extracted 0 offers for KWD/USDT/BUY
2025-12-03 14:35:13,406 - worker.extractor - INFO - Extracting LYD/BTC/BUY
2025-12-03 14:35:13,974 - worker.extractor - ERROR - Failed to extract KWD/USDT/SELL: illegal parameter
2025-12-03 14:35:14,000 - worker.extractor - INFO - Extracted 0 offers for KWD/USDT/SELL
2025-12-03 14:35:14,050 - worker.extractor - INFO - Extracting LYD/BTC/SELL
2025-12-03 14:35:14,625 - worker.extractor - ERROR - Failed to extract KWD/BTC/BUY: illegal parameter
2025-12-03 14:35:14,631 - worker.extractor - INFO - Extracted 0 offers for KWD/BTC/BUY
2025-12-03 14:35:14,642 - worker.extractor - INFO - Extracting LYD/ETH/BUY
2025-12-03 14:35:15,250 - worker.extractor - ERROR - Failed to extract KWD/BTC/SELL: illegal parameter
2025-12-03 14:35:15,276 - worker.extractor - INFO - Extracted 0 offers for KWD/BTC/SELL
2025-12-03 14:35:15,290 - worker.extractor - INFO - Extracting LYD/ETH/SELL
2025-12-03 14:35:15,927 - worker.extractor - ERROR - Failed to extract KWD/ETH/BUY: illegal parameter
2025-12-03 14:35:15,950 - worker.extractor - INFO - Extracted 0 offers for KWD/ETH/BUY
2025-12-03 14:35:15,957 - worker.extractor - INFO - Extracting MDL/USDT/BUY
2025-12-03 14:35:16,465 - worker.extractor - ERROR - Failed to extract KWD/ETH/SELL: illegal parameter
2025-12-03 14:35:16,466 - worker.extractor - INFO - Extracted 0 offers for KWD/ETH/SELL
2025-12-03 14:35:16,466 - worker.extractor - INFO - Extracting MDL/USDT/SELL
2025-12-03 14:35:17,061 - worker.extractor - ERROR - Failed to extract KYD/USDT/BUY: illegal parameter
2025-12-03 14:35:17,073 - worker.extractor - INFO - Extracted 0 offers for KYD/USDT/BUY
2025-12-03 14:35:17,074 - worker.extractor - INFO - Extracting MDL/BTC/BUY
2025-12-03 14:35:17,699 - worker.extractor - ERROR - Failed to extract KYD/USDT/SELL: illegal parameter
2025-12-03 14:35:17,700 - worker.extractor - INFO - Extracted 0 offers for KYD/USDT/SELL
2025-12-03 14:35:17,706 - worker.extractor - INFO - Extracting MDL/BTC/SELL
2025-12-03 14:35:18,291 - worker.extractor - ERROR - Failed to extract KYD/BTC/BUY: illegal parameter
2025-12-03 14:35:18,315 - worker.extractor - INFO - Extracted 0 offers for KYD/BTC/BUY
2025-12-03 14:35:18,316 - worker.extractor - INFO - Extracting MDL/ETH/BUY
2025-12-03 14:35:18,932 - worker.extractor - ERROR - Failed to extract KYD/BTC/SELL: illegal parameter
2025-12-03 14:35:18,948 - worker.extractor - INFO - Extracted 0 offers for KYD/BTC/SELL
2025-12-03 14:35:18,949 - worker.extractor - INFO - Extracting MDL/ETH/SELL
2025-12-03 14:35:19,212 - worker.rate_limiter - WARNING - Rate limiter active: 810 waits, 907 total requests
2025-12-03 14:35:19,921 - worker.extractor - ERROR - Failed to extract KYD/ETH/BUY: illegal parameter
2025-12-03 14:35:19,931 - worker.extractor - INFO - Extracted 0 offers for KYD/ETH/BUY
2025-12-03 14:35:19,940 - worker.extractor - INFO - Extracting MGA/USDT/BUY
2025-12-03 14:35:20,120 - worker.extractor - ERROR - Failed to extract KYD/ETH/SELL: illegal parameter
2025-12-03 14:35:20,124 - worker.extractor - INFO - Extracted 0 offers for KYD/ETH/SELL
2025-12-03 14:35:20,125 - worker.extractor - INFO - Extracting MGA/USDT/SELL
2025-12-03 14:35:20,743 - worker.extractor - ERROR - Failed to extract LRD/USDT/BUY: illegal parameter
2025-12-03 14:35:20,748 - worker.extractor - INFO - Extracted 0 offers for LRD/USDT/BUY
2025-12-03 14:35:20,758 - worker.extractor - INFO - Extracting MGA/BTC/BUY
2025-12-03 14:35:21,333 - worker.extractor - ERROR - Failed to extract LRD/USDT/SELL: illegal parameter
2025-12-03 14:35:21,339 - worker.extractor - INFO - Extracted 0 offers for LRD/USDT/SELL
2025-12-03 14:35:21,340 - worker.extractor - INFO - Extracting MGA/BTC/SELL
2025-12-03 14:35:21,938 - worker.extractor - ERROR - Failed to extract LRD/BTC/BUY: illegal parameter
2025-12-03 14:35:21,944 - worker.extractor - INFO - Extracted 0 offers for LRD/BTC/BUY
2025-12-03 14:35:21,944 - worker.extractor - INFO - Extracting MGA/ETH/BUY
2025-12-03 14:35:22,532 - worker.extractor - ERROR - Failed to extract LRD/BTC/SELL: illegal parameter
2025-12-03 14:35:22,532 - worker.extractor - INFO - Extracted 0 offers for LRD/BTC/SELL
2025-12-03 14:35:22,537 - worker.extractor - INFO - Extracting MGA/ETH/SELL
2025-12-03 14:35:23,137 - worker.extractor - ERROR - Failed to extract LRD/ETH/BUY: illegal parameter
2025-12-03 14:35:23,140 - worker.extractor - INFO - Extracted 0 offers for LRD/ETH/BUY
2025-12-03 14:35:23,144 - worker.extractor - INFO - Extracting MKD/USDT/BUY
2025-12-03 14:35:23,740 - worker.extractor - ERROR - Failed to extract LRD/ETH/SELL: illegal parameter
2025-12-03 14:35:23,748 - worker.extractor - INFO - Extracted 0 offers for LRD/ETH/SELL
2025-12-03 14:35:23,748 - worker.extractor - INFO - Extracting MKD/USDT/SELL
2025-12-03 14:35:24,379 - worker.extractor - ERROR - Failed to extract LYD/USDT/BUY: illegal parameter
2025-12-03 14:35:24,380 - worker.extractor - INFO - Extracted 0 offers for LYD/USDT/BUY
2025-12-03 14:35:24,381 - worker.extractor - INFO - Extracting MKD/BTC/BUY
2025-12-03 14:35:24,988 - worker.extractor - ERROR - Failed to extract LYD/USDT/SELL: illegal parameter
2025-12-03 14:35:24,991 - worker.extractor - INFO - Extracted 0 offers for LYD/USDT/SELL
2025-12-03 14:35:24,992 - worker.extractor - INFO - Extracting MKD/BTC/SELL
2025-12-03 14:35:25,313 - worker.rate_limiter - WARNING - Rate limiter active: 820 waits, 917 total requests
2025-12-03 14:35:25,570 - worker.extractor - ERROR - Failed to extract LYD/BTC/BUY: illegal parameter
2025-12-03 14:35:25,571 - worker.extractor - INFO - Extracted 0 offers for LYD/BTC/BUY
2025-12-03 14:35:25,571 - worker.extractor - INFO - Extracting MKD/ETH/BUY
2025-12-03 14:35:26,209 - worker.extractor - ERROR - Failed to extract LYD/BTC/SELL: illegal parameter
2025-12-03 14:35:26,212 - worker.extractor - INFO - Extracted 0 offers for LYD/BTC/SELL
2025-12-03 14:35:26,214 - worker.extractor - INFO - Extracting MKD/ETH/SELL
2025-12-03 14:35:26,808 - worker.extractor - ERROR - Failed to extract LYD/ETH/BUY: illegal parameter
2025-12-03 14:35:26,827 - worker.extractor - INFO - Extracted 0 offers for LYD/ETH/BUY
2025-12-03 14:35:26,828 - worker.extractor - INFO - Extracting MOP/USDT/BUY
2025-12-03 14:35:27,538 - worker.extractor - ERROR - Failed to extract LYD/ETH/SELL: illegal parameter
2025-12-03 14:35:27,561 - worker.extractor - INFO - Extracted 0 offers for LYD/ETH/SELL
2025-12-03 14:35:27,668 - worker.extractor - INFO - Extracting MOP/USDT/SELL
2025-12-03 14:35:28,607 - worker.extractor - ERROR - Failed to extract MDL/USDT/BUY: illegal parameter
2025-12-03 14:35:28,645 - worker.extractor - INFO - Extracted 0 offers for MDL/USDT/BUY
2025-12-03 14:35:28,645 - worker.extractor - INFO - Extracting MOP/BTC/BUY
2025-12-03 14:35:28,907 - worker.extractor - ERROR - Failed to extract MDL/USDT/SELL: illegal parameter
2025-12-03 14:35:28,959 - worker.extractor - INFO - Extracted 0 offers for MDL/USDT/SELL
2025-12-03 14:35:28,980 - worker.extractor - INFO - Extracting MOP/BTC/SELL
2025-12-03 14:35:29,383 - worker.extractor - ERROR - Failed to extract MDL/BTC/BUY: illegal parameter
2025-12-03 14:35:29,387 - worker.extractor - INFO - Extracted 0 offers for MDL/BTC/BUY
2025-12-03 14:35:29,388 - worker.extractor - INFO - Extracting MOP/ETH/BUY
2025-12-03 14:35:29,995 - worker.extractor - ERROR - Failed to extract MDL/BTC/SELL: illegal parameter
2025-12-03 14:35:29,995 - worker.extractor - INFO - Extracted 0 offers for MDL/BTC/SELL
2025-12-03 14:35:29,996 - worker.extractor - INFO - Extracting MOP/ETH/SELL
2025-12-03 14:35:30,671 - worker.extractor - ERROR - Failed to extract MDL/ETH/BUY: illegal parameter
2025-12-03 14:35:30,672 - worker.extractor - INFO - Extracted 0 offers for MDL/ETH/BUY
2025-12-03 14:35:30,672 - worker.extractor - INFO - Extracting MRU/USDT/BUY
2025-12-03 14:35:31,191 - worker.extractor - ERROR - Failed to extract MDL/ETH/SELL: illegal parameter
2025-12-03 14:35:31,210 - worker.extractor - INFO - Extracted 0 offers for MDL/ETH/SELL
2025-12-03 14:35:31,210 - worker.extractor - INFO - Extracting MRU/USDT/SELL
2025-12-03 14:35:31,537 - worker.rate_limiter - WARNING - Rate limiter active: 830 waits, 927 total requests
2025-12-03 14:35:31,852 - worker.extractor - ERROR - Failed to extract MGA/USDT/BUY: illegal parameter
2025-12-03 14:35:31,888 - worker.extractor - INFO - Extracted 0 offers for MGA/USDT/BUY
2025-12-03 14:35:31,889 - worker.extractor - INFO - Extracting MRU/BTC/BUY
2025-12-03 14:35:32,493 - worker.extractor - ERROR - Failed to extract MGA/USDT/SELL: illegal parameter
2025-12-03 14:35:32,509 - worker.extractor - INFO - Extracted 0 offers for MGA/USDT/SELL
2025-12-03 14:35:32,510 - worker.extractor - INFO - Extracting MRU/BTC/SELL
2025-12-03 14:35:33,102 - worker.extractor - ERROR - Failed to extract MGA/BTC/BUY: illegal parameter
2025-12-03 14:35:33,162 - worker.extractor - INFO - Extracted 0 offers for MGA/BTC/BUY
2025-12-03 14:35:33,169 - worker.extractor - INFO - Extracting MRU/ETH/BUY
2025-12-03 14:35:33,748 - worker.extractor - ERROR - Failed to extract MGA/BTC/SELL: illegal parameter
2025-12-03 14:35:33,769 - worker.extractor - INFO - Extracted 0 offers for MGA/BTC/SELL
2025-12-03 14:35:33,795 - worker.extractor - INFO - Extracting MRU/ETH/SELL
2025-12-03 14:35:34,419 - worker.extractor - ERROR - Failed to extract MGA/ETH/BUY: illegal parameter
2025-12-03 14:35:34,438 - worker.extractor - INFO - Extracted 0 offers for MGA/ETH/BUY
2025-12-03 14:35:34,452 - worker.extractor - INFO - Extracting MWK/USDT/BUY
2025-12-03 14:35:35,055 - worker.extractor - ERROR - Failed to extract MGA/ETH/SELL: illegal parameter
2025-12-03 14:35:35,055 - worker.extractor - INFO - Extracted 0 offers for MGA/ETH/SELL
2025-12-03 14:35:35,056 - worker.extractor - INFO - Extracting MWK/USDT/SELL
2025-12-03 14:35:35,592 - worker.extractor - ERROR - Failed to extract MKD/USDT/BUY: illegal parameter
2025-12-03 14:35:35,599 - worker.extractor - INFO - Extracted 0 offers for MKD/USDT/BUY
2025-12-03 14:35:35,605 - worker.extractor - INFO - Extracting MWK/BTC/BUY
2025-12-03 14:35:36,593 - worker.extractor - ERROR - Failed to extract MKD/USDT/SELL: illegal parameter
2025-12-03 14:35:36,620 - worker.extractor - INFO - Extracted 0 offers for MKD/USDT/SELL
2025-12-03 14:35:36,621 - worker.extractor - INFO - Extracting MWK/BTC/SELL
2025-12-03 14:35:36,810 - worker.extractor - ERROR - Failed to extract MKD/BTC/BUY: illegal parameter
2025-12-03 14:35:36,812 - worker.extractor - INFO - Extracted 0 offers for MKD/BTC/BUY
2025-12-03 14:35:36,827 - worker.extractor - INFO - Extracting MWK/ETH/BUY
2025-12-03 14:35:37,404 - worker.extractor - ERROR - Failed to extract MKD/BTC/SELL: illegal parameter
2025-12-03 14:35:37,409 - worker.extractor - INFO - Extracted 0 offers for MKD/BTC/SELL
2025-12-03 14:35:37,422 - worker.extractor - INFO - Extracting MWK/ETH/SELL
2025-12-03 14:35:37,733 - worker.rate_limiter - WARNING - Rate limiter active: 840 waits, 937 total requests
2025-12-03 14:35:38,006 - worker.extractor - ERROR - Failed to extract MKD/ETH/BUY: illegal parameter
2025-12-03 14:35:38,008 - worker.extractor - INFO - Extracted 0 offers for MKD/ETH/BUY
2025-12-03 14:35:38,009 - worker.extractor - INFO - Extracting MZN/USDT/BUY
2025-12-03 14:35:38,596 - worker.extractor - ERROR - Failed to extract MKD/ETH/SELL: illegal parameter
2025-12-03 14:35:38,622 - worker.extractor - INFO - Extracted 0 offers for MKD/ETH/SELL
2025-12-03 14:35:38,623 - worker.extractor - INFO - Extracting MZN/USDT/SELL
2025-12-03 14:35:39,251 - worker.extractor - ERROR - Failed to extract MOP/USDT/BUY: illegal parameter
2025-12-03 14:35:39,277 - worker.extractor - INFO - Extracted 0 offers for MOP/USDT/BUY
2025-12-03 14:35:39,284 - worker.extractor - INFO - Extracting MZN/BTC/BUY
2025-12-03 14:35:39,867 - worker.extractor - ERROR - Failed to extract MOP/USDT/SELL: illegal parameter
2025-12-03 14:35:39,902 - worker.extractor - INFO - Extracted 0 offers for MOP/USDT/SELL
2025-12-03 14:35:39,917 - worker.extractor - INFO - Extracting MZN/BTC/SELL
2025-12-03 14:35:40,509 - worker.extractor - ERROR - Failed to extract MOP/BTC/BUY: illegal parameter
2025-12-03 14:35:40,555 - worker.extractor - INFO - Extracted 0 offers for MOP/BTC/BUY
2025-12-03 14:35:40,555 - worker.extractor - INFO - Extracting MZN/ETH/BUY
2025-12-03 14:35:41,219 - worker.extractor - ERROR - Failed to extract MOP/BTC/SELL: illegal parameter
2025-12-03 14:35:41,244 - worker.extractor - INFO - Extracted 0 offers for MOP/BTC/SELL
2025-12-03 14:35:41,290 - worker.extractor - INFO - Extracting MZN/ETH/SELL
2025-12-03 14:35:41,839 - worker.extractor - ERROR - Failed to extract MOP/ETH/BUY: illegal parameter
2025-12-03 14:35:41,908 - worker.extractor - INFO - Extracted 0 offers for MOP/ETH/BUY
2025-12-03 14:35:42,040 - worker.extractor - INFO - Extracting NAD/USDT/BUY
2025-12-03 14:35:42,542 - worker.extractor - ERROR - Failed to extract MOP/ETH/SELL: illegal parameter
2025-12-03 14:35:42,558 - worker.extractor - INFO - Extracted 0 offers for MOP/ETH/SELL
2025-12-03 14:35:42,575 - worker.extractor - INFO - Extracting NAD/USDT/SELL
2025-12-03 14:35:43,187 - worker.extractor - ERROR - Failed to extract MRU/USDT/BUY: illegal parameter
2025-12-03 14:35:43,189 - worker.extractor - INFO - Extracted 0 offers for MRU/USDT/BUY
2025-12-03 14:35:43,191 - worker.extractor - INFO - Extracting NAD/BTC/BUY
2025-12-03 14:35:43,782 - worker.extractor - ERROR - Failed to extract MRU/USDT/SELL: illegal parameter
2025-12-03 14:35:43,798 - worker.extractor - INFO - Extracted 0 offers for MRU/USDT/SELL
2025-12-03 14:35:43,799 - worker.extractor - INFO - Extracting NAD/BTC/SELL
2025-12-03 14:35:44,175 - worker.rate_limiter - WARNING - Rate limiter active: 850 waits, 947 total requests
2025-12-03 14:35:44,553 - worker.extractor - ERROR - Failed to extract MRU/BTC/BUY: illegal parameter
2025-12-03 14:35:44,585 - worker.extractor - INFO - Extracted 0 offers for MRU/BTC/BUY
2025-12-03 14:35:44,586 - worker.extractor - INFO - Extracting NAD/ETH/BUY
2025-12-03 14:35:45,403 - worker.extractor - ERROR - Failed to extract MRU/BTC/SELL: illegal parameter
2025-12-03 14:35:45,488 - worker.extractor - INFO - Extracted 0 offers for MRU/BTC/SELL
2025-12-03 14:35:45,489 - worker.extractor - INFO - Extracting NAD/ETH/SELL
2025-12-03 14:35:46,283 - worker.extractor - ERROR - Failed to extract MRU/ETH/BUY: illegal parameter
2025-12-03 14:35:46,467 - worker.extractor - INFO - Extracted 0 offers for MRU/ETH/BUY
2025-12-03 14:35:46,468 - worker.extractor - INFO - Extracting NIO/USDT/BUY
2025-12-03 14:35:47,202 - worker.extractor - ERROR - Failed to extract MRU/ETH/SELL: illegal parameter
2025-12-03 14:35:47,435 - worker.extractor - INFO - Extracted 0 offers for MRU/ETH/SELL
2025-12-03 14:35:47,703 - worker.extractor - INFO - Extracting NIO/USDT/SELL
2025-12-03 14:35:47,921 - worker.extractor - ERROR - Failed to extract MWK/USDT/BUY: illegal parameter
2025-12-03 14:35:48,010 - worker.extractor - INFO - Extracted 0 offers for MWK/USDT/BUY
2025-12-03 14:35:48,185 - worker.extractor - INFO - Extracting NIO/BTC/BUY
2025-12-03 14:35:48,591 - worker.extractor - ERROR - Failed to extract MWK/USDT/SELL: illegal parameter
2025-12-03 14:35:48,721 - worker.extractor - INFO - Extracted 0 offers for MWK/USDT/SELL
2025-12-03 14:35:48,724 - worker.extractor - INFO - Extracting NIO/BTC/SELL
2025-12-03 14:35:49,373 - worker.extractor - ERROR - Failed to extract MWK/BTC/BUY: illegal parameter
2025-12-03 14:35:49,487 - worker.extractor - INFO - Extracted 0 offers for MWK/BTC/BUY
2025-12-03 14:35:49,621 - worker.extractor - INFO - Extracting NIO/ETH/BUY
2025-12-03 14:35:50,037 - worker.extractor - ERROR - Failed to extract MWK/BTC/SELL: illegal parameter
2025-12-03 14:35:50,067 - worker.extractor - INFO - Extracted 0 offers for MWK/BTC/SELL
2025-12-03 14:35:50,152 - worker.extractor - INFO - Extracting NIO/ETH/SELL
2025-12-03 14:35:50,838 - worker.extractor - ERROR - Failed to extract MWK/ETH/BUY: illegal parameter
2025-12-03 14:35:51,065 - worker.extractor - INFO - Extracted 0 offers for MWK/ETH/BUY
2025-12-03 14:35:51,066 - worker.extractor - INFO - Extracting NOK/USDT/BUY
2025-12-03 14:35:51,433 - worker.extractor - ERROR - Failed to extract MWK/ETH/SELL: illegal parameter
2025-12-03 14:35:51,486 - worker.extractor - INFO - Extracted 0 offers for MWK/ETH/SELL
2025-12-03 14:35:51,487 - worker.extractor - INFO - Extracting NOK/USDT/SELL
2025-12-03 14:35:51,835 - worker.rate_limiter - WARNING - Rate limiter active: 860 waits, 957 total requests
2025-12-03 14:35:52,252 - worker.extractor - ERROR - Failed to extract MZN/USDT/BUY: illegal parameter
2025-12-03 14:35:52,270 - worker.extractor - INFO - Extracted 0 offers for MZN/USDT/BUY
2025-12-03 14:35:52,298 - worker.extractor - INFO - Extracting NOK/BTC/BUY
2025-12-03 14:35:52,734 - worker.extractor - ERROR - Failed to extract MZN/USDT/SELL: illegal parameter
2025-12-03 14:35:52,789 - worker.extractor - INFO - Extracted 0 offers for MZN/USDT/SELL
2025-12-03 14:35:52,798 - worker.extractor - INFO - Extracting NOK/BTC/SELL
2025-12-03 14:35:53,365 - worker.extractor - ERROR - Failed to extract MZN/BTC/BUY: illegal parameter
2025-12-03 14:35:53,401 - worker.extractor - INFO - Extracted 0 offers for MZN/BTC/BUY
2025-12-03 14:35:53,486 - worker.extractor - INFO - Extracting NOK/ETH/BUY
2025-12-03 14:35:54,015 - worker.extractor - ERROR - Failed to extract MZN/BTC/SELL: illegal parameter
2025-12-03 14:35:54,037 - worker.extractor - INFO - Extracted 0 offers for MZN/BTC/SELL
2025-12-03 14:35:54,038 - worker.extractor - INFO - Extracting NOK/ETH/SELL
2025-12-03 14:35:54,656 - worker.extractor - ERROR - Failed to extract MZN/ETH/BUY: illegal parameter
2025-12-03 14:35:54,700 - worker.extractor - INFO - Extracted 0 offers for MZN/ETH/BUY
2025-12-03 14:35:54,701 - worker.extractor - INFO - Extracting PGK/USDT/BUY
2025-12-03 14:35:55,349 - worker.extractor - ERROR - Failed to extract MZN/ETH/SELL: illegal parameter
2025-12-03 14:35:55,488 - worker.extractor - INFO - Extracted 0 offers for MZN/ETH/SELL
2025-12-03 14:35:55,739 - worker.extractor - INFO - Extracting PGK/USDT/SELL
2025-12-03 14:35:56,432 - worker.extractor - ERROR - Failed to extract NAD/USDT/BUY: illegal parameter
2025-12-03 14:35:56,434 - worker.extractor - INFO - Extracted 0 offers for NAD/USDT/BUY
2025-12-03 14:35:56,436 - worker.extractor - INFO - Extracting PGK/BTC/BUY
2025-12-03 14:35:56,593 - worker.extractor - ERROR - Failed to extract NAD/USDT/SELL: illegal parameter
2025-12-03 14:35:56,598 - worker.extractor - INFO - Extracted 0 offers for NAD/USDT/SELL
2025-12-03 14:35:56,599 - worker.extractor - INFO - Extracting PGK/BTC/SELL
2025-12-03 14:35:57,221 - worker.extractor - ERROR - Failed to extract NAD/BTC/BUY: illegal parameter
2025-12-03 14:35:57,248 - worker.extractor - INFO - Extracted 0 offers for NAD/BTC/BUY
2025-12-03 14:35:57,249 - worker.extractor - INFO - Extracting PGK/ETH/BUY
2025-12-03 14:35:57,803 - worker.extractor - ERROR - Failed to extract NAD/BTC/SELL: illegal parameter
2025-12-03 14:35:57,808 - worker.extractor - INFO - Extracted 0 offers for NAD/BTC/SELL
2025-12-03 14:35:57,817 - worker.extractor - INFO - Extracting PGK/ETH/SELL
2025-12-03 14:35:58,122 - worker.rate_limiter - WARNING - Rate limiter active: 870 waits, 967 total requests
2025-12-03 14:35:58,447 - worker.extractor - ERROR - Failed to extract NAD/ETH/BUY: illegal parameter
2025-12-03 14:35:58,449 - worker.extractor - INFO - Extracted 0 offers for NAD/ETH/BUY
2025-12-03 14:35:58,449 - worker.extractor - INFO - Extracting RSD/USDT/BUY
2025-12-03 14:35:59,044 - worker.extractor - ERROR - Failed to extract NAD/ETH/SELL: illegal parameter
2025-12-03 14:35:59,151 - worker.extractor - INFO - Extracted 0 offers for NAD/ETH/SELL
2025-12-03 14:35:59,152 - worker.extractor - INFO - Extracting RSD/USDT/SELL
2025-12-03 14:35:59,709 - worker.extractor - ERROR - Failed to extract NIO/USDT/BUY: illegal parameter
2025-12-03 14:35:59,788 - worker.extractor - INFO - Extracted 0 offers for NIO/USDT/BUY
2025-12-03 14:35:59,980 - worker.extractor - INFO - Extracting RSD/BTC/BUY
2025-12-03 14:36:00,421 - worker.extractor - ERROR - Failed to extract NIO/USDT/SELL: illegal parameter
2025-12-03 14:36:00,498 - worker.extractor - INFO - Extracted 0 offers for NIO/USDT/SELL
2025-12-03 14:36:00,499 - worker.extractor - INFO - Extracting RSD/BTC/SELL
2025-12-03 14:36:01,036 - worker.extractor - ERROR - Failed to extract NIO/BTC/BUY: illegal parameter
2025-12-03 14:36:01,053 - worker.extractor - INFO - Extracted 0 offers for NIO/BTC/BUY
2025-12-03 14:36:01,054 - worker.extractor - INFO - Extracting RSD/ETH/BUY
2025-12-03 14:36:01,632 - worker.extractor - ERROR - Failed to extract NIO/BTC/SELL: illegal parameter
2025-12-03 14:36:01,634 - worker.extractor - INFO - Extracted 0 offers for NIO/BTC/SELL
2025-12-03 14:36:01,635 - worker.extractor - INFO - Extracting RSD/ETH/SELL
2025-12-03 14:36:02,231 - worker.extractor - ERROR - Failed to extract NIO/ETH/BUY: illegal parameter
2025-12-03 14:36:02,231 - worker.extractor - INFO - Extracted 0 offers for NIO/ETH/BUY
2025-12-03 14:36:02,232 - worker.extractor - INFO - Extracting SCR/USDT/BUY
2025-12-03 14:36:02,837 - worker.extractor - ERROR - Failed to extract NIO/ETH/SELL: illegal parameter
2025-12-03 14:36:02,838 - worker.extractor - INFO - Extracted 0 offers for NIO/ETH/SELL
2025-12-03 14:36:02,839 - worker.extractor - INFO - Extracting SCR/USDT/SELL
2025-12-03 14:36:03,431 - worker.extractor - ERROR - Failed to extract NOK/USDT/BUY: illegal parameter
2025-12-03 14:36:03,447 - worker.extractor - INFO - Extracted 0 offers for NOK/USDT/BUY
2025-12-03 14:36:03,467 - worker.extractor - INFO - Extracting SCR/BTC/BUY
2025-12-03 14:36:04,074 - worker.extractor - ERROR - Failed to extract NOK/USDT/SELL: illegal parameter
2025-12-03 14:36:04,081 - worker.extractor - INFO - Extracted 0 offers for NOK/USDT/SELL
2025-12-03 14:36:04,084 - worker.extractor - INFO - Extracting SCR/BTC/SELL
2025-12-03 14:36:04,368 - worker.rate_limiter - WARNING - Rate limiter active: 880 waits, 977 total requests
2025-12-03 14:36:04,636 - worker.extractor - ERROR - Failed to extract NOK/BTC/BUY: illegal parameter
2025-12-03 14:36:04,637 - worker.extractor - INFO - Extracted 0 offers for NOK/BTC/BUY
2025-12-03 14:36:04,637 - worker.extractor - INFO - Extracting SCR/ETH/BUY
2025-12-03 14:36:05,272 - worker.extractor - ERROR - Failed to extract NOK/BTC/SELL: illegal parameter
2025-12-03 14:36:05,297 - worker.extractor - INFO - Extracted 0 offers for NOK/BTC/SELL
2025-12-03 14:36:05,307 - worker.extractor - INFO - Extracting SCR/ETH/SELL
2025-12-03 14:36:05,970 - worker.extractor - ERROR - Failed to extract NOK/ETH/BUY: illegal parameter
2025-12-03 14:36:05,971 - worker.extractor - INFO - Extracted 0 offers for NOK/ETH/BUY
2025-12-03 14:36:05,972 - worker.extractor - INFO - Extracting SLE/USDT/BUY
2025-12-03 14:36:06,489 - worker.extractor - ERROR - Failed to extract NOK/ETH/SELL: illegal parameter
2025-12-03 14:36:06,688 - worker.extractor - INFO - Extracted 0 offers for NOK/ETH/SELL
2025-12-03 14:36:06,689 - worker.extractor - INFO - Extracting SLE/USDT/SELL
2025-12-03 14:36:07,254 - worker.extractor - ERROR - Failed to extract PGK/USDT/BUY: illegal parameter
2025-12-03 14:36:07,314 - worker.extractor - INFO - Extracted 0 offers for PGK/USDT/BUY
2025-12-03 14:36:07,319 - worker.extractor - INFO - Extracting SLE/BTC/BUY
2025-12-03 14:36:07,808 - worker.extractor - ERROR - Failed to extract PGK/USDT/SELL: illegal parameter
2025-12-03 14:36:07,818 - worker.extractor - INFO - Extracted 0 offers for PGK/USDT/SELL
2025-12-03 14:36:07,831 - worker.extractor - INFO - Extracting SLE/BTC/SELL
2025-12-03 14:36:08,437 - worker.extractor - ERROR - Failed to extract PGK/BTC/BUY: illegal parameter
2025-12-03 14:36:08,480 - worker.extractor - INFO - Extracted 0 offers for PGK/BTC/BUY
2025-12-03 14:36:08,484 - worker.extractor - INFO - Extracting SLE/ETH/BUY
2025-12-03 14:36:09,008 - worker.extractor - ERROR - Failed to extract PGK/BTC/SELL: illegal parameter
2025-12-03 14:36:09,012 - worker.extractor - INFO - Extracted 0 offers for PGK/BTC/SELL
2025-12-03 14:36:09,021 - worker.extractor - INFO - Extracting SLE/ETH/SELL
2025-12-03 14:36:09,619 - worker.extractor - ERROR - Failed to extract PGK/ETH/BUY: illegal parameter
2025-12-03 14:36:09,669 - worker.extractor - INFO - Extracted 0 offers for PGK/ETH/BUY
2025-12-03 14:36:09,693 - worker.extractor - INFO - Extracting SOS/USDT/BUY
2025-12-03 14:36:10,264 - worker.extractor - ERROR - Failed to extract PGK/ETH/SELL: illegal parameter
2025-12-03 14:36:10,269 - worker.extractor - INFO - Extracted 0 offers for PGK/ETH/SELL
2025-12-03 14:36:10,278 - worker.extractor - INFO - Extracting SOS/USDT/SELL
2025-12-03 14:36:10,610 - worker.rate_limiter - WARNING - Rate limiter active: 890 waits, 987 total requests
2025-12-03 14:36:10,902 - worker.extractor - ERROR - Failed to extract RSD/USDT/BUY: illegal parameter
2025-12-03 14:36:10,937 - worker.extractor - INFO - Extracted 0 offers for RSD/USDT/BUY
2025-12-03 14:36:10,938 - worker.extractor - INFO - Extracting SOS/BTC/BUY
2025-12-03 14:36:11,561 - worker.extractor - ERROR - Failed to extract RSD/USDT/SELL: illegal parameter
2025-12-03 14:36:11,672 - worker.extractor - INFO - Extracted 0 offers for RSD/USDT/SELL
2025-12-03 14:36:11,675 - worker.extractor - INFO - Extracting SOS/BTC/SELL
2025-12-03 14:36:12,365 - worker.extractor - ERROR - Failed to extract RSD/BTC/BUY: illegal parameter
2025-12-03 14:36:12,385 - worker.extractor - INFO - Extracted 0 offers for RSD/BTC/BUY
2025-12-03 14:36:12,387 - worker.extractor - INFO - Extracting SOS/ETH/BUY
2025-12-03 14:36:12,913 - worker.extractor - ERROR - Failed to extract RSD/BTC/SELL: illegal parameter
2025-12-03 14:36:12,970 - worker.extractor - INFO - Extracted 0 offers for RSD/BTC/SELL
2025-12-03 14:36:13,168 - worker.extractor - INFO - Extracting SOS/ETH/SELL
2025-12-03 14:36:13,562 - worker.extractor - ERROR - Failed to extract RSD/ETH/BUY: illegal parameter
2025-12-03 14:36:13,569 - worker.extractor - INFO - Extracted 0 offers for RSD/ETH/BUY
2025-12-03 14:36:13,579 - worker.extractor - INFO - Extracting SYP/USDT/BUY
2025-12-03 14:36:14,396 - worker.extractor - ERROR - Failed to extract RSD/ETH/SELL: illegal parameter
2025-12-03 14:36:14,398 - worker.extractor - INFO - Extracted 0 offers for RSD/ETH/SELL
2025-12-03 14:36:14,401 - worker.extractor - INFO - Extracting SYP/USDT/SELL
2025-12-03 14:36:14,976 - worker.extractor - ERROR - Failed to extract SCR/USDT/BUY: illegal parameter
2025-12-03 14:36:14,986 - worker.extractor - INFO - Extracted 0 offers for SCR/USDT/BUY
2025-12-03 14:36:14,995 - worker.extractor - INFO - Extracting SYP/BTC/BUY
2025-12-03 14:36:15,572 - worker.extractor - ERROR - Failed to extract SCR/USDT/SELL: illegal parameter
2025-12-03 14:36:15,580 - worker.extractor - INFO - Extracted 0 offers for SCR/USDT/SELL
2025-12-03 14:36:15,580 - worker.extractor - INFO - Extracting SYP/BTC/SELL
2025-12-03 14:36:16,202 - worker.extractor - ERROR - Failed to extract SCR/BTC/BUY: illegal parameter
2025-12-03 14:36:16,243 - worker.extractor - INFO - Extracted 0 offers for SCR/BTC/BUY
2025-12-03 14:36:16,252 - worker.extractor - INFO - Extracting SYP/ETH/BUY
2025-12-03 14:36:16,802 - worker.extractor - ERROR - Failed to extract SCR/BTC/SELL: illegal parameter
2025-12-03 14:36:16,814 - worker.extractor - INFO - Extracted 0 offers for SCR/BTC/SELL
2025-12-03 14:36:16,815 - worker.extractor - INFO - Extracting SYP/ETH/SELL
2025-12-03 14:36:17,138 - worker.rate_limiter - WARNING - Rate limiter active: 900 waits, 997 total requests
2025-12-03 14:36:17,429 - worker.extractor - ERROR - Failed to extract SCR/ETH/BUY: illegal parameter
2025-12-03 14:36:17,429 - worker.extractor - INFO - Extracted 0 offers for SCR/ETH/BUY
2025-12-03 14:36:17,430 - worker.extractor - INFO - Extracting TJS/USDT/BUY
2025-12-03 14:36:18,078 - worker.extractor - ERROR - Failed to extract SCR/ETH/SELL: illegal parameter
2025-12-03 14:36:18,095 - worker.extractor - INFO - Extracted 0 offers for SCR/ETH/SELL
2025-12-03 14:36:18,100 - worker.extractor - INFO - Extracting TJS/USDT/SELL
2025-12-03 14:36:19,182 - worker.extractor - ERROR - Failed to extract SLE/USDT/BUY: illegal parameter
2025-12-03 14:36:19,200 - worker.extractor - INFO - Extracted 0 offers for SLE/USDT/BUY
2025-12-03 14:36:19,200 - worker.extractor - INFO - Extracting TJS/BTC/BUY
2025-12-03 14:36:19,289 - worker.extractor - ERROR - Failed to extract SLE/USDT/SELL: illegal parameter
2025-12-03 14:36:19,331 - worker.extractor - INFO - Extracted 0 offers for SLE/USDT/SELL
2025-12-03 14:36:19,347 - worker.extractor - INFO - Extracting TJS/BTC/SELL
2025-12-03 14:36:19,963 - worker.extractor - ERROR - Failed to extract SLE/BTC/BUY: illegal parameter
2025-12-03 14:36:20,018 - worker.extractor - INFO - Extracted 0 offers for SLE/BTC/BUY
2025-12-03 14:36:20,020 - worker.extractor - INFO - Extracting TJS/ETH/BUY
2025-12-03 14:36:20,649 - worker.extractor - ERROR - Failed to extract SLE/BTC/SELL: illegal parameter
2025-12-03 14:36:20,709 - worker.extractor - INFO - Extracted 0 offers for SLE/BTC/SELL
2025-12-03 14:36:20,710 - worker.extractor - INFO - Extracting TJS/ETH/SELL
2025-12-03 14:36:21,280 - worker.extractor - ERROR - Failed to extract SLE/ETH/BUY: illegal parameter
2025-12-03 14:36:21,286 - worker.extractor - INFO - Extracted 0 offers for SLE/ETH/BUY
2025-12-03 14:36:21,287 - worker.extractor - INFO - Extracting TMT/USDT/BUY
2025-12-03 14:36:21,928 - worker.extractor - ERROR - Failed to extract SLE/ETH/SELL: illegal parameter
2025-12-03 14:36:21,949 - worker.extractor - INFO - Extracted 0 offers for SLE/ETH/SELL
2025-12-03 14:36:21,950 - worker.extractor - INFO - Extracting TMT/USDT/SELL
2025-12-03 14:36:22,534 - worker.extractor - ERROR - Failed to extract SOS/USDT/BUY: illegal parameter
2025-12-03 14:36:22,541 - worker.extractor - INFO - Extracted 0 offers for SOS/USDT/BUY
2025-12-03 14:36:22,542 - worker.extractor - INFO - Extracting TMT/BTC/BUY
2025-12-03 14:36:23,166 - worker.extractor - ERROR - Failed to extract SOS/USDT/SELL: illegal parameter
2025-12-03 14:36:23,167 - worker.extractor - INFO - Extracted 0 offers for SOS/USDT/SELL
2025-12-03 14:36:23,168 - worker.extractor - INFO - Extracting TMT/BTC/SELL
2025-12-03 14:36:23,531 - worker.rate_limiter - WARNING - Rate limiter active: 910 waits, 1007 total requests
2025-12-03 14:36:23,831 - worker.extractor - ERROR - Failed to extract SOS/BTC/BUY: illegal parameter
2025-12-03 14:36:23,849 - worker.extractor - INFO - Extracted 0 offers for SOS/BTC/BUY
2025-12-03 14:36:23,851 - worker.extractor - INFO - Extracting TMT/ETH/BUY
2025-12-03 14:36:24,418 - worker.extractor - ERROR - Failed to extract SOS/BTC/SELL: illegal parameter
2025-12-03 14:36:24,427 - worker.extractor - INFO - Extracted 0 offers for SOS/BTC/SELL
2025-12-03 14:36:24,428 - worker.extractor - INFO - Extracting TMT/ETH/SELL
2025-12-03 14:36:25,009 - worker.extractor - ERROR - Failed to extract SOS/ETH/BUY: illegal parameter
2025-12-03 14:36:25,018 - worker.extractor - INFO - Extracted 0 offers for SOS/ETH/BUY
2025-12-03 14:36:25,019 - worker.extractor - INFO - Extracting TTD/USDT/BUY
2025-12-03 14:36:25,617 - worker.extractor - ERROR - Failed to extract SOS/ETH/SELL: illegal parameter
2025-12-03 14:36:25,618 - worker.extractor - INFO - Extracted 0 offers for SOS/ETH/SELL
2025-12-03 14:36:25,618 - worker.extractor - INFO - Extracting TTD/USDT/SELL
2025-12-03 14:36:26,236 - worker.extractor - ERROR - Failed to extract SYP/USDT/BUY: illegal parameter
2025-12-03 14:36:26,237 - worker.extractor - INFO - Extracted 0 offers for SYP/USDT/BUY
2025-12-03 14:36:26,241 - worker.extractor - INFO - Extracting TTD/BTC/BUY
2025-12-03 14:36:26,842 - worker.extractor - ERROR - Failed to extract SYP/USDT/SELL: illegal parameter
2025-12-03 14:36:26,898 - worker.extractor - INFO - Extracted 0 offers for SYP/USDT/SELL
2025-12-03 14:36:26,899 - worker.extractor - INFO - Extracting TTD/BTC/SELL
2025-12-03 14:36:27,460 - worker.extractor - ERROR - Failed to extract SYP/BTC/BUY: illegal parameter
2025-12-03 14:36:27,476 - worker.extractor - INFO - Extracted 0 offers for SYP/BTC/BUY
2025-12-03 14:36:27,477 - worker.extractor - INFO - Extracting TTD/ETH/BUY
2025-12-03 14:36:28,119 - worker.extractor - ERROR - Failed to extract SYP/BTC/SELL: illegal parameter
2025-12-03 14:36:28,130 - worker.extractor - INFO - Extracted 0 offers for SYP/BTC/SELL
2025-12-03 14:36:28,133 - worker.extractor - INFO - Extracting TTD/ETH/SELL
2025-12-03 14:36:28,698 - worker.extractor - ERROR - Failed to extract SYP/ETH/BUY: illegal parameter
2025-12-03 14:36:28,698 - worker.extractor - INFO - Extracted 0 offers for SYP/ETH/BUY
2025-12-03 14:36:28,699 - worker.extractor - INFO - Extracting YER/USDT/BUY
2025-12-03 14:36:29,301 - worker.extractor - ERROR - Failed to extract SYP/ETH/SELL: illegal parameter
2025-12-03 14:36:29,302 - worker.extractor - INFO - Extracted 0 offers for SYP/ETH/SELL
2025-12-03 14:36:29,306 - worker.extractor - INFO - Extracting YER/USDT/SELL
2025-12-03 14:36:29,630 - worker.rate_limiter - WARNING - Rate limiter active: 920 waits, 1017 total requests
2025-12-03 14:36:29,941 - worker.extractor - ERROR - Failed to extract TJS/USDT/BUY: illegal parameter
2025-12-03 14:36:29,949 - worker.extractor - INFO - Extracted 0 offers for TJS/USDT/BUY
2025-12-03 14:36:29,950 - worker.extractor - INFO - Extracting YER/BTC/BUY
2025-12-03 14:36:30,494 - worker.extractor - ERROR - Failed to extract TJS/USDT/SELL: illegal parameter
2025-12-03 14:36:30,499 - worker.extractor - INFO - Extracted 0 offers for TJS/USDT/SELL
2025-12-03 14:36:30,500 - worker.extractor - INFO - Extracting YER/BTC/SELL
2025-12-03 14:36:31,091 - worker.extractor - ERROR - Failed to extract TJS/BTC/BUY: illegal parameter
2025-12-03 14:36:31,091 - worker.extractor - INFO - Extracted 0 offers for TJS/BTC/BUY
2025-12-03 14:36:31,092 - worker.extractor - INFO - Extracting YER/ETH/BUY
2025-12-03 14:36:31,728 - worker.extractor - ERROR - Failed to extract TJS/BTC/SELL: illegal parameter
2025-12-03 14:36:31,729 - worker.extractor - INFO - Extracted 0 offers for TJS/BTC/SELL
2025-12-03 14:36:31,730 - worker.extractor - INFO - Extracting YER/ETH/SELL
2025-12-03 14:36:32,995 - worker.extractor - ERROR - Failed to extract TJS/ETH/BUY: illegal parameter
2025-12-03 14:36:33,475 - worker.extractor - INFO - Extracted 0 offers for TJS/ETH/BUY
2025-12-03 14:36:33,476 - worker.extractor - INFO - Extracting ZMW/USDT/BUY
2025-12-03 14:36:33,812 - worker.extractor - ERROR - Failed to extract TJS/ETH/SELL: illegal parameter
2025-12-03 14:36:33,831 - worker.extractor - INFO - Extracted 0 offers for TJS/ETH/SELL
2025-12-03 14:36:33,837 - worker.extractor - INFO - Extracting ZMW/USDT/SELL
2025-12-03 14:36:34,497 - worker.extractor - ERROR - Failed to extract TMT/USDT/BUY: illegal parameter
2025-12-03 14:36:35,213 - worker.extractor - INFO - Extracted 0 offers for TMT/USDT/BUY
2025-12-03 14:36:35,214 - worker.extractor - INFO - Extracting ZMW/BTC/BUY
2025-12-03 14:36:35,743 - worker.extractor - ERROR - Failed to extract TMT/USDT/SELL: illegal parameter
2025-12-03 14:36:36,830 - worker.extractor - INFO - Extracted 0 offers for TMT/USDT/SELL
2025-12-03 14:36:36,830 - worker.extractor - INFO - Extracting ZMW/BTC/SELL
2025-12-03 14:36:37,215 - worker.extractor - ERROR - Failed to extract TMT/BTC/BUY: illegal parameter
2025-12-03 14:36:37,389 - worker.extractor - INFO - Extracted 0 offers for TMT/BTC/BUY
2025-12-03 14:36:37,545 - worker.extractor - INFO - Extracting ZMW/ETH/BUY
2025-12-03 14:36:37,912 - worker.extractor - ERROR - Failed to extract TMT/BTC/SELL: illegal parameter
2025-12-03 14:36:37,947 - worker.extractor - INFO - Extracted 0 offers for TMT/BTC/SELL
2025-12-03 14:36:37,991 - worker.extractor - INFO - Extracting ZMW/ETH/SELL
2025-12-03 14:36:38,201 - worker.rate_limiter - WARNING - Rate limiter active: 930 waits, 1027 total requests
2025-12-03 14:36:38,464 - worker.extractor - ERROR - Failed to extract TMT/ETH/BUY: illegal parameter
2025-12-03 14:36:38,465 - worker.extractor - INFO - Extracted 0 offers for TMT/ETH/BUY
2025-12-03 14:36:38,466 - worker.extractor - INFO - Extracting ZWG/USDT/BUY
2025-12-03 14:36:39,099 - worker.extractor - ERROR - Failed to extract TMT/ETH/SELL: illegal parameter
2025-12-03 14:36:39,212 - worker.extractor - INFO - Extracted 0 offers for TMT/ETH/SELL
2025-12-03 14:36:39,214 - worker.extractor - INFO - Extracting ZWG/USDT/SELL
2025-12-03 14:36:39,775 - worker.extractor - ERROR - Failed to extract TTD/USDT/BUY: illegal parameter
2025-12-03 14:36:39,880 - worker.extractor - INFO - Extracted 0 offers for TTD/USDT/BUY
2025-12-03 14:36:40,108 - worker.extractor - INFO - Extracting ZWG/BTC/BUY
2025-12-03 14:36:40,440 - worker.extractor - ERROR - Failed to extract TTD/USDT/SELL: illegal parameter
2025-12-03 14:36:40,476 - worker.extractor - INFO - Extracted 0 offers for TTD/USDT/SELL
2025-12-03 14:36:40,608 - worker.extractor - INFO - Extracting ZWG/BTC/SELL
2025-12-03 14:36:41,090 - worker.extractor - ERROR - Failed to extract TTD/BTC/BUY: illegal parameter
2025-12-03 14:36:41,207 - worker.extractor - INFO - Extracted 0 offers for TTD/BTC/BUY
2025-12-03 14:36:41,208 - worker.extractor - INFO - Extracting ZWG/ETH/BUY
2025-12-03 14:36:41,760 - worker.extractor - ERROR - Failed to extract TTD/BTC/SELL: illegal parameter
2025-12-03 14:36:41,789 - worker.extractor - INFO - Extracted 0 offers for TTD/BTC/SELL
2025-12-03 14:36:41,866 - worker.extractor - INFO - Extracting ZWG/ETH/SELL
2025-12-03 14:36:42,511 - worker.extractor - ERROR - Failed to extract TTD/ETH/BUY: illegal parameter
2025-12-03 14:36:42,582 - worker.extractor - INFO - Extracted 0 offers for TTD/ETH/BUY
2025-12-03 14:36:42,583 - worker.extractor - INFO - Extracting VND/USDT/BUY
2025-12-03 14:36:43,258 - worker.extractor - ERROR - Failed to extract TTD/ETH/SELL: illegal parameter
2025-12-03 14:36:43,599 - worker.extractor - INFO - Extracted 0 offers for TTD/ETH/SELL
2025-12-03 14:36:43,607 - worker.extractor - INFO - Extracting VND/USDT/SELL
2025-12-03 14:36:44,957 - worker.extractor - ERROR - Failed to extract YER/USDT/BUY: illegal parameter
2025-12-03 14:36:45,196 - worker.extractor - INFO - Extracted 0 offers for YER/USDT/BUY
2025-12-03 14:36:45,198 - worker.extractor - INFO - Extracting VND/BTC/BUY
2025-12-03 14:36:45,808 - worker.extractor - ERROR - Failed to extract YER/USDT/SELL: illegal parameter
2025-12-03 14:36:46,165 - worker.extractor - INFO - Extracted 0 offers for YER/USDT/SELL
2025-12-03 14:36:46,276 - worker.rate_limiter - WARNING - Rate limiter active: 940 waits, 1037 total requests
2025-12-03 14:36:46,661 - worker.extractor - INFO - Extracting VND/BTC/SELL
2025-12-03 14:36:47,511 - worker.extractor - ERROR - Failed to extract YER/BTC/SELL: illegal parameter
2025-12-03 14:36:47,676 - worker.extractor - INFO - Extracted 0 offers for YER/BTC/SELL
2025-12-03 14:36:47,512 - worker.extractor - ERROR - Failed to extract YER/BTC/BUY: illegal parameter
2025-12-03 14:36:47,943 - worker.extractor - ERROR - Failed to extract YER/ETH/BUY: illegal parameter
2025-12-03 14:36:48,025 - worker.extractor - INFO - Extracting VND/ETH/BUY
2025-12-03 14:36:48,261 - worker.extractor - INFO - Extracted 0 offers for YER/BTC/BUY
2025-12-03 14:36:48,661 - worker.extractor - INFO - Extracted 0 offers for YER/ETH/BUY
2025-12-03 14:36:48,807 - worker.extractor - ERROR - Failed to extract YER/ETH/SELL: illegal parameter
2025-12-03 14:36:48,995 - worker.extractor - INFO - Extracting VND/ETH/SELL
2025-12-03 14:36:48,996 - worker.extractor - INFO - Extracting UAH/USDT/BUY
2025-12-03 14:36:49,256 - worker.extractor - INFO - Extracted 0 offers for YER/ETH/SELL
2025-12-03 14:36:49,540 - worker.extractor - ERROR - Failed to extract ZMW/USDT/BUY: illegal parameter
2025-12-03 14:36:49,597 - worker.extractor - INFO - Extracting UAH/USDT/SELL
2025-12-03 14:36:49,721 - worker.extractor - INFO - Extracted 0 offers for ZMW/USDT/BUY
2025-12-03 14:36:49,997 - worker.extractor - INFO - Extracting UAH/BTC/BUY
2025-12-03 14:36:50,238 - worker.extractor - ERROR - Failed to extract ZMW/USDT/SELL: illegal parameter
2025-12-03 14:36:50,297 - worker.extractor - INFO - Extracted 0 offers for ZMW/USDT/SELL
2025-12-03 14:36:50,297 - worker.extractor - INFO - Extracting UAH/BTC/SELL
2025-12-03 14:36:50,900 - worker.extractor - ERROR - Failed to extract ZMW/BTC/BUY: illegal parameter
2025-12-03 14:36:50,960 - worker.extractor - INFO - Extracted 0 offers for ZMW/BTC/BUY
2025-12-03 14:36:51,121 - worker.extractor - INFO - Extracting UAH/ETH/BUY
2025-12-03 14:36:51,580 - worker.extractor - ERROR - Failed to extract ZMW/BTC/SELL: illegal parameter
2025-12-03 14:36:51,671 - worker.extractor - INFO - Extracted 0 offers for ZMW/BTC/SELL
2025-12-03 14:36:51,672 - worker.extractor - INFO - Extracting UAH/ETH/SELL
2025-12-03 14:36:52,713 - worker.extractor - ERROR - Failed to extract ZMW/ETH/BUY: illegal parameter
2025-12-03 14:36:52,773 - worker.extractor - INFO - Extracted 0 offers for ZMW/ETH/BUY
2025-12-03 14:36:52,926 - worker.extractor - ERROR - Failed to extract ZMW/ETH/SELL: illegal parameter
2025-12-03 14:36:52,960 - worker.extractor - INFO - Extracting EUR/USDT/BUY
2025-12-03 14:36:53,221 - worker.extractor - INFO - Extracted 0 offers for ZMW/ETH/SELL
2025-12-03 14:36:53,497 - worker.extractor - INFO - Extracting EUR/USDT/SELL
2025-12-03 14:36:53,570 - worker.extractor - ERROR - Failed to extract ZWG/USDT/BUY: illegal parameter
2025-12-03 14:36:53,829 - worker.extractor - INFO - Extracted 0 offers for ZWG/USDT/BUY
2025-12-03 14:36:54,056 - worker.rate_limiter - WARNING - Rate limiter active: 950 waits, 1048 total requests
2025-12-03 14:36:54,175 - worker.extractor - INFO - Extracting EUR/BTC/BUY
2025-12-03 14:36:54,593 - worker.extractor - ERROR - Failed to extract ZWG/USDT/SELL: illegal parameter
2025-12-03 14:36:54,664 - worker.extractor - INFO - Extracted 0 offers for ZWG/USDT/SELL
2025-12-03 14:36:54,775 - worker.extractor - INFO - Extracting EUR/BTC/SELL
2025-12-03 14:36:54,990 - worker.extractor - ERROR - Failed to extract ZWG/BTC/BUY: illegal parameter
2025-12-03 14:36:55,029 - worker.extractor - INFO - Extracted 0 offers for ZWG/BTC/BUY
2025-12-03 14:36:55,030 - worker.extractor - INFO - Extracting EUR/ETH/BUY
2025-12-03 14:36:55,635 - worker.extractor - ERROR - Failed to extract ZWG/BTC/SELL: illegal parameter
2025-12-03 14:36:55,675 - worker.extractor - INFO - Extracted 0 offers for ZWG/BTC/SELL
2025-12-03 14:36:55,697 - worker.extractor - INFO - Extracting EUR/ETH/SELL
2025-12-03 14:36:56,290 - worker.extractor - ERROR - Failed to extract ZWG/ETH/BUY: illegal parameter
2025-12-03 14:36:56,305 - worker.extractor - INFO - Extracted 0 offers for ZWG/ETH/BUY
2025-12-03 14:36:56,305 - worker.extractor - INFO - Extracting COP/USDT/BUY
2025-12-03 14:36:56,880 - worker.extractor - ERROR - Failed to extract ZWG/ETH/SELL: illegal parameter
2025-12-03 14:36:56,957 - worker.extractor - INFO - Extracted 0 offers for ZWG/ETH/SELL
2025-12-03 14:36:56,970 - worker.extractor - INFO - Extracting COP/USDT/SELL
2025-12-03 14:36:57,556 - worker.extractor - ERROR - Failed to extract VND/USDT/BUY: illegal parameter
2025-12-03 14:36:57,625 - worker.extractor - INFO - Extracted 0 offers for VND/USDT/BUY
2025-12-03 14:36:57,846 - worker.extractor - INFO - Extracting COP/BTC/BUY
2025-12-03 14:36:58,262 - worker.extractor - ERROR - Failed to extract VND/USDT/SELL: illegal parameter
2025-12-03 14:36:58,335 - worker.extractor - INFO - Extracted 0 offers for VND/USDT/SELL
2025-12-03 14:36:58,336 - worker.extractor - INFO - Extracting COP/BTC/SELL
2025-12-03 14:36:59,156 - worker.extractor - ERROR - Failed to extract VND/BTC/BUY: illegal parameter
2025-12-03 14:36:59,440 - worker.extractor - INFO - Extracted 0 offers for VND/BTC/BUY
2025-12-03 14:36:59,746 - worker.extractor - INFO - Extracting COP/ETH/BUY
2025-12-03 14:36:59,786 - worker.extractor - ERROR - Failed to extract VND/BTC/SELL: illegal parameter
2025-12-03 14:37:00,096 - worker.extractor - INFO - Extracted 0 offers for VND/BTC/SELL
2025-12-03 14:37:00,242 - worker.extractor - INFO - Extracting COP/ETH/SELL
2025-12-03 14:37:00,488 - worker.extractor - ERROR - Failed to extract VND/ETH/BUY: illegal parameter
2025-12-03 14:37:00,555 - worker.extractor - INFO - Extracted 0 offers for VND/ETH/BUY
2025-12-03 14:37:00,556 - worker.extractor - INFO - Extracting BRL/USDT/BUY
2025-12-03 14:37:00,771 - worker.rate_limiter - WARNING - Rate limiter active: 960 waits, 1058 total requests
2025-12-03 14:37:01,413 - worker.extractor - ERROR - Failed to extract VND/ETH/SELL: illegal parameter
2025-12-03 14:37:01,424 - worker.extractor - INFO - Extracted 0 offers for VND/ETH/SELL
2025-12-03 14:37:01,457 - worker.extractor - INFO - Extracting BRL/USDT/SELL
2025-12-03 14:37:01,667 - worker.extractor - ERROR - Failed to extract UAH/USDT/BUY: illegal parameter
2025-12-03 14:37:01,683 - worker.extractor - INFO - Extracted 0 offers for UAH/USDT/BUY
2025-12-03 14:37:01,684 - worker.extractor - INFO - Extracting BRL/BTC/BUY
2025-12-03 14:37:02,312 - worker.extractor - ERROR - Failed to extract UAH/USDT/SELL: illegal parameter
2025-12-03 14:37:02,345 - worker.extractor - INFO - Extracted 0 offers for UAH/USDT/SELL
2025-12-03 14:37:02,350 - worker.extractor - INFO - Extracting BRL/BTC/SELL
2025-12-03 14:37:02,945 - worker.extractor - ERROR - Failed to extract UAH/BTC/BUY: illegal parameter
2025-12-03 14:37:03,021 - worker.extractor - INFO - Extracted 0 offers for UAH/BTC/BUY
2025-12-03 14:37:03,137 - worker.extractor - INFO - Extracting BRL/ETH/BUY
2025-12-03 14:37:03,586 - worker.extractor - ERROR - Failed to extract UAH/BTC/SELL: illegal parameter
2025-12-03 14:37:03,628 - worker.extractor - INFO - Extracted 0 offers for UAH/BTC/SELL
2025-12-03 14:37:03,691 - worker.extractor - INFO - Extracting BRL/ETH/SELL
2025-12-03 14:37:04,293 - worker.extractor - ERROR - Failed to extract UAH/ETH/BUY: illegal parameter
2025-12-03 14:37:04,317 - worker.extractor - INFO - Extracted 0 offers for UAH/ETH/BUY
2025-12-03 14:37:04,340 - worker.extractor - INFO - Extracting ARS/USDT/BUY
2025-12-03 14:37:04,957 - worker.extractor - ERROR - Failed to extract UAH/ETH/SELL: illegal parameter
2025-12-03 14:37:05,003 - worker.extractor - INFO - Extracted 0 offers for UAH/ETH/SELL
2025-12-03 14:37:05,102 - worker.extractor - INFO - Extracting ARS/USDT/SELL
2025-12-03 14:37:05,615 - worker.extractor - ERROR - Failed to extract EUR/USDT/BUY: illegal parameter
2025-12-03 14:37:05,619 - worker.extractor - INFO - Extracted 0 offers for EUR/USDT/BUY
2025-12-03 14:37:05,625 - worker.extractor - INFO - Extracting ARS/BTC/BUY
2025-12-03 14:37:06,168 - worker.extractor - ERROR - Failed to extract EUR/USDT/SELL: illegal parameter
2025-12-03 14:37:06,189 - worker.extractor - INFO - Extracted 0 offers for EUR/USDT/SELL
2025-12-03 14:37:06,192 - worker.extractor - INFO - Extracting ARS/BTC/SELL
2025-12-03 14:37:06,785 - worker.extractor - ERROR - Failed to extract EUR/BTC/BUY: illegal parameter
2025-12-03 14:37:06,789 - worker.extractor - INFO - Extracted 0 offers for EUR/BTC/BUY
2025-12-03 14:37:06,790 - worker.extractor - INFO - Extracting ARS/ETH/BUY
2025-12-03 14:37:07,109 - worker.rate_limiter - WARNING - Rate limiter active: 970 waits, 1068 total requests
2025-12-03 14:37:07,406 - worker.extractor - ERROR - Failed to extract EUR/BTC/SELL: illegal parameter
2025-12-03 14:37:07,408 - worker.extractor - INFO - Extracted 0 offers for EUR/BTC/SELL
2025-12-03 14:37:07,408 - worker.extractor - INFO - Extracting ARS/ETH/SELL
2025-12-03 14:37:07,983 - worker.extractor - ERROR - Failed to extract EUR/ETH/BUY: illegal parameter
2025-12-03 14:37:07,990 - worker.extractor - INFO - Extracted 0 offers for EUR/ETH/BUY
2025-12-03 14:37:07,994 - worker.extractor - INFO - Extracting PEN/USDT/BUY
2025-12-03 14:37:08,619 - worker.extractor - ERROR - Failed to extract EUR/ETH/SELL: illegal parameter
2025-12-03 14:37:08,635 - worker.extractor - INFO - Extracted 0 offers for EUR/ETH/SELL
2025-12-03 14:37:08,635 - worker.extractor - INFO - Extracting PEN/USDT/SELL
2025-12-03 14:37:09,218 - worker.extractor - ERROR - Failed to extract COP/USDT/BUY: illegal parameter
2025-12-03 14:37:09,219 - worker.extractor - INFO - Extracted 0 offers for COP/USDT/BUY
2025-12-03 14:37:09,219 - worker.extractor - INFO - Extracting PEN/BTC/BUY
2025-12-03 14:37:09,929 - worker.extractor - ERROR - Failed to extract COP/USDT/SELL: illegal parameter
2025-12-03 14:37:10,117 - worker.extractor - INFO - Extracted 0 offers for COP/USDT/SELL
2025-12-03 14:37:10,351 - worker.extractor - INFO - Extracting PEN/BTC/SELL
2025-12-03 14:37:10,641 - worker.extractor - ERROR - Failed to extract COP/BTC/BUY: illegal parameter
2025-12-03 14:37:10,685 - worker.extractor - INFO - Extracted 0 offers for COP/BTC/BUY
2025-12-03 14:37:10,710 - worker.extractor - INFO - Extracting PEN/ETH/BUY
2025-12-03 14:37:11,343 - worker.extractor - ERROR - Failed to extract COP/BTC/SELL: illegal parameter
2025-12-03 14:37:11,352 - worker.extractor - INFO - Extracted 0 offers for COP/BTC/SELL
2025-12-03 14:37:11,355 - worker.extractor - INFO - Extracting PEN/ETH/SELL
2025-12-03 14:37:12,111 - worker.extractor - ERROR - Failed to extract COP/ETH/BUY: illegal parameter
2025-12-03 14:37:12,115 - worker.extractor - INFO - Extracted 0 offers for COP/ETH/BUY
2025-12-03 14:37:12,116 - worker.extractor - INFO - Extracting ZAR/USDT/BUY
2025-12-03 14:37:12,541 - worker.extractor - ERROR - Failed to extract COP/ETH/SELL: illegal parameter
2025-12-03 14:37:12,549 - worker.extractor - INFO - Extracted 0 offers for COP/ETH/SELL
2025-12-03 14:37:12,550 - worker.extractor - INFO - Extracting ZAR/USDT/SELL
2025-12-03 14:37:13,200 - worker.extractor - ERROR - Failed to extract BRL/USDT/BUY: illegal parameter
2025-12-03 14:37:13,202 - worker.extractor - INFO - Extracted 0 offers for BRL/USDT/BUY
2025-12-03 14:37:13,205 - worker.extractor - INFO - Extracting ZAR/BTC/BUY
2025-12-03 14:37:13,372 - worker.rate_limiter - WARNING - Rate limiter active: 980 waits, 1078 total requests
2025-12-03 14:37:13,636 - worker.extractor - ERROR - Failed to extract BRL/USDT/SELL: illegal parameter
2025-12-03 14:37:13,639 - worker.extractor - INFO - Extracted 0 offers for BRL/USDT/SELL
2025-12-03 14:37:13,640 - worker.extractor - INFO - Extracting ZAR/BTC/SELL
2025-12-03 14:37:14,250 - worker.extractor - ERROR - Failed to extract BRL/BTC/BUY: illegal parameter
2025-12-03 14:37:14,271 - worker.extractor - INFO - Extracted 0 offers for BRL/BTC/BUY
2025-12-03 14:37:14,272 - worker.extractor - INFO - Extracting ZAR/ETH/BUY
2025-12-03 14:37:14,901 - worker.extractor - ERROR - Failed to extract BRL/BTC/SELL: illegal parameter
2025-12-03 14:37:14,908 - worker.extractor - INFO - Extracted 0 offers for BRL/BTC/SELL
2025-12-03 14:37:14,908 - worker.extractor - INFO - Extracting ZAR/ETH/SELL
2025-12-03 14:37:15,507 - worker.extractor - ERROR - Failed to extract BRL/ETH/BUY: illegal parameter
2025-12-03 14:37:15,509 - worker.extractor - INFO - Extracted 0 offers for BRL/ETH/BUY
2025-12-03 14:37:15,510 - worker.extractor - INFO - Extracting MXN/USDT/BUY
2025-12-03 14:37:16,121 - worker.extractor - ERROR - Failed to extract BRL/ETH/SELL: illegal parameter
2025-12-03 14:37:16,126 - worker.extractor - INFO - Extracted 0 offers for BRL/ETH/SELL
2025-12-03 14:37:16,131 - worker.extractor - INFO - Extracting MXN/USDT/SELL
2025-12-03 14:37:16,706 - worker.extractor - ERROR - Failed to extract ARS/USDT/BUY: illegal parameter
2025-12-03 14:37:16,791 - worker.extractor - INFO - Extracted 0 offers for ARS/USDT/BUY
2025-12-03 14:37:16,793 - worker.extractor - INFO - Extracting MXN/BTC/BUY
2025-12-03 14:37:17,356 - worker.extractor - ERROR - Failed to extract ARS/USDT/SELL: illegal parameter
2025-12-03 14:37:17,368 - worker.extractor - INFO - Extracted 0 offers for ARS/USDT/SELL
2025-12-03 14:37:17,371 - worker.extractor - INFO - Extracting MXN/BTC/SELL
2025-12-03 14:37:17,953 - worker.extractor - ERROR - Failed to extract ARS/BTC/BUY: illegal parameter
2025-12-03 14:37:17,959 - worker.extractor - INFO - Extracted 0 offers for ARS/BTC/BUY
2025-12-03 14:37:17,962 - worker.extractor - INFO - Extracting MXN/ETH/BUY
2025-12-03 14:37:18,557 - worker.extractor - ERROR - Failed to extract ARS/BTC/SELL: illegal parameter
2025-12-03 14:37:18,588 - worker.extractor - INFO - Extracted 0 offers for ARS/BTC/SELL
2025-12-03 14:37:18,589 - worker.extractor - INFO - Extracting MXN/ETH/SELL
2025-12-03 14:37:19,234 - worker.extractor - ERROR - Failed to extract ARS/ETH/BUY: illegal parameter
2025-12-03 14:37:19,330 - worker.extractor - INFO - Extracted 0 offers for ARS/ETH/BUY
2025-12-03 14:37:19,332 - worker.extractor - INFO - Extracting HKD/USDT/BUY
2025-12-03 14:37:19,601 - worker.rate_limiter - WARNING - Rate limiter active: 990 waits, 1088 total requests
2025-12-03 14:37:19,937 - worker.extractor - ERROR - Failed to extract ARS/ETH/SELL: illegal parameter
2025-12-03 14:37:19,983 - worker.extractor - INFO - Extracted 0 offers for ARS/ETH/SELL
2025-12-03 14:37:19,986 - worker.extractor - INFO - Extracting HKD/USDT/SELL
2025-12-03 14:37:20,474 - worker.extractor - ERROR - Failed to extract PEN/USDT/BUY: illegal parameter
2025-12-03 14:37:20,481 - worker.extractor - INFO - Extracted 0 offers for PEN/USDT/BUY
2025-12-03 14:37:20,483 - worker.extractor - INFO - Extracting HKD/BTC/BUY
2025-12-03 14:37:21,237 - worker.extractor - ERROR - Failed to extract PEN/USDT/SELL: illegal parameter
2025-12-03 14:37:21,239 - worker.extractor - INFO - Extracted 0 offers for PEN/USDT/SELL
2025-12-03 14:37:21,240 - worker.extractor - INFO - Extracting HKD/BTC/SELL
2025-12-03 14:37:21,849 - worker.extractor - ERROR - Failed to extract PEN/BTC/BUY: illegal parameter
2025-12-03 14:37:21,849 - worker.extractor - INFO - Extracted 0 offers for PEN/BTC/BUY
2025-12-03 14:37:21,851 - worker.extractor - INFO - Extracting HKD/ETH/BUY
2025-12-03 14:37:22,477 - worker.extractor - ERROR - Failed to extract PEN/BTC/SELL: illegal parameter
2025-12-03 14:37:22,498 - worker.extractor - INFO - Extracted 0 offers for PEN/BTC/SELL
2025-12-03 14:37:22,509 - worker.extractor - INFO - Extracting HKD/ETH/SELL
2025-12-03 14:37:23,082 - worker.extractor - ERROR - Failed to extract PEN/ETH/BUY: illegal parameter
2025-12-03 14:37:23,102 - worker.extractor - INFO - Extracted 0 offers for PEN/ETH/BUY
2025-12-03 14:37:23,103 - worker.extractor - INFO - Extracting GBP/USDT/BUY
2025-12-03 14:37:23,679 - worker.extractor - ERROR - Failed to extract PEN/ETH/SELL: illegal parameter
2025-12-03 14:37:23,685 - worker.extractor - INFO - Extracted 0 offers for PEN/ETH/SELL
2025-12-03 14:37:23,686 - worker.extractor - INFO - Extracting GBP/USDT/SELL
2025-12-03 14:37:24,277 - worker.extractor - ERROR - Failed to extract ZAR/USDT/BUY: illegal parameter
2025-12-03 14:37:24,278 - worker.extractor - INFO - Extracted 0 offers for ZAR/USDT/BUY
2025-12-03 14:37:24,278 - worker.extractor - INFO - Extracting GBP/BTC/BUY
2025-12-03 14:37:25,313 - worker.extractor - ERROR - Failed to extract ZAR/USDT/SELL: illegal parameter
2025-12-03 14:37:25,315 - worker.extractor - INFO - Extracted 0 offers for ZAR/USDT/SELL
2025-12-03 14:37:25,316 - worker.extractor - INFO - Extracting GBP/BTC/SELL
2025-12-03 14:37:25,475 - worker.extractor - ERROR - Failed to extract ZAR/BTC/BUY: illegal parameter
2025-12-03 14:37:25,479 - worker.extractor - INFO - Extracted 0 offers for ZAR/BTC/BUY
2025-12-03 14:37:25,480 - worker.extractor - INFO - Extracting GBP/ETH/BUY
2025-12-03 14:37:25,801 - worker.rate_limiter - WARNING - Rate limiter active: 1000 waits, 1098 total requests
2025-12-03 14:37:26,086 - worker.extractor - ERROR - Failed to extract ZAR/BTC/SELL: illegal parameter
2025-12-03 14:37:26,087 - worker.extractor - INFO - Extracted 0 offers for ZAR/BTC/SELL
2025-12-03 14:37:26,089 - worker.extractor - INFO - Extracting GBP/ETH/SELL
2025-12-03 14:37:26,668 - worker.extractor - ERROR - Failed to extract ZAR/ETH/BUY: illegal parameter
2025-12-03 14:37:26,669 - worker.extractor - INFO - Extracted 0 offers for ZAR/ETH/BUY
2025-12-03 14:37:26,669 - worker.extractor - INFO - Extracting KES/USDT/BUY
2025-12-03 14:37:27,264 - worker.extractor - ERROR - Failed to extract ZAR/ETH/SELL: illegal parameter
2025-12-03 14:37:27,265 - worker.extractor - INFO - Extracted 0 offers for ZAR/ETH/SELL
2025-12-03 14:37:27,265 - worker.extractor - INFO - Extracting KES/USDT/SELL
2025-12-03 14:37:27,900 - worker.extractor - ERROR - Failed to extract MXN/USDT/BUY: illegal parameter
2025-12-03 14:37:27,971 - worker.extractor - INFO - Extracted 0 offers for MXN/USDT/BUY
2025-12-03 14:37:28,055 - worker.extractor - INFO - Extracting KES/BTC/BUY
2025-12-03 14:37:28,583 - worker.extractor - ERROR - Failed to extract MXN/USDT/SELL: illegal parameter
2025-12-03 14:37:28,605 - worker.extractor - INFO - Extracted 0 offers for MXN/USDT/SELL
2025-12-03 14:37:28,649 - worker.extractor - INFO - Extracting KES/BTC/SELL
2025-12-03 14:37:29,263 - worker.extractor - ERROR - Failed to extract MXN/BTC/BUY: illegal parameter
2025-12-03 14:37:29,417 - worker.extractor - INFO - Extracted 0 offers for MXN/BTC/BUY
2025-12-03 14:37:29,419 - worker.extractor - INFO - Extracting KES/ETH/BUY
2025-12-03 14:37:29,885 - worker.extractor - ERROR - Failed to extract MXN/BTC/SELL: illegal parameter
2025-12-03 14:37:30,020 - worker.extractor - INFO - Extracted 0 offers for MXN/BTC/SELL
2025-12-03 14:37:30,039 - worker.extractor - INFO - Extracting KES/ETH/SELL
2025-12-03 14:37:30,490 - worker.extractor - ERROR - Failed to extract MXN/ETH/BUY: illegal parameter
2025-12-03 14:37:30,548 - worker.extractor - INFO - Extracted 0 offers for MXN/ETH/BUY
2025-12-03 14:37:30,550 - worker.extractor - INFO - Extracting AUD/USDT/BUY
2025-12-03 14:37:31,102 - worker.extractor - ERROR - Failed to extract MXN/ETH/SELL: illegal parameter
2025-12-03 14:37:31,168 - worker.extractor - INFO - Extracted 0 offers for MXN/ETH/SELL
2025-12-03 14:37:31,239 - worker.extractor - INFO - Extracting AUD/USDT/SELL
2025-12-03 14:37:31,699 - worker.extractor - ERROR - Failed to extract HKD/USDT/BUY: illegal parameter
2025-12-03 14:37:31,717 - worker.extractor - INFO - Extracted 0 offers for HKD/USDT/BUY
2025-12-03 14:37:31,724 - worker.extractor - INFO - Extracting AUD/BTC/BUY
2025-12-03 14:37:32,038 - worker.rate_limiter - WARNING - Rate limiter active: 1010 waits, 1108 total requests
2025-12-03 14:37:32,354 - worker.extractor - ERROR - Failed to extract HKD/USDT/SELL: illegal parameter
2025-12-03 14:37:32,363 - worker.extractor - INFO - Extracted 0 offers for HKD/USDT/SELL
2025-12-03 14:37:32,367 - worker.extractor - INFO - Extracting AUD/BTC/SELL
2025-12-03 14:37:32,919 - worker.extractor - ERROR - Failed to extract HKD/BTC/BUY: illegal parameter
2025-12-03 14:37:32,937 - worker.extractor - INFO - Extracted 0 offers for HKD/BTC/BUY
2025-12-03 14:37:32,938 - worker.extractor - INFO - Extracting AUD/ETH/BUY
2025-12-03 14:37:33,519 - worker.extractor - ERROR - Failed to extract HKD/BTC/SELL:

# fifth run

2025-12-03 14:40:23,461 - worker.extractor - INFO - Extracted 0 offers for TND/ETH/BUY
2025-12-03 14:40:23,520 - worker.extractor - INFO - Extracting NPR/USDT/BUY
2025-12-03 14:40:23,526 - worker.rate_limiter - WARNING - Rate limiter active: 1290 waits, 1388 total requests
2025-12-03 14:40:23,835 - worker.extractor - ERROR - Failed to extract TND/ETH/SELL: illegal parameter
2025-12-03 14:40:23,836 - worker.extractor - INFO - Extracted 0 offers for TND/ETH/SELL
2025-12-03 14:40:23,836 - worker.extractor - INFO - Extracting NPR/USDT/SELL
2025-12-03 14:40:24,397 - worker.extractor - ERROR - Failed to extract SDG/USDT/BUY: illegal parameter
2025-12-03 14:40:24,431 - worker.extractor - INFO - Extracted 0 offers for SDG/USDT/BUY
2025-12-03 14:40:24,435 - worker.extractor - INFO - Extracting NPR/BTC/BUY
2025-12-03 14:40:24,997 - worker.extractor - ERROR - Failed to extract SDG/USDT/SELL: illegal parameter
2025-12-03 14:40:24,997 - worker.extractor - INFO - Extracted 0 offers for SDG/USDT/SELL
2025-12-03 14:40:24,998 - worker.extractor - INFO - Extracting NPR/BTC/SELL
2025-12-03 14:40:25,610 - worker.extractor - ERROR - Failed to extract SDG/BTC/BUY: illegal parameter
2025-12-03 14:40:25,611 - worker.extractor - INFO - Extracted 0 offers for SDG/BTC/BUY
2025-12-03 14:40:25,611 - worker.extractor - INFO - Extracting NPR/ETH/BUY
2025-12-03 14:40:26,190 - worker.extractor - ERROR - Failed to extract SDG/BTC/SELL: illegal parameter
2025-12-03 14:40:26,190 - worker.extractor - INFO - Extracted 0 offers for SDG/BTC/SELL
2025-12-03 14:40:26,191 - worker.extractor - INFO - Extracting NPR/ETH/SELL
2025-12-03 14:40:26,828 - worker.extractor - ERROR - Failed to extract SDG/ETH/BUY: illegal parameter
2025-12-03 14:40:26,830 - worker.extractor - INFO - Extracted 0 offers for SDG/ETH/BUY
2025-12-03 14:40:26,831 - worker.extractor - INFO - Extracting TZS/USDT/BUY
2025-12-03 14:40:27,442 - worker.extractor - ERROR - Failed to extract SDG/ETH/SELL: illegal parameter
2025-12-03 14:40:27,475 - worker.extractor - INFO - Extracted 0 offers for SDG/ETH/SELL
2025-12-03 14:40:27,482 - worker.extractor - INFO - Extracting TZS/USDT/SELL
2025-12-03 14:40:28,068 - worker.extractor - ERROR - Failed to extract MNT/USDT/BUY: illegal parameter
2025-12-03 14:40:28,071 - worker.extractor - INFO - Extracted 0 offers for MNT/USDT/BUY
2025-12-03 14:40:28,071 - worker.extractor - INFO - Extracting TZS/BTC/BUY
2025-12-03 14:40:28,655 - worker.extractor - ERROR - Failed to extract MNT/USDT/SELL: illegal parameter
2025-12-03 14:40:28,655 - worker.extractor - INFO - Extracted 0 offers for MNT/USDT/SELL
2025-12-03 14:40:28,656 - worker.extractor - INFO - Extracting TZS/BTC/SELL
2025-12-03 14:40:29,446 - worker.extractor - ERROR - Failed to extract MNT/BTC/BUY: illegal parameter
2025-12-03 14:40:29,476 - worker.extractor - INFO - Extracted 0 offers for MNT/BTC/BUY
2025-12-03 14:40:29,527 - worker.extractor - INFO - Extracting TZS/ETH/BUY
2025-12-03 14:40:29,722 - worker.rate_limiter - WARNING - Rate limiter active: 1300 waits, 1398 total requests
2025-12-03 14:40:30,139 - worker.extractor - ERROR - Failed to extract MNT/BTC/SELL: illegal parameter
2025-12-03 14:40:30,141 - worker.extractor - INFO - Extracted 0 offers for MNT/BTC/SELL
2025-12-03 14:40:30,145 - worker.extractor - INFO - Extracting TZS/ETH/SELL
2025-12-03 14:40:30,619 - worker.extractor - ERROR - Failed to extract MNT/ETH/BUY: illegal parameter
2025-12-03 14:40:30,619 - worker.extractor - INFO - Extracted 0 offers for MNT/ETH/BUY
2025-12-03 14:40:30,620 - worker.extractor - INFO - Extracting XOF/USDT/BUY
2025-12-03 14:40:31,234 - worker.extractor - ERROR - Failed to extract MNT/ETH/SELL: illegal parameter
2025-12-03 14:40:31,235 - worker.extractor - INFO - Extracted 0 offers for MNT/ETH/SELL
2025-12-03 14:40:31,236 - worker.extractor - INFO - Extracting XOF/USDT/SELL
2025-12-03 14:40:31,805 - worker.extractor - ERROR - Failed to extract UZS/USDT/BUY: illegal parameter
2025-12-03 14:40:31,806 - worker.extractor - INFO - Extracted 0 offers for UZS/USDT/BUY
2025-12-03 14:40:31,806 - worker.extractor - INFO - Extracting XOF/BTC/BUY
2025-12-03 14:40:32,596 - worker.extractor - ERROR - Failed to extract UZS/USDT/SELL: illegal parameter
2025-12-03 14:40:32,596 - worker.extractor - INFO - Extracted 0 offers for UZS/USDT/SELL
2025-12-03 14:40:32,597 - worker.extractor - INFO - Extracting XOF/BTC/SELL
2025-12-03 14:40:33,076 - worker.extractor - ERROR - Failed to extract UZS/BTC/BUY: illegal parameter
2025-12-03 14:40:33,076 - worker.extractor - INFO - Extracted 0 offers for UZS/BTC/BUY
2025-12-03 14:40:33,077 - worker.extractor - INFO - Extracting XOF/ETH/BUY
2025-12-03 14:40:33,674 - worker.extractor - ERROR - Failed to extract UZS/BTC/SELL: illegal parameter
2025-12-03 14:40:33,675 - worker.extractor - INFO - Extracted 0 offers for UZS/BTC/SELL
2025-12-03 14:40:33,676 - worker.extractor - INFO - Extracting XOF/ETH/SELL
2025-12-03 14:40:34,213 - worker.extractor - ERROR - Failed to extract UZS/ETH/BUY: illegal parameter
2025-12-03 14:40:34,213 - worker.extractor - INFO - Extracted 0 offers for UZS/ETH/BUY
2025-12-03 14:40:34,213 - worker.extractor - INFO - Extracting RWF/USDT/BUY
2025-12-03 14:40:34,786 - worker.extractor - ERROR - Failed to extract UZS/ETH/SELL: illegal parameter
2025-12-03 14:40:34,787 - worker.extractor - INFO - Extracted 0 offers for UZS/ETH/SELL
2025-12-03 14:40:34,787 - worker.extractor - INFO - Extracting RWF/USDT/SELL
2025-12-03 14:40:35,433 - worker.extractor - ERROR - Failed to extract NPR/USDT/BUY: illegal parameter
2025-12-03 14:40:35,446 - worker.extractor - INFO - Extracted 0 offers for NPR/USDT/BUY
2025-12-03 14:40:35,447 - worker.extractor - INFO - Extracting RWF/BTC/BUY
2025-12-03 14:40:35,756 - worker.rate_limiter - WARNING - Rate limiter active: 1310 waits, 1408 total requests
2025-12-03 14:40:36,021 - worker.extractor - ERROR - Failed to extract NPR/USDT/SELL: illegal parameter
2025-12-03 14:40:36,022 - worker.extractor - INFO - Extracted 0 offers for NPR/USDT/SELL
2025-12-03 14:40:36,023 - worker.extractor - INFO - Extracting RWF/BTC/SELL
2025-12-03 14:40:36,629 - worker.extractor - ERROR - Failed to extract NPR/BTC/BUY: illegal parameter
2025-12-03 14:40:36,630 - worker.extractor - INFO - Extracted 0 offers for NPR/BTC/BUY
2025-12-03 14:40:36,630 - worker.extractor - INFO - Extracting RWF/ETH/BUY
2025-12-03 14:40:37,236 - worker.extractor - ERROR - Failed to extract NPR/BTC/SELL: illegal parameter
2025-12-03 14:40:37,239 - worker.extractor - INFO - Extracted 0 offers for NPR/BTC/SELL
2025-12-03 14:40:37,240 - worker.extractor - INFO - Extracting RWF/ETH/SELL
2025-12-03 14:40:37,825 - worker.extractor - ERROR - Failed to extract NPR/ETH/BUY: illegal parameter
2025-12-03 14:40:37,826 - worker.extractor - INFO - Extracted 0 offers for NPR/ETH/BUY
2025-12-03 14:40:38,431 - worker.extractor - ERROR - Failed to extract NPR/ETH/SELL: illegal parameter
2025-12-03 14:40:38,446 - worker.extractor - INFO - Extracted 0 offers for NPR/ETH/SELL
2025-12-03 14:40:39,071 - worker.extractor - ERROR - Failed to extract TZS/USDT/BUY: illegal parameter
2025-12-03 14:40:39,072 - worker.extractor - INFO - Extracted 0 offers for TZS/USDT/BUY
2025-12-03 14:40:39,686 - worker.extractor - ERROR - Failed to extract TZS/USDT/SELL: illegal parameter
2025-12-03 14:40:39,687 - worker.extractor - INFO - Extracted 0 offers for TZS/USDT/SELL
2025-12-03 14:40:40,287 - worker.extractor - ERROR - Failed to extract TZS/BTC/BUY: illegal parameter
2025-12-03 14:40:40,288 - worker.extractor - INFO - Extracted 0 offers for TZS/BTC/BUY
2025-12-03 14:40:40,867 - worker.extractor - ERROR - Failed to extract TZS/BTC/SELL: illegal parameter
2025-12-03 14:40:40,882 - worker.extractor - INFO - Extracted 0 offers for TZS/BTC/SELL
2025-12-03 14:40:41,499 - worker.extractor - ERROR - Failed to extract TZS/ETH/BUY: illegal parameter
2025-12-03 14:40:41,501 - worker.extractor - INFO - Extracted 0 offers for TZS/ETH/BUY
2025-12-03 14:40:41,839 - worker.rate_limiter - WARNING - Rate limiter active: 1320 waits, 1418 total requests
2025-12-03 14:40:42,126 - worker.extractor - ERROR - Failed to extract TZS/ETH/SELL: illegal parameter
2025-12-03 14:40:42,127 - worker.extractor - INFO - Extracted 0 offers for TZS/ETH/SELL
2025-12-03 14:40:42,760 - worker.extractor - ERROR - Failed to extract XOF/USDT/BUY: illegal parameter
2025-12-03 14:40:42,760 - worker.extractor - INFO - Extracted 0 offers for XOF/USDT/BUY
2025-12-03 14:40:43,321 - worker.extractor - ERROR - Failed to extract XOF/USDT/SELL: illegal parameter
2025-12-03 14:40:43,323 - worker.extractor - INFO - Extracted 0 offers for XOF/USDT/SELL
2025-12-03 14:40:43,924 - worker.extractor - ERROR - Failed to extract XOF/BTC/BUY: illegal parameter
2025-12-03 14:40:43,925 - worker.extractor - INFO - Extracted 0 offers for XOF/BTC/BUY
Traceback (most recent call last):
  File "C:\Users\DELL\Desktop\dashboards\worker\extractor.py", line 308, in extract_all_offers
    for future in as_completed(future_to_pair):
                  ~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "C:\Python313\Lib\concurrent\futures\_base.py", line 243, in as_completed
    waiter.event.wait(wait_timeout)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
  File "C:\Python313\Lib\threading.py", line 659, in wait
    signaled = self._cond.wait(timeout)
  File "C:\Python313\Lib\threading.py", line 359, in wait
    waiter.acquire()
    ~~~~~~~~~~~~~~^^
KeyboardInterrupt

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\DELL\Desktop\dashboards\worker\main.py", line 56, in <module>
    main()
    ~~~~^^
  File "C:\Users\DELL\Desktop\dashboards\worker\main.py", line 52, in main
    schedule.run_pending()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\schedule\__init__.py", line 854, in run_pending   
    default_scheduler.run_pending()
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\schedule\__init__.py", line 101, in run_pending   
    self._run_job(job)
    ~~~~~~~~~~~~~^^^^^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\schedule\__init__.py", line 173, in _run_job      
    ret = job.run()
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\schedule\__init__.py", line 691, in run
    ret = self.job_func()
  File "C:\Users\DELL\Desktop\dashboards\worker\main.py", line 27, in job
    offers = extractor.extract_all_offers()
  File "C:\Users\DELL\Desktop\dashboards\worker\extractor.py", line 295, in extract_all_offers
    with ThreadPoolExecutor(max_workers=settings.max_workers) as executor:
         ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python313\Lib\concurrent\futures\_base.py", line 647, in __exit__
    self.shutdown(wait=True)
    ~~~~~~~~~~~~~^^^^^^^^^^^
  File "C:\Python313\Lib\concurrent\futures\thread.py", line 239, in shutdown
    t.join()
    ~~~~~~^^
  File "C:\Python313\Lib\threading.py", line 1094, in join
    self._handle.join(timeout)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^
KeyboardInterrupt
2025-12-03 14:40:44,964 - worker.extractor - ERROR - Failed to extract XOF/BTC/SELL: illegal parameter
2025-12-03 14:40:44,965 - worker.extractor - INFO - Extracted 0 offers for XOF/BTC/SELL
2025-12-03 14:40:45,194 - worker.extractor - ERROR - Failed to extract XOF/ETH/BUY: illegal parameter
2025-12-03 14:40:45,723 - worker.extractor - ERROR - Failed to extract XOF/ETH/SELL: illegal parameter
2025-12-03 14:40:45,724 - worker.extractor - INFO - Extracted 0 offers for XOF/ETH/SELL
2025-12-03 14:40:46,352 - worker.extractor - ERROR - Failed to extract RWF/USDT/BUY: illegal parameter
2025-12-03 14:40:46,353 - worker.extractor - INFO - Extracted 0 offers for RWF/USDT/BUY
2025-12-03 14:40:46,921 - worker.extractor - ERROR - Failed to extract RWF/USDT/SELL: illegal parameter
2025-12-03 14:40:46,932 - worker.extractor - INFO - Extracted 0 offers for RWF/USDT/SELL
2025-12-03 14:40:47,628 - worker.extractor - ERROR - Failed to extract RWF/BTC/BUY: illegal parameter
2025-12-03 14:40:47,629 - worker.extractor - INFO - Extracted 0 offers for RWF/BTC/BUY
2025-12-03 14:40:47,934 - worker.rate_limiter - WARNING - Rate limiter active: 1330 waits, 1428 total requests
2025-12-03 14:40:48,191 - worker.extractor - ERROR - Failed to extract RWF/BTC/SELL: illegal parameter
2025-12-03 14:40:48,192 - worker.extractor - INFO - Extracted 0 offers for RWF/BTC/SELL
2025-12-03 14:40:48,957 - worker.extractor - ERROR - Failed to extract RWF/ETH/BUY: illegal parameter
2025-12-03 14:40:48,958 - worker.extractor - INFO - Extracted 0 offers for RWF/ETH/BUY
2025-12-03 14:40:49,420 - worker.extractor - ERROR - Failed to extract RWF/ETH/SELL: illegal parameter
2025-12-03 14:40:49,420 - worker.extractor - INFO - Extracted 0 offers for RWF/ETH/SELL
(.venv) PS C:\Users\DELL\Desktop\dashboards> python -m worker.main 
2025-12-03 14:46:49,303 - __main__ - INFO - Worker starting. Job will run every 10 minutes.
2025-12-03 14:46:49,305 - __main__ - INFO - Starting P2P data extraction job...
2025-12-03 14:46:49,306 - worker.extractor - INFO - Fetching all trading pairs...
2025-12-03 14:46:51,102 - worker.extractor - INFO - Found 119 fiat currencies: ['AFN', 'ALL', 'AOA', 'AZN', 'BAM', 'BIF', 'BND', 'BSD', 'BWP', 'BYN', 'BZD', 'CDF', 'CNY', 'CRC', 'CVE', 'DJF', 'DKK', 'ERN', 'GMD', 'GNF', 'GTQ', 'HNL', 'HTG', 'HUF', 'IQD', 'ISK', 'JMD', 'JOD', 'KGS', 'KMF', 'KWD', 'KYD', 'LRD', 'LYD', 'MDL', 'MGA', 'MKD', 'MOP', 'MRU', 'MWK', 'MZN', 'NAD', 'NIO', 'NOK', 'PGK', 'RSD', 'SCR', 'SLE', 'SOS', 'SYP', 'TJS', 'TMT', 'TTD', 'YER', 'ZMW', 'ZWG', 'VND', 'UAH', 'EUR', 'COP', 'BRL', 'ARS', 'PEN', 'ZAR', 'MXN', 'HKD', 'GBP', 'KES', 'AUD', 'CAD', 'VES', 'INR', 'IDR', 'KZT', 'USD', 'JPY', 'THB', 'PHP', 'TWD', 'SAR', 'BDT', 'EGP', 'AED', 'BGN', 'MAD', 'PLN', 'PKR', 'RON', 'CHF', 'CZK', 'SEK', 'TRY', 'UGX', 'LBP', 'AMD', 'GEL', 'UYU', 'CLP', 'XAF', 'DZD', 'PYG', 'BOB', 'LKR', 'PAB', 'NZD', 'KHR', 'LAK', 'DOP', 'QAR', 'BHD', 'OMR', 'TND', 'SDG', 'MNT', 'UZS', 'NPR', 'TZS', 'XOF', 'RWF']
2025-12-03 14:46:51,106 - worker.extractor - INFO - Generated 714 dummy trading pairs.
2025-12-03 14:46:51,107 - worker.extractor - INFO - Starting parallel extraction for 714 pairs...
2025-12-03 14:46:51,115 - worker.extractor - INFO - Extracting AFN/USDT/BUY
2025-12-03 14:46:51,122 - worker.extractor - INFO - Extracting AFN/USDT/SELL
2025-12-03 14:46:51,132 - worker.extractor - INFO - Extracting AFN/BTC/BUY
2025-12-03 14:46:51,146 - worker.extractor - INFO - Extracting AFN/BTC/SELL
2025-12-03 14:46:51,180 - worker.extractor - INFO - Extracting AFN/ETH/BUY
2025-12-03 14:46:51,202 - worker.extractor - INFO - Extracting AFN/ETH/SELL
2025-12-03 14:46:51,289 - worker.extractor - INFO - Extracting ALL/USDT/BUY
2025-12-03 14:46:51,311 - worker.extractor - INFO - Extracting ALL/USDT/SELL
2025-12-03 14:46:51,402 - worker.extractor - ERROR - Failed to extract AFN/USDT/BUY: illegal parameter
2025-12-03 14:46:51,406 - worker.extractor - INFO - Extracted 0 offers for AFN/USDT/BUY
2025-12-03 14:46:51,407 - worker.extractor - INFO - Extracting ALL/BTC/BUY
2025-12-03 14:46:51,428 - worker.extractor - INFO - Extracting ALL/BTC/SELL
2025-12-03 14:46:51,549 - worker.extractor - INFO - Extracting ALL/ETH/BUY
2025-12-03 14:46:51,682 - worker.extractor - ERROR - Failed to extract ALL/USDT/SELL: illegal parameter
2025-12-03 14:46:51,761 - worker.extractor - INFO - Extracted 0 offers for ALL/USDT/SELL
2025-12-03 14:46:51,767 - worker.extractor - INFO - Extracting ALL/ETH/SELL
2025-12-03 14:46:51,768 - worker.extractor - INFO - Extracting AOA/USDT/BUY
2025-12-03 14:46:51,870 - worker.extractor - INFO - Extracting AOA/USDT/SELL
2025-12-03 14:46:51,981 - worker.extractor - INFO - Extracting AOA/BTC/BUY
2025-12-03 14:46:52,041 - worker.extractor - INFO - Extracting AOA/BTC/SELL
2025-12-03 14:46:52,048 - worker.extractor - ERROR - Failed to extract ALL/ETH/BUY: illegal parameter
2025-12-03 14:46:52,227 - worker.extractor - INFO - Extracting AOA/ETH/BUY
2025-12-03 14:46:52,357 - worker.extractor - ERROR - Failed to extract AOA/USDT/BUY: illegal parameter
2025-12-03 14:46:52,391 - worker.extractor - INFO - Extracted 0 offers for ALL/ETH/BUY
2025-12-03 14:46:52,566 - worker.extractor - INFO - Extracting AOA/ETH/SELL
2025-12-03 14:46:52,627 - worker.extractor - INFO - Extracted 0 offers for AOA/USDT/BUY
2025-12-03 14:46:52,628 - worker.extractor - INFO - Extracting AZN/USDT/BUY
2025-12-03 14:46:52,801 - worker.extractor - INFO - Extracting AZN/USDT/SELL
2025-12-03 14:46:52,897 - worker.extractor - ERROR - Failed to extract AOA/ETH/BUY: illegal parameter
2025-12-03 14:46:52,961 - worker.extractor - INFO - Extracting AZN/BTC/BUY
2025-12-03 14:46:53,245 - worker.extractor - INFO - Extracting AZN/BTC/SELL
2025-12-03 14:46:53,246 - worker.extractor - INFO - Extracting AZN/ETH/BUY
2025-12-03 14:46:53,528 - worker.extractor - ERROR - Failed to extract AOA/ETH/SELL: illegal parameter
2025-12-03 14:46:53,544 - worker.extractor - INFO - Extracting AZN/ETH/SELL
2025-12-03 14:46:54,028 - worker.extractor - INFO - Extracted 0 offers for AOA/ETH/BUY
2025-12-03 14:46:54,110 - worker.extractor - ERROR - Failed to extract AZN/USDT/BUY: illegal parameter
2025-12-03 14:46:54,822 - worker.extractor - ERROR - Failed to extract AZN/BTC/BUY: illegal parameter
2025-12-03 14:46:54,881 - worker.extractor - INFO - Extracted 0 offers for AOA/ETH/SELL
2025-12-03 14:46:55,108 - worker.extractor - INFO - Extracting BAM/USDT/BUY
2025-12-03 14:46:55,118 - worker.extractor - INFO - Extracted 0 offers for AZN/USDT/BUY
2025-12-03 14:46:55,128 - worker.extractor - INFO - Extracted 0 offers for AZN/BTC/BUY
2025-12-03 14:46:55,129 - worker.extractor - INFO - Extracting BAM/USDT/SELL
2025-12-03 14:46:55,187 - worker.extractor - ERROR - Failed to extract AZN/ETH/BUY: illegal parameter
2025-12-03 14:46:55,516 - worker.extractor - INFO - Extracting BAM/BTC/BUY
2025-12-03 14:46:55,739 - worker.extractor - INFO - Extracting BAM/BTC/SELL
2025-12-03 14:46:55,824 - worker.extractor - ERROR - Failed to extract BAM/USDT/BUY: illegal parameter
2025-12-03 14:46:56,061 - worker.extractor - INFO - Extracted 0 offers for AZN/ETH/BUY
2025-12-03 14:46:56,373 - worker.extractor - ERROR - Failed to extract BAM/USDT/SELL: illegal parameter
2025-12-03 14:46:56,508 - worker.extractor - INFO - Extracted 0 offers for BAM/USDT/BUY
2025-12-03 14:46:56,555 - worker.extractor - INFO - Extracting BAM/ETH/BUY
2025-12-03 14:46:56,841 - worker.extractor - ERROR - Failed to extract BAM/BTC/SELL: illegal parameter
2025-12-03 14:46:56,902 - worker.extractor - INFO - Extracted 0 offers for BAM/USDT/SELL
2025-12-03 14:46:57,211 - worker.extractor - INFO - Extracting BAM/ETH/SELL
2025-12-03 14:46:57,749 - worker.extractor - INFO - Extracted 0 offers for BAM/BTC/SELL
2025-12-03 14:46:58,215 - worker.extractor - INFO - Extracting BIF/USDT/SELL
2025-12-03 14:46:58,049 - worker.extractor - INFO - Extracting BIF/USDT/BUY
2025-12-03 14:46:57,904 - worker.extractor - ERROR - Failed to extract BAM/ETH/BUY: illegal parameter
2025-12-03 14:46:58,320 - worker.extractor - ERROR - Failed to extract AFN/USDT/SELL: illegal parameter
2025-12-03 14:46:58,448 - worker.extractor - ERROR - Failed to extract ALL/USDT/BUY: illegal parameter
2025-12-03 14:46:58,559 - worker.extractor - ERROR - Failed to extract AFN/BTC/SELL: illegal parameter
2025-12-03 14:46:58,586 - worker.extractor - ERROR - Failed to extract BAM/ETH/SELL: illegal parameter
2025-12-03 14:46:58,637 - worker.extractor - ERROR - Failed to extract AFN/ETH/SELL: illegal parameter
2025-12-03 14:46:58,696 - worker.extractor - ERROR - Failed to extract BIF/USDT/SELL: illegal parameter
2025-12-03 14:46:58,737 - worker.extractor - INFO - Extracted 0 offers for BAM/ETH/BUY
2025-12-03 14:46:58,817 - worker.extractor - ERROR - Failed to extract BIF/USDT/BUY: illegal parameter
2025-12-03 14:46:58,847 - worker.extractor - ERROR - Failed to extract ALL/BTC/BUY: illegal parameter
2025-12-03 14:46:58,859 - worker.extractor - INFO - Extracted 0 offers for AFN/USDT/SELL
2025-12-03 14:46:58,882 - worker.extractor - ERROR - Failed to extract AFN/BTC/BUY: illegal parameter
2025-12-03 14:46:58,919 - worker.extractor - ERROR - Failed to extract AFN/ETH/BUY: illegal parameter
2025-12-03 14:46:58,974 - worker.extractor - INFO - Extracted 0 offers for ALL/USDT/BUY
2025-12-03 14:46:59,036 - worker.extractor - ERROR - Failed to extract ALL/BTC/SELL: illegal parameter
2025-12-03 14:46:59,091 - worker.extractor - INFO - Extracted 0 offers for AFN/BTC/SELL
2025-12-03 14:46:59,150 - worker.extractor - ERROR - Failed to extract ALL/ETH/SELL: illegal parameter
2025-12-03 14:46:59,168 - worker.extractor - INFO - Extracted 0 offers for BAM/ETH/SELL
2025-12-03 14:46:59,241 - worker.extractor - INFO - Extracted 0 offers for AFN/ETH/SELL
2025-12-03 14:46:59,313 - worker.extractor - INFO - Extracted 0 offers for BIF/USDT/SELL
2025-12-03 14:46:59,386 - worker.extractor - INFO - Extracting BIF/BTC/BUY
2025-12-03 14:46:59,421 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 14:46:59,458 - worker.extractor - INFO - Extracted 0 offers for BIF/USDT/BUY
2025-12-03 14:46:59,462 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 14:46:59,532 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 14:46:59,536 - worker.extractor - INFO - Extracted 0 offers for ALL/BTC/BUY
2025-12-03 14:46:59,639 - worker.extractor - INFO - Extracting BIF/BTC/SELL
2025-12-03 14:46:59,735 - worker.extractor - INFO - Extracted 0 offers for AFN/BTC/BUY
2025-12-03 14:46:59,828 - worker.extractor - INFO - Extracted 0 offers for AFN/ETH/BUY
2025-12-03 14:46:59,896 - worker.extractor - INFO - Extracting BIF/ETH/BUY
2025-12-03 14:46:59,967 - worker.extractor - INFO - Extracted 0 offers for ALL/BTC/SELL
2025-12-03 14:47:00,021 - worker.extractor - INFO - Extracting BIF/ETH/SELL
2025-12-03 14:47:00,111 - worker.extractor - INFO - Extracted 0 offers for ALL/ETH/SELL
2025-12-03 14:47:00,216 - worker.extractor - INFO - Extracting BND/USDT/BUY
2025-12-03 14:47:00,313 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 14:47:00,320 - worker.extractor - INFO - Extracting BND/USDT/SELL
2025-12-03 14:47:00,394 - worker.extractor - INFO - Extracting BND/BTC/BUY
2025-12-03 14:47:00,484 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 14:47:00,507 - worker.extractor - ERROR - Failed to extract AOA/USDT/SELL: illegal parameter
2025-12-03 14:47:00,611 - worker.extractor - INFO - Extracting BND/BTC/SELL
2025-12-03 14:47:00,619 - worker.extractor - ERROR - Failed to extract AZN/ETH/SELL: illegal parameter
2025-12-03 14:47:00,699 - worker.extractor - ERROR - Failed to extract AOA/BTC/BUY: illegal parameter
2025-12-03 14:47:00,760 - worker.extractor - ERROR - Failed to extract AOA/BTC/SELL: illegal parameter
2025-12-03 14:47:00,770 - worker.extractor - INFO - Extracting BND/ETH/BUY
2025-12-03 14:47:00,780 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 14:47:00,786 - worker.extractor - INFO - Extracting BND/ETH/SELL
2025-12-03 14:47:00,859 - worker.extractor - INFO - Extracting BSD/USDT/BUY
2025-12-03 14:47:00,890 - worker.extractor - INFO - Extracting BSD/USDT/SELL
2025-12-03 14:47:00,957 - worker.extractor - INFO - Extracting BSD/BTC/BUY
2025-12-03 14:47:01,064 - worker.extractor - ERROR - Failed to extract BIF/BTC/SELL: illegal parameter
2025-12-03 14:47:01,354 - worker.extractor - INFO - Extracted 0 offers for BIF/BTC/SELL
2025-12-03 14:47:01,114 - worker.extractor - ERROR - Failed to extract AZN/BTC/SELL: illegal parameter
2025-12-03 14:47:01,369 - worker.extractor - INFO - Extracted 0 offers for AZN/BTC/SELL
2025-12-03 14:47:01,170 - worker.extractor - INFO - Extracted 0 offers for AOA/USDT/SELL
2025-12-03 14:47:01,172 - worker.extractor - ERROR - Failed to extract BIF/ETH/BUY: illegal parameter
2025-12-03 14:47:01,177 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 14:47:01,192 - worker.extractor - INFO - Extracted 0 offers for AZN/ETH/SELL
2025-12-03 14:47:01,197 - worker.extractor - INFO - Extracted 0 offers for AOA/BTC/BUY
2025-12-03 14:47:01,240 - worker.extractor - INFO - Extracted 0 offers for AOA/BTC/SELL
2025-12-03 14:47:01,260 - worker.extractor - ERROR - Failed to extract BIF/BTC/BUY: illegal parameter
2025-12-03 14:47:01,099 - worker.extractor - ERROR - Failed to extract AZN/USDT/SELL: illegal parameter
2025-12-03 14:47:01,355 - worker.extractor - INFO - Extracting BSD/BTC/SELL
2025-12-03 14:47:01,129 - worker.extractor - ERROR - Failed to extract BAM/BTC/BUY: illegal parameter
2025-12-03 14:47:01,373 - worker.extractor - INFO - Extracting BSD/ETH/BUY
2025-12-03 14:47:01,395 - worker.extractor - INFO - Extracting BSD/ETH/SELL
2025-12-03 14:47:01,400 - worker.extractor - INFO - Extracted 0 offers for BIF/ETH/BUY
2025-12-03 14:47:01,408 - worker.extractor - ERROR - Failed to extract BIF/ETH/SELL: illegal parameter
2025-12-03 14:47:01,426 - worker.extractor - INFO - Extracting BWP/USDT/BUY
2025-12-03 14:47:01,429 - worker.extractor - INFO - Extracting BWP/USDT/SELL
2025-12-03 14:47:01,450 - worker.extractor - INFO - Extracting BWP/BTC/BUY
2025-12-03 14:47:01,460 - worker.extractor - INFO - Extracted 0 offers for BIF/BTC/BUY
2025-12-03 14:47:01,461 - worker.extractor - INFO - Extracted 0 offers for AZN/USDT/SELL
2025-12-03 14:47:01,480 - worker.extractor - INFO - Extracted 0 offers for BAM/BTC/BUY
2025-12-03 14:47:01,496 - worker.extractor - INFO - Extracting BWP/BTC/SELL
2025-12-03 14:47:01,512 - worker.extractor - INFO - Extracted 0 offers for BIF/ETH/SELL
2025-12-03 14:47:01,521 - worker.extractor - INFO - Extracting BWP/ETH/BUY
2025-12-03 14:47:01,532 - worker.extractor - INFO - Extracting BWP/ETH/SELL
2025-12-03 14:47:01,551 - worker.extractor - INFO - Extracting BYN/USDT/BUY
2025-12-03 14:47:01,567 - worker.extractor - INFO - Extracting BYN/USDT/SELL
2025-12-03 14:47:01,613 - worker.extractor - ERROR - Failed to extract BND/USDT/BUY: illegal parameter
2025-12-03 14:47:01,627 - worker.extractor - INFO - Extracted 0 offers for BND/USDT/BUY
2025-12-03 14:47:01,628 - worker.extractor - INFO - Extracting BYN/BTC/BUY
2025-12-03 14:47:02,222 - worker.extractor - ERROR - Failed to extract BND/USDT/SELL: illegal parameter
2025-12-03 14:47:02,240 - worker.extractor - INFO - Extracted 0 offers for BND/USDT/SELL
2025-12-03 14:47:02,262 - worker.extractor - INFO - Extracting BYN/BTC/SELL
2025-12-03 14:47:02,806 - worker.extractor - ERROR - Failed to extract BND/BTC/BUY: illegal parameter
2025-12-03 14:47:02,807 - worker.extractor - INFO - Extracted 0 offers for BND/BTC/BUY
2025-12-03 14:47:02,808 - worker.extractor - INFO - Extracting BYN/ETH/BUY
2025-12-03 14:47:03,414 - worker.extractor - ERROR - Failed to extract BND/BTC/SELL: illegal parameter
2025-12-03 14:47:03,415 - worker.extractor - INFO - Extracted 0 offers for BND/BTC/SELL
2025-12-03 14:47:03,416 - worker.extractor - INFO - Extracting BYN/ETH/SELL
2025-12-03 14:47:04,036 - worker.extractor - ERROR - Failed to extract BND/ETH/BUY: illegal parameter
2025-12-03 14:47:04,036 - worker.extractor - INFO - Extracted 0 offers for BND/ETH/BUY
2025-12-03 14:47:04,037 - worker.extractor - INFO - Extracting BZD/USDT/BUY
2025-12-03 14:47:04,632 - worker.extractor - ERROR - Failed to extract BND/ETH/SELL: illegal parameter
2025-12-03 14:47:04,637 - worker.extractor - INFO - Extracted 0 offers for BND/ETH/SELL
2025-12-03 14:47:04,637 - worker.extractor - INFO - Extracting BZD/USDT/SELL
2025-12-03 14:47:05,206 - worker.extractor - ERROR - Failed to extract BSD/USDT/BUY: illegal parameter
2025-12-03 14:47:05,207 - worker.extractor - INFO - Extracted 0 offers for BSD/USDT/BUY
2025-12-03 14:47:05,207 - worker.extractor - INFO - Extracting BZD/BTC/BUY
2025-12-03 14:47:05,846 - worker.extractor - ERROR - Failed to extract BSD/USDT/SELL: illegal parameter
2025-12-03 14:47:05,847 - worker.extractor - INFO - Extracted 0 offers for BSD/USDT/SELL
2025-12-03 14:47:05,848 - worker.extractor - INFO - Extracting BZD/BTC/SELL
2025-12-03 14:47:06,409 - worker.extractor - ERROR - Failed to extract BSD/BTC/BUY: illegal parameter
2025-12-03 14:47:06,437 - worker.extractor - INFO - Extracted 0 offers for BSD/BTC/BUY
2025-12-03 14:47:06,438 - worker.extractor - INFO - Extracting BZD/ETH/BUY
2025-12-03 14:47:06,804 - worker.rate_limiter - WARNING - Rate limiter active: 10 waits, 47 total requests
2025-12-03 14:47:07,096 - worker.extractor - ERROR - Failed to extract BSD/BTC/SELL: illegal parameter
2025-12-03 14:47:07,096 - worker.extractor - INFO - Extracted 0 offers for BSD/BTC/SELL
2025-12-03 14:47:07,097 - worker.extractor - INFO - Extracting BZD/ETH/SELL
2025-12-03 14:47:07,827 - worker.extractor - ERROR - Failed to extract BSD/ETH/BUY: illegal parameter
2025-12-03 14:47:07,830 - worker.extractor - INFO - Extracted 0 offers for BSD/ETH/BUY
2025-12-03 14:47:07,831 - worker.extractor - INFO - Extracting CDF/USDT/BUY
2025-12-03 14:47:08,277 - worker.extractor - ERROR - Failed to extract BSD/ETH/SELL: illegal parameter
2025-12-03 14:47:08,278 - worker.extractor - INFO - Extracted 0 offers for BSD/ETH/SELL
2025-12-03 14:47:08,278 - worker.extractor - INFO - Extracting CDF/USDT/SELL
2025-12-03 14:47:08,877 - worker.extractor - ERROR - Failed to extract BWP/USDT/BUY: illegal parameter
2025-12-03 14:47:08,879 - worker.extractor - INFO - Extracted 0 offers for BWP/USDT/BUY
2025-12-03 14:47:08,879 - worker.extractor - INFO - Extracting CDF/BTC/BUY


sixth run

2025-12-03 14:53:54,417 - worker.extractor - INFO - Extracted 0 offers for TZS/ETH/SELL
2025-12-03 14:53:55,006 - worker.extractor - ERROR - Failed to extract XOF/USDT/BUY: illegal parameter
2025-12-03 14:53:55,007 - worker.extractor - INFO - Extracted 0 offers for XOF/USDT/BUY
2025-12-03 14:53:55,633 - worker.extractor - ERROR - Failed to extract XOF/USDT/SELL: illegal parameter
2025-12-03 14:53:55,633 - worker.extractor - INFO - Extracted 0 offers for XOF/USDT/SELL
2025-12-03 14:53:56,229 - worker.extractor - ERROR - Failed to extract XOF/BTC/BUY: illegal parameter
2025-12-03 14:53:56,229 - worker.extractor - INFO - Extracted 0 offers for XOF/BTC/BUY
2025-12-03 14:53:56,851 - worker.extractor - ERROR - Failed to extract XOF/BTC/SELL: illegal parameter
2025-12-03 14:53:56,855 - worker.extractor - INFO - Extracted 0 offers for XOF/BTC/SELL
2025-12-03 14:53:57,436 - worker.extractor - ERROR - Failed to extract XOF/ETH/BUY: illegal parameter
2025-12-03 14:53:57,437 - worker.extractor - INFO - Extracted 0 offers for XOF/ETH/BUY
2025-12-03 14:53:57,786 - worker.rate_limiter - WARNING - Rate limiter active: 670 waits, 709 total requests
2025-12-03 14:53:58,144 - worker.extractor - ERROR - Failed to extract XOF/ETH/SELL: illegal parameter
2025-12-03 14:53:58,213 - worker.extractor - INFO - Extracted 0 offers for XOF/ETH/SELL
2025-12-03 14:53:58,656 - worker.extractor - ERROR - Failed to extract RWF/USDT/BUY: illegal parameter
2025-12-03 14:53:58,657 - worker.extractor - INFO - Extracted 0 offers for RWF/USDT/BUY
2025-12-03 14:53:59,298 - worker.extractor - ERROR - Failed to extract RWF/USDT/SELL: illegal parameter
2025-12-03 14:53:59,309 - worker.extractor - INFO - Extracted 0 offers for RWF/USDT/SELL
2025-12-03 14:53:59,908 - worker.extractor - ERROR - Failed to extract RWF/BTC/BUY: illegal parameter
2025-12-03 14:53:59,911 - worker.extractor - INFO - Extracted 0 offers for RWF/BTC/BUY
2025-12-03 14:54:00,477 - worker.extractor - ERROR - Failed to extract RWF/BTC/SELL: illegal parameter
2025-12-03 14:54:00,478 - worker.extractor - INFO - Extracted 0 offers for RWF/BTC/SELL
2025-12-03 14:54:01,098 - worker.extractor - ERROR - Failed to extract RWF/ETH/BUY: illegal parameter
2025-12-03 14:54:01,122 - worker.extractor - INFO - Extracted 0 offers for RWF/ETH/BUY
2025-12-03 14:54:01,729 - worker.extractor - ERROR - Failed to extract RWF/ETH/SELL: illegal parameter
2025-12-03 14:54:01,735 - worker.extractor - INFO - Extracted 0 offers for RWF/ETH/SELL
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\DELL\Desktop\dashboards\worker\main.py", line 56, in <module>
    main()
    ~~~~^^
  File "C:\Users\DELL\Desktop\dashboards\worker\main.py", line 46, in main
    job()
  File "C:\Users\DELL\Desktop\dashboards\worker\main.py", line 27, in job
    offers = extractor.extract_all_offers()
  File "C:\Users\DELL\Desktop\dashboards\worker\extractor.py", line 316, in extract_all_offers
    for future in as_completed(future_to_pair):
                  ~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "C:\Python313\Lib\concurrent\futures\_base.py", line 243, in as_completed
    waiter.event.wait(wait_timeout)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
  File "C:\Python313\Lib\threading.py", line 659, in wait
    signaled = self._cond.wait(timeout)
  File "C:\Python313\Lib\threading.py", line 359, in wait
    waiter.acquire()
    ~~~~~~~~~~~~~~^^
KeyboardInterrupt
(.venv) PS C:\Users\DELL\Desktop\dashboards> ^C
(.venv) PS C:\Users\DELL\Desktop\dashboards> python -m worker.main 
2025-12-03 15:19:10,486 - __main__ - INFO - Worker starting. Job will run every 10 minutes.
2025-12-03 15:19:10,488 - __main__ - INFO - Starting P2P data extraction job...
2025-12-03 15:19:10,489 - worker.extractor - INFO - Fetching all trading pairs...
2025-12-03 15:19:10,489 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v1/friendly/c2c/trade-rule/fiat-list
2025-12-03 15:19:13,258 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:13,259 - worker.extractor - INFO - Found 119 fiat currencies: ['AFN', 'ALL', 'AOA', 'AZN', 'BAM', 'BIF', 'BND', 'BSD', 'BWP', 'BYN', 'BZD', 'CDF', 'CNY', 'CRC', 'CVE', 'DJF', 'DKK', 'ERN', 'GMD', 'GNF', 'GTQ', 'HNL', 'HTG', 'HUF', 'IQD', 'ISK', 'JMD', 'JOD', 'KGS', 'KMF', 'KWD', 'KYD', 'LRD', 'LYD', 'MDL', 'MGA', 'MKD', 'MOP', 'MRU', 'MWK', 'MZN', 'NAD', 'NIO', 'NOK', 'PGK', 'RSD', 'SCR', 'SLE', 'SOS', 'SYP', 'TJS', 'TMT', 'TTD', 'YER', 'ZMW', 'ZWG', 'VND', 'UAH', 'EUR', 'COP', 'BRL', 'ARS', 'PEN', 'ZAR', 'MXN', 'HKD', 'GBP', 'KES', 'AUD', 'CAD', 'VES', 'INR', 'IDR', 'KZT', 'USD', 'JPY', 'THB', 'PHP', 'TWD', 'SAR', 'BDT', 'EGP', 'AED', 'BGN', 'MAD', 'PLN', 'PKR', 'RON', 'CHF', 'CZK', 'SEK', 'TRY', 'UGX', 'LBP', 'AMD', 'GEL', 'UYU', 'CLP', 'XAF', 'DZD', 'PYG', 'BOB', 'LKR', 'PAB', 'NZD', 'KHR', 'LAK', 'DOP', 'QAR', 'BHD', 'OMR', 'TND', 'SDG', 'MNT', 'UZS', 'NPR', 'TZS', 'XOF', 'RWF']
2025-12-03 15:19:13,262 - worker.extractor - INFO - Generated 714 dummy trading pairs.
2025-12-03 15:19:13,262 - worker.extractor - INFO - Starting parallel extraction for 714 pairs...
2025-12-03 15:19:13,267 - worker.extractor - INFO - Extracting AFN/USDT/BUY
2025-12-03 15:19:13,269 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:13,270 - worker.extractor - INFO - Extracting AFN/USDT/SELL
2025-12-03 15:19:13,271 - worker.extractor - INFO - Extracting AFN/BTC/BUY
2025-12-03 15:19:13,275 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:13,274 - worker.extractor - INFO - Extracting AFN/BTC/SELL
2025-12-03 15:19:13,272 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:13,279 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:13,289 - worker.extractor - INFO - Extracting AFN/ETH/BUY
2025-12-03 15:19:13,310 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:13,321 - worker.extractor - INFO - Extracting AFN/ETH/SELL
2025-12-03 15:19:13,324 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:13,327 - worker.extractor - INFO - Extracting ALL/USDT/BUY
2025-12-03 15:19:13,327 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:13,332 - worker.extractor - INFO - Extracting ALL/USDT/SELL
2025-12-03 15:19:13,334 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:13,452 - worker.extractor - INFO - Extracting ALL/BTC/BUY
2025-12-03 15:19:13,553 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:13,562 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:13,563 - worker.extractor - ERROR - Failed to extract AFN/USDT/BUY: illegal parameter
2025-12-03 15:19:13,710 - worker.extractor - INFO - Extracted 0 offers for AFN/USDT/BUY
2025-12-03 15:19:13,711 - worker.extractor - INFO - Extracting ALL/ETH/BUY
2025-12-03 15:19:13,628 - worker.extractor - INFO - Extracting ALL/BTC/SELL
2025-12-03 15:19:13,712 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:13,712 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:13,714 - worker.extractor - INFO - Extracting ALL/ETH/SELL
2025-12-03 15:19:13,899 - worker.extractor - INFO - Extracting AOA/USDT/BUY
2025-12-03 15:19:13,982 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:14,019 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:14,021 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:14,096 - worker.extractor - INFO - Extracting AOA/USDT/SELL
2025-12-03 15:19:14,159 - worker.extractor - ERROR - Failed to extract ALL/BTC/BUY: illegal parameter
2025-12-03 15:19:14,301 - worker.extractor - INFO - Extracting AOA/BTC/BUY
2025-12-03 15:19:14,386 - worker.extractor - INFO - Extracting AOA/BTC/SELL
2025-12-03 15:19:14,481 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:14,658 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:14,686 - worker.extractor - INFO - Extracting AOA/ETH/BUY
2025-12-03 15:19:14,686 - worker.extractor - INFO - Extracted 0 offers for ALL/BTC/BUY
2025-12-03 15:19:14,891 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:14,892 - worker.extractor - INFO - Extracting AOA/ETH/SELL
2025-12-03 15:19:15,072 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:15,151 - worker.extractor - INFO - Extracting AZN/USDT/BUY
2025-12-03 15:19:15,241 - worker.extractor - ERROR - Failed to extract ALL/ETH/SELL: illegal parameter
2025-12-03 15:19:15,354 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:15,451 - worker.extractor - INFO - Extracting AZN/USDT/SELL
2025-12-03 15:19:15,451 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:15,635 - worker.extractor - INFO - Extracting AZN/BTC/BUY
2025-12-03 15:19:15,650 - worker.extractor - INFO - Extracting AZN/BTC/SELL
2025-12-03 15:19:15,925 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:16,227 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:16,305 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:16,578 - worker.extractor - INFO - Extracted 0 offers for ALL/ETH/SELL
2025-12-03 15:19:16,935 - worker.extractor - ERROR - Failed to extract AOA/USDT/SELL: illegal parameter
2025-12-03 15:19:17,148 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:17,477 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:17,514 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:17,790 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:17,850 - worker.extractor - ERROR - Failed to extract AOA/BTC/BUY: illegal parameter
2025-12-03 15:19:18,086 - worker.extractor - INFO - Extracting AZN/ETH/BUY
2025-12-03 15:19:18,211 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:18,303 - worker.extractor - INFO - Extracted 0 offers for AOA/USDT/SELL
2025-12-03 15:19:19,127 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:19,222 - worker.extractor - ERROR - Failed to extract AOA/ETH/BUY: illegal parameter
2025-12-03 15:19:19,268 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:19,279 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:19,324 - worker.extractor - INFO - Extracted 0 offers for AOA/BTC/BUY
2025-12-03 15:19:19,391 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:19,440 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:19,468 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:19,476 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:19,760 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:19,857 - worker.extractor - ERROR - Failed to extract AOA/ETH/SELL: illegal parameter
2025-12-03 15:19:19,961 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:19,977 - worker.extractor - INFO - Extracting AZN/ETH/SELL
2025-12-03 15:19:20,132 - worker.extractor - ERROR - Failed to extract AZN/USDT/SELL: illegal parameter
2025-12-03 15:19:20,207 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:20,227 - worker.extractor - INFO - Extracted 0 offers for AOA/ETH/BUY
2025-12-03 15:19:20,310 - worker.extractor - ERROR - Failed to extract AFN/BTC/SELL: illegal parameter
2025-12-03 15:19:20,371 - worker.extractor - ERROR - Failed to extract AFN/USDT/SELL: illegal parameter
2025-12-03 15:19:20,478 - worker.extractor - INFO - Extracting BAM/USDT/BUY
2025-12-03 15:19:20,551 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:20,581 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:19:20,590 - worker.extractor - ERROR - Failed to extract ALL/USDT/BUY: illegal parameter
2025-12-03 15:19:20,741 - worker.extractor - ERROR - Failed to extract AFN/BTC/BUY: illegal parameter
2025-12-03 15:19:20,992 - worker.extractor - ERROR - Failed to extract AFN/ETH/SELL: illegal parameter
2025-12-03 15:19:21,045 - worker.extractor - ERROR - Failed to extract AFN/ETH/BUY: illegal parameter
2025-12-03 15:19:21,084 - worker.extractor - INFO - Extracted 0 offers for AOA/ETH/SELL
2025-12-03 15:19:21,129 - worker.extractor - ERROR - Failed to extract ALL/USDT/SELL: illegal parameter
2025-12-03 15:19:21,171 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:21,174 - worker.extractor - INFO - Extracted 0 offers for AZN/USDT/SELL
2025-12-03 15:19:21,201 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:21,205 - worker.extractor - ERROR - Failed to extract ALL/ETH/BUY: illegal parameter
2025-12-03 15:19:21,212 - worker.extractor - INFO - Extracting BAM/USDT/SELL
2025-12-03 15:19:21,246 - worker.extractor - INFO - Extracted 0 offers for AFN/BTC/SELL
2025-12-03 15:19:21,250 - worker.extractor - INFO - Extracted 0 offers for AFN/USDT/SELL
2025-12-03 15:19:21,286 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:21,288 - worker.extractor - ERROR - Failed to extract ALL/BTC/SELL: illegal parameter
2025-12-03 15:19:21,558 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:21,944 - worker.extractor - INFO - Extracted 0 offers for ALL/USDT/BUY
2025-12-03 15:19:21,973 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:19:22,061 - worker.extractor - INFO - Extracted 0 offers for AFN/BTC/BUY
2025-12-03 15:19:22,073 - worker.extractor - INFO - Extracted 0 offers for AFN/ETH/SELL
2025-12-03 15:19:22,080 - worker.extractor - INFO - Extracted 0 offers for AFN/ETH/BUY
2025-12-03 15:19:22,088 - worker.extractor - INFO - Extracting BAM/BTC/BUY
2025-12-03 15:19:22,088 - worker.extractor - INFO - Extracted 0 offers for ALL/USDT/SELL
2025-12-03 15:19:22,094 - worker.extractor - INFO - Extracting BAM/BTC/SELL
2025-12-03 15:19:22,099 - worker.extractor - ERROR - Failed to extract AZN/ETH/BUY: illegal parameter
2025-12-03 15:19:22,100 - worker.extractor - INFO - Extracted 0 offers for ALL/ETH/BUY
2025-12-03 15:19:22,100 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:22,102 - worker.extractor - INFO - Extracting BAM/ETH/BUY
2025-12-03 15:19:22,102 - worker.extractor - INFO - Extracting BAM/ETH/SELL
2025-12-03 15:19:22,105 - worker.extractor - INFO - Extracted 0 offers for ALL/BTC/SELL
2025-12-03 15:19:22,108 - worker.extractor - ERROR - Failed to extract AOA/USDT/BUY: illegal parameter
2025-12-03 15:19:22,109 - worker.extractor - INFO - Extracting BIF/USDT/BUY
2025-12-03 15:19:22,110 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:22,110 - worker.extractor - INFO - Extracting BIF/USDT/SELL
2025-12-03 15:19:22,111 - worker.extractor - INFO - Extracting BIF/BTC/BUY
2025-12-03 15:19:22,111 - worker.extractor - INFO - Extracting BIF/BTC/SELL
2025-12-03 15:19:22,112 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:22,113 - worker.extractor - INFO - Extracting BIF/ETH/BUY
2025-12-03 15:19:22,115 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:22,116 - worker.extractor - INFO - Extracted 0 offers for AZN/ETH/BUY
2025-12-03 15:19:22,117 - worker.extractor - INFO - Extracting BIF/ETH/SELL
2025-12-03 15:19:22,123 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:22,125 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:22,126 - worker.extractor - INFO - Extracting BND/USDT/BUY
2025-12-03 15:19:22,128 - worker.extractor - INFO - Extracted 0 offers for AOA/USDT/BUY
2025-12-03 15:19:22,128 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:22,129 - worker.extractor - ERROR - Failed to extract AOA/BTC/SELL: illegal parameter
2025-12-03 15:19:22,130 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:22,130 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:22,131 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:22,138 - worker.extractor - INFO - Extracting BND/USDT/SELL
2025-12-03 15:19:22,150 - worker.extractor - INFO - Extracting BND/BTC/BUY
2025-12-03 15:19:22,153 - worker.extractor - INFO - Extracted 0 offers for AOA/BTC/SELL
2025-12-03 15:19:22,170 - worker.extractor - INFO - Extracting BND/BTC/SELL
2025-12-03 15:19:22,269 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:22,367 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:22,367 - worker.extractor - ERROR - Failed to extract AZN/ETH/SELL: illegal parameter
2025-12-03 15:19:22,367 - worker.extractor - INFO - Extracted 0 offers for AZN/ETH/SELL
2025-12-03 15:19:22,368 - worker.extractor - INFO - Extracting BND/ETH/BUY
2025-12-03 15:19:22,370 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:22,371 - worker.extractor - ERROR - Failed to extract BAM/USDT/BUY: illegal parameter
2025-12-03 15:19:22,371 - worker.extractor - INFO - Extracted 0 offers for BAM/USDT/BUY
2025-12-03 15:19:22,372 - worker.extractor - INFO - Extracting BND/ETH/SELL
2025-12-03 15:19:22,389 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:22,390 - worker.extractor - ERROR - Failed to extract BAM/USDT/SELL: illegal parameter
2025-12-03 15:19:22,390 - worker.extractor - INFO - Extracted 0 offers for BAM/USDT/SELL
2025-12-03 15:19:22,391 - worker.extractor - INFO - Extracting BSD/USDT/BUY
2025-12-03 15:19:22,401 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:22,401 - worker.extractor - ERROR - Failed to extract BAM/BTC/SELL: illegal parameter
2025-12-03 15:19:22,402 - worker.extractor - INFO - Extracted 0 offers for BAM/BTC/SELL
2025-12-03 15:19:22,402 - worker.extractor - INFO - Extracting BSD/USDT/SELL
2025-12-03 15:19:22,406 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:22,407 - worker.extractor - ERROR - Failed to extract BAM/BTC/BUY: illegal parameter
2025-12-03 15:19:22,407 - worker.extractor - INFO - Extracted 0 offers for BAM/BTC/BUY
2025-12-03 15:19:22,408 - worker.extractor - INFO - Extracting BSD/BTC/BUY
2025-12-03 15:19:22,411 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:22,412 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:22,412 - worker.extractor - ERROR - Failed to extract BIF/USDT/SELL: illegal parameter
2025-12-03 15:19:22,413 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:22,414 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:22,414 - worker.extractor - ERROR - Failed to extract BAM/ETH/BUY: illegal parameter
2025-12-03 15:19:22,415 - worker.extractor - INFO - Extracted 0 offers for BIF/USDT/SELL
2025-12-03 15:19:22,416 - worker.extractor - ERROR - Failed to extract BIF/USDT/BUY: illegal parameter
2025-12-03 15:19:22,416 - worker.extractor - ERROR - Failed to extract BAM/ETH/SELL: illegal parameter
2025-12-03 15:19:22,417 - worker.extractor - INFO - Extracted 0 offers for BAM/ETH/BUY
2025-12-03 15:19:22,417 - worker.extractor - INFO - Extracting BSD/BTC/SELL
2025-12-03 15:19:22,418 - worker.extractor - INFO - Extracted 0 offers for BIF/USDT/BUY
2025-12-03 15:19:22,418 - worker.extractor - INFO - Extracted 0 offers for BAM/ETH/SELL
2025-12-03 15:19:22,419 - worker.extractor - INFO - Extracting BSD/ETH/BUY
2025-12-03 15:19:22,419 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:22,420 - worker.extractor - INFO - Extracting BSD/ETH/SELL
2025-12-03 15:19:22,420 - worker.extractor - INFO - Extracting BWP/USDT/BUY
2025-12-03 15:19:22,421 - worker.extractor - ERROR - Failed to extract BIF/BTC/BUY: illegal parameter
2025-12-03 15:19:22,422 - worker.extractor - INFO - Extracted 0 offers for BIF/BTC/BUY
2025-12-03 15:19:22,423 - worker.extractor - INFO - Extracting BWP/USDT/SELL
2025-12-03 15:19:22,648 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:19:22,896 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:22,873 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:19:22,867 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:19:22,904 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:22,900 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:23,044 - worker.extractor - ERROR - Failed to extract AZN/USDT/BUY: illegal parameter
2025-12-03 15:19:22,905 - worker.extractor - ERROR - Failed to extract AZN/BTC/BUY: illegal parameter
2025-12-03 15:19:23,016 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:22,897 - worker.extractor - ERROR - Failed to extract AZN/BTC/SELL: illegal parameter
2025-12-03 15:19:23,219 - worker.extractor - INFO - Extracted 0 offers for AZN/USDT/BUY
2025-12-03 15:19:23,490 - worker.extractor - INFO - Extracted 0 offers for AZN/BTC/BUY
2025-12-03 15:19:23,805 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:24,069 - worker.extractor - INFO - Extracted 0 offers for AZN/BTC/SELL
2025-12-03 15:19:24,096 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:24,177 - worker.extractor - INFO - Extracting BWP/BTC/BUY
2025-12-03 15:19:24,252 - worker.extractor - INFO - Extracting BWP/BTC/SELL
2025-12-03 15:19:24,333 - worker.extractor - INFO - Extracting BWP/ETH/BUY
2025-12-03 15:19:24,353 - worker.extractor - ERROR - Failed to extract BIF/ETH/SELL: illegal parameter
2025-12-03 15:19:24,449 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:24,479 - worker.extractor - INFO - Extracted 0 offers for BIF/ETH/SELL
2025-12-03 15:19:24,537 - worker.extractor - INFO - Extracting BWP/ETH/SELL
2025-12-03 15:19:24,667 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:24,756 - worker.extractor - ERROR - Failed to extract BND/USDT/BUY: illegal parameter
2025-12-03 15:19:24,901 - worker.extractor - INFO - Extracted 0 offers for BND/USDT/BUY
2025-12-03 15:19:25,052 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:25,061 - worker.extractor - INFO - Extracting BYN/USDT/BUY
2025-12-03 15:19:25,081 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:25,093 - worker.extractor - ERROR - Failed to extract BND/USDT/SELL: illegal parameter
2025-12-03 15:19:25,170 - worker.extractor - INFO - Extracted 0 offers for BND/USDT/SELL
2025-12-03 15:19:25,226 - worker.extractor - INFO - Extracting BYN/USDT/SELL
2025-12-03 15:19:25,417 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:25,431 - worker.extractor - ERROR - Failed to extract BND/BTC/BUY: illegal parameter
2025-12-03 15:19:25,449 - worker.extractor - INFO - Extracted 0 offers for BND/BTC/BUY
2025-12-03 15:19:25,468 - worker.extractor - INFO - Extracting BYN/BTC/BUY
2025-12-03 15:19:25,701 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:26,100 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:26,102 - worker.extractor - ERROR - Failed to extract BND/BTC/SELL: illegal parameter
2025-12-03 15:19:26,106 - worker.extractor - INFO - Extracted 0 offers for BND/BTC/SELL
2025-12-03 15:19:26,107 - worker.extractor - INFO - Extracting BYN/BTC/SELL
2025-12-03 15:19:26,242 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:19:26,244 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:26,244 - worker.extractor - ERROR - Failed to extract BIF/BTC/SELL: illegal parameter
2025-12-03 15:19:26,245 - worker.extractor - INFO - Extracted 0 offers for BIF/BTC/SELL
2025-12-03 15:19:26,249 - worker.extractor - INFO - Extracting BYN/ETH/BUY
2025-12-03 15:19:26,301 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:26,583 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:26,585 - worker.extractor - ERROR - Failed to extract BND/ETH/BUY: illegal parameter
2025-12-03 15:19:26,587 - worker.extractor - INFO - Extracted 0 offers for BND/ETH/BUY
2025-12-03 15:19:26,593 - worker.extractor - INFO - Extracting BYN/ETH/SELL
2025-12-03 15:19:26,674 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:19:26,682 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:26,684 - worker.extractor - ERROR - Failed to extract BIF/ETH/BUY: illegal parameter
2025-12-03 15:19:26,687 - worker.extractor - INFO - Extracted 0 offers for BIF/ETH/BUY
2025-12-03 15:19:26,692 - worker.extractor - INFO - Extracting BZD/USDT/BUY
2025-12-03 15:19:26,902 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:27,277 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:27,281 - worker.extractor - ERROR - Failed to extract BND/ETH/SELL: illegal parameter
2025-12-03 15:19:27,282 - worker.extractor - INFO - Extracted 0 offers for BND/ETH/SELL
2025-12-03 15:19:27,285 - worker.extractor - INFO - Extracting BZD/USDT/SELL
2025-12-03 15:19:27,505 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:27,788 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:27,796 - worker.extractor - ERROR - Failed to extract BSD/USDT/BUY: illegal parameter
2025-12-03 15:19:27,802 - worker.extractor - INFO - Extracted 0 offers for BSD/USDT/BUY
2025-12-03 15:19:27,803 - worker.extractor - INFO - Extracting BZD/BTC/BUY
2025-12-03 15:19:28,106 - worker.rate_limiter - WARNING - Rate limiter active: 10 waits, 45 total requests
2025-12-03 15:19:28,106 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:28,706 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:28,803 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:28,812 - worker.extractor - ERROR - Failed to extract BSD/USDT/SELL: illegal parameter
2025-12-03 15:19:28,817 - worker.extractor - INFO - Extracted 0 offers for BSD/USDT/SELL
2025-12-03 15:19:28,818 - worker.extractor - INFO - Extracting BZD/BTC/SELL
2025-12-03 15:19:28,970 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:28,975 - worker.extractor - ERROR - Failed to extract BSD/BTC/BUY: illegal parameter
2025-12-03 15:19:28,989 - worker.extractor - INFO - Extracted 0 offers for BSD/BTC/BUY
2025-12-03 15:19:29,007 - worker.extractor - INFO - Extracting BZD/ETH/BUY
2025-12-03 15:19:29,308 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:29,570 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:29,572 - worker.extractor - ERROR - Failed to extract BSD/BTC/SELL: illegal parameter
2025-12-03 15:19:29,575 - worker.extractor - INFO - Extracted 0 offers for BSD/BTC/SELL
2025-12-03 15:19:29,576 - worker.extractor - INFO - Extracting BZD/ETH/SELL
2025-12-03 15:19:29,914 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:30,257 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:30,258 - worker.extractor - ERROR - Failed to extract BSD/ETH/BUY: illegal parameter
2025-12-03 15:19:30,258 - worker.extractor - INFO - Extracted 0 offers for BSD/ETH/BUY
2025-12-03 15:19:30,259 - worker.extractor - INFO - Extracting CDF/USDT/BUY
2025-12-03 15:19:30,517 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:30,803 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:30,889 - worker.extractor - ERROR - Failed to extract BSD/ETH/SELL: illegal parameter
2025-12-03 15:19:31,179 - worker.extractor - INFO - Extracted 0 offers for BSD/ETH/SELL
2025-12-03 15:19:31,200 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:31,303 - worker.extractor - INFO - Extracting CDF/USDT/SELL
2025-12-03 15:19:31,639 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:31,748 - worker.extractor - ERROR - Failed to extract BWP/USDT/BUY: illegal parameter
2025-12-03 15:19:31,750 - worker.extractor - INFO - Extracted 0 offers for BWP/USDT/BUY
2025-12-03 15:19:31,751 - worker.extractor - INFO - Extracting CDF/BTC/BUY
2025-12-03 15:19:31,836 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:32,436 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:32,613 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:32,721 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:32,768 - worker.extractor - ERROR - Failed to extract BWP/USDT/SELL: illegal parameter
2025-12-03 15:19:32,853 - worker.extractor - ERROR - Failed to extract BWP/BTC/BUY: illegal parameter
2025-12-03 15:19:32,869 - worker.extractor - INFO - Extracted 0 offers for BWP/USDT/SELL
2025-12-03 15:19:32,913 - worker.extractor - INFO - Extracted 0 offers for BWP/BTC/BUY
2025-12-03 15:19:33,001 - worker.extractor - INFO - Extracting CDF/ETH/BUY
2025-12-03 15:19:32,986 - worker.extractor - INFO - Extracting CDF/BTC/SELL
2025-12-03 15:19:33,067 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:33,631 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:33,717 - worker.extractor - ERROR - Failed to extract BWP/BTC/SELL: illegal parameter
2025-12-03 15:19:33,734 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:33,801 - worker.extractor - INFO - Extracted 0 offers for BWP/BTC/SELL
2025-12-03 15:19:33,928 - worker.extractor - INFO - Extracting CDF/ETH/SELL
2025-12-03 15:19:34,304 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:34,494 - worker.extractor - ERROR - Failed to extract BWP/ETH/BUY: illegal parameter
2025-12-03 15:19:34,499 - worker.extractor - INFO - Extracted 0 offers for BWP/ETH/BUY
2025-12-03 15:19:34,499 - worker.rate_limiter - WARNING - Rate limiter active: 20 waits, 55 total requests
2025-12-03 15:19:35,042 - worker.extractor - INFO - Extracting CNY/USDT/BUY
2025-12-03 15:19:35,310 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:35,310 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:35,867 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:36,188 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:36,242 - worker.extractor - ERROR - Failed to extract BYN/USDT/BUY: illegal parameter
2025-12-03 15:19:36,276 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:36,346 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:36,347 - worker.extractor - INFO - Extracted 0 offers for BYN/USDT/BUY
2025-12-03 15:19:36,458 - worker.extractor - ERROR - Failed to extract BYN/USDT/SELL: illegal parameter
2025-12-03 15:19:36,532 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:36,554 - worker.extractor - ERROR - Failed to extract BWP/ETH/SELL: illegal parameter
2025-12-03 15:19:36,826 - worker.extractor - INFO - Extracting CNY/USDT/SELL
2025-12-03 15:19:36,847 - worker.extractor - INFO - Extracted 0 offers for BYN/USDT/SELL
2025-12-03 15:19:37,031 - worker.extractor - INFO - Extracted 0 offers for BWP/ETH/SELL
2025-12-03 15:19:37,059 - worker.extractor - INFO - Extracting CNY/BTC/BUY
2025-12-03 15:19:37,071 - worker.extractor - INFO - Extracting CNY/BTC/SELL
2025-12-03 15:19:37,151 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:37,219 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:37,266 - worker.extractor - ERROR - Failed to extract BYN/BTC/BUY: illegal parameter
2025-12-03 15:19:37,267 - worker.extractor - INFO - Extracted 0 offers for BYN/BTC/BUY
2025-12-03 15:19:37,268 - worker.extractor - INFO - Extracting CNY/ETH/BUY
2025-12-03 15:19:37,502 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:37,523 - worker.extractor - ERROR - Failed to extract BYN/BTC/SELL: illegal parameter
2025-12-03 15:19:37,551 - worker.extractor - INFO - Extracted 0 offers for BYN/BTC/SELL
2025-12-03 15:19:37,628 - worker.extractor - INFO - Extracting CNY/ETH/SELL
2025-12-03 15:19:37,800 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:38,165 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:38,187 - worker.extractor - ERROR - Failed to extract BYN/ETH/BUY: illegal parameter
2025-12-03 15:19:38,242 - worker.extractor - INFO - Extracted 0 offers for BYN/ETH/BUY
2025-12-03 15:19:38,347 - worker.extractor - INFO - Extracting CRC/USDT/BUY
2025-12-03 15:19:38,455 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:38,828 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:38,959 - worker.extractor - ERROR - Failed to extract BYN/ETH/SELL: illegal parameter
2025-12-03 15:19:38,961 - worker.extractor - INFO - Extracted 0 offers for BYN/ETH/SELL
2025-12-03 15:19:39,166 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:39,183 - worker.extractor - INFO - Extracting CRC/USDT/SELL
2025-12-03 15:19:39,516 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:39,802 - worker.extractor - ERROR - Failed to extract BZD/USDT/BUY: illegal parameter
2025-12-03 15:19:39,808 - worker.extractor - INFO - Extracted 0 offers for BZD/USDT/BUY
2025-12-03 15:19:39,923 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:39,968 - worker.extractor - INFO - Extracting CRC/BTC/BUY
2025-12-03 15:19:40,442 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:40,486 - worker.extractor - ERROR - Failed to extract BZD/USDT/SELL: illegal parameter
2025-12-03 15:19:40,543 - worker.extractor - INFO - Extracted 0 offers for BZD/USDT/SELL
2025-12-03 15:19:40,549 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:40,619 - worker.extractor - INFO - Extracting CRC/BTC/SELL
2025-12-03 15:19:41,031 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:41,057 - worker.extractor - ERROR - Failed to extract BZD/BTC/BUY: illegal parameter
2025-12-03 15:19:41,075 - worker.extractor - INFO - Extracted 0 offers for BZD/BTC/BUY
2025-12-03 15:19:41,076 - worker.extractor - INFO - Extracting CRC/ETH/BUY
2025-12-03 15:19:41,189 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:41,524 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:41,560 - worker.extractor - ERROR - Failed to extract BZD/BTC/SELL: illegal parameter
2025-12-03 15:19:41,561 - worker.extractor - INFO - Extracted 0 offers for BZD/BTC/SELL
2025-12-03 15:19:41,591 - worker.extractor - INFO - Extracting CRC/ETH/SELL
2025-12-03 15:19:41,810 - worker.rate_limiter - WARNING - Rate limiter active: 30 waits, 66 total requests
2025-12-03 15:19:41,865 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:42,190 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:42,229 - worker.extractor - ERROR - Failed to extract BZD/ETH/BUY: illegal parameter
2025-12-03 15:19:42,230 - worker.extractor - INFO - Extracted 0 offers for BZD/ETH/BUY
2025-12-03 15:19:42,301 - worker.extractor - INFO - Extracting CVE/USDT/BUY
2025-12-03 15:19:42,425 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:42,754 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:42,844 - worker.extractor - ERROR - Failed to extract BZD/ETH/SELL: illegal parameter
2025-12-03 15:19:42,845 - worker.extractor - INFO - Extracted 0 offers for BZD/ETH/SELL
2025-12-03 15:19:42,901 - worker.extractor - INFO - Extracting CVE/USDT/SELL
2025-12-03 15:19:43,035 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:19:43,356 - worker.extractor - INFO - Response status: 200
2025-12-03 15:19:43,357 - worker.extractor - ERROR - Failed to extract CDF/USDT/BUY: illegal parameter
2025-12-03 15:19:43,359 - worker.extractor - INFO - Extracted 0 offers for CDF/USDT/BUY
2025-12-03 15:19:43,361 - worker.extractor - INFO - Extracting CVE/BTC/B


# Seventh run

(.venv) PS C:\Users\DELL\Desktop\dashboards> python -m worker.main 
2025-12-03 15:35:45,906 - __main__ - INFO - Worker starting. Job will run every 10 minutes.
2025-12-03 15:35:45,906 - __main__ - INFO - Starting P2P data extraction job...
2025-12-03 15:35:45,906 - worker.extractor - INFO - Fetching all trading pairs...
2025-12-03 15:35:45,907 - worker.extractor - INFO - Generating trading pairs from p2p_config.json...
2025-12-03 15:35:45,909 - worker.extractor - INFO - Generated 28 trading pairs from configuration.
2025-12-03 15:35:45,909 - worker.extractor - INFO - Starting parallel extraction for 28 pairs...
2025-12-03 15:35:45,910 - worker.extractor - INFO - Extracting ARS/USDT/BUY
2025-12-03 15:35:45,911 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:35:45,913 - worker.extractor - INFO - Extracting ARS/USDT/SELL
2025-12-03 15:35:45,914 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:35:45,920 - worker.extractor - INFO - Extracting ARS/BTC/BUY
2025-12-03 15:35:45,921 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:35:45,931 - worker.extractor - INFO - Extracting ARS/BTC/SELL
2025-12-03 15:35:45,932 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:35:45,933 - worker.extractor - INFO - Extracting ARS/ETH/BUY
2025-12-03 15:35:45,938 - worker.extractor - INFO - Extracting ARS/ETH/SELL
2025-12-03 15:35:45,941 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:35:45,938 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:35:45,942 - worker.extractor - INFO - Extracting ARS/BNB/BUY
2025-12-03 15:35:45,953 - worker.extractor - INFO - Extracting ARS/BNB/SELL
2025-12-03 15:35:45,954 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:35:45,956 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:35:45,956 - worker.extractor - INFO - Extracting COP/USDT/BUY
2025-12-03 15:35:45,964 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:35:45,966 - worker.extractor - INFO - Extracting COP/USDT/SELL
2025-12-03 15:35:45,970 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:35:45,971 - worker.extractor - INFO - Extracting COP/BTC/BUY
2025-12-03 15:35:45,979 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:35:45,972 - worker.extractor - INFO - Extracting COP/BTC/SELL
2025-12-03 15:35:45,982 - worker.extractor - INFO - Extracting COP/ETH/BUY
2025-12-03 15:35:45,986 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:35:45,988 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:35:45,992 - worker.extractor - INFO - Extracting COP/ETH/SELL
2025-12-03 15:35:45,998 - worker.extractor - INFO - Extracting VES/USDT/BUY
2025-12-03 15:35:45,998 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:35:45,999 - worker.extractor - INFO - Extracting VES/USDT/SELL
2025-12-03 15:35:45,999 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:35:46,000 - worker.extractor - INFO - Extracting VES/BTC/BUY
2025-12-03 15:35:46,002 - worker.extractor - INFO - Extracting VES/BTC/SELL
2025-12-03 15:35:46,002 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:35:46,004 - worker.extractor - INFO - Extracting USD/USDT/BUY
2025-12-03 15:35:46,021 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:35:46,012 - worker.extractor - INFO - Extracting USD/USDT/SELL
2025-12-03 15:35:46,015 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:35:46,008 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:35:46,024 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:35:56,008 - worker.extractor - INFO - Response status: 200
2025-12-03 15:35:56,024 - worker.extractor - ERROR - Error extracting ARS/USDT/SELL: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:35:56,037 - worker.extractor - INFO - Response status: 200
2025-12-03 15:35:56,042 - worker.extractor - INFO - Extracted 6 offers for ARS/USDT/SELL
2025-12-03 15:35:56,059 - worker.extractor - ERROR - Error extracting COP/USDT/BUY: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:35:56,070 - worker.extractor - INFO - Extracting USD/BTC/BUY
2025-12-03 15:35:56,089 - worker.extractor - INFO - Extracted 6 offers for COP/USDT/BUY
2025-12-03 15:35:56,100 - worker.extractor - INFO - Response status: 200
2025-12-03 15:35:56,143 - worker.extractor - ERROR - Error extracting VES/USDT/SELL: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:35:56,157 - worker.extractor - INFO - Extracted 6 offers for VES/USDT/SELL
2025-12-03 15:35:56,158 - worker.extractor - INFO - Extracting USD/ETH/BUY
2025-12-03 15:35:56,105 - worker.extractor - INFO - Response status: 200
2025-12-03 15:35:56,181 - worker.extractor - ERROR - Error extracting USD/USDT/SELL: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:35:56,193 - worker.extractor - INFO - Extracted 6 offers for USD/USDT/SELL
2025-12-03 15:35:56,196 - worker.extractor - INFO - Extracting USD/ETH/SELL
2025-12-03 15:35:56,197 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:35:56,125 - worker.extractor - INFO - Response status: 200
2025-12-03 15:35:56,125 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:35:56,103 - worker.extractor - INFO - Response status: 200
2025-12-03 15:35:56,105 - worker.extractor - INFO - Response status: 200
2025-12-03 15:35:56,105 - worker.extractor - INFO - Response status: 200
2025-12-03 15:35:56,159 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:35:56,105 - worker.extractor - INFO - Response status: 200
2025-12-03 15:35:56,107 - worker.extractor - INFO - Response status: 200
2025-12-03 15:35:56,109 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:35:56,121 - worker.extractor - INFO - Extracting USD/BTC/SELL
2025-12-03 15:35:56,211 - worker.extractor - ERROR - Error extracting ARS/BTC/SELL: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:35:56,215 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:35:56,215 - worker.extractor - INFO - Response status: 200
2025-12-03 15:35:56,215 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:35:56,218 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:35:56,219 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:35:56,219 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:35:56,240 - worker.extractor - INFO - Response status: 200
2025-12-03 15:35:56,278 - worker.extractor - ERROR - Error extracting VES/BTC/SELL: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:35:56,307 - worker.extractor - ERROR - Error extracting COP/BTC/SELL: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:35:56,329 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:35:56,397 - worker.extractor - ERROR - Error extracting USD/USDT/BUY: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:35:56,538 - worker.extractor - INFO - Response status: 200
2025-12-03 15:35:56,547 - worker.extractor - ERROR - Error extracting COP/ETH/SELL: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:35:56,556 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:35:56,556 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:35:56,680 - worker.extractor - ERROR - Error extracting COP/ETH/BUY: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:35:56,823 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:35:56,877 - worker.extractor - INFO - Extracted 6 offers for ARS/BTC/SELL
2025-12-03 15:35:56,902 - worker.extractor - INFO - Response status: 200
2025-12-03 15:35:56,910 - worker.extractor - ERROR - Error extracting ARS/BNB/BUY: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:35:56,929 - worker.extractor - INFO - Response status: 200
2025-12-03 15:35:56,975 - worker.extractor - INFO - Response status: 200
2025-12-03 15:35:57,009 - worker.extractor - INFO - Response status: 200
2025-12-03 15:35:57,027 - worker.extractor - INFO - Response status: 200
2025-12-03 15:35:57,080 - worker.extractor - ERROR - Error extracting COP/BTC/BUY: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:35:57,093 - worker.extractor - INFO - Extracted 5 offers for VES/BTC/SELL
2025-12-03 15:35:57,108 - worker.extractor - INFO - Extracted 6 offers for COP/BTC/SELL
2025-12-03 15:35:57,127 - worker.extractor - INFO - Response status: 200
2025-12-03 15:35:57,146 - worker.extractor - INFO - Extracted 6 offers for USD/USDT/BUY
2025-12-03 15:35:57,159 - worker.extractor - ERROR - Error extracting ARS/ETH/BUY: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:35:57,176 - worker.extractor - INFO - Extracted 5 offers for COP/ETH/SELL
2025-12-03 15:35:57,257 - worker.extractor - INFO - Response status: 200
2025-12-03 15:35:57,310 - worker.extractor - INFO - Response status: 200
2025-12-03 15:35:57,349 - worker.extractor - INFO - Extracted 5 offers for COP/ETH/BUY
2025-12-03 15:35:57,500 - worker.extractor - INFO - Extracting USD/BNB/BUY
2025-12-03 15:35:57,536 - worker.extractor - INFO - Response status: 200
2025-12-03 15:35:57,536 - worker.extractor - INFO - Response status: 200
2025-12-03 15:35:57,622 - worker.extractor - ERROR - Error extracting ARS/USDT/BUY: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:35:57,758 - worker.extractor - INFO - Extracted 5 offers for ARS/BNB/BUY
2025-12-03 15:35:57,890 - worker.extractor - ERROR - Error extracting COP/USDT/SELL: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:35:57,912 - worker.extractor - ERROR - Error extracting ARS/BNB/SELL: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:35:57,978 - worker.extractor - ERROR - Error extracting ARS/BTC/BUY: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:35:58,071 - worker.extractor - ERROR - Error extracting VES/USDT/BUY: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:35:58,205 - worker.extractor - INFO - Extracted 5 offers for COP/BTC/BUY
2025-12-03 15:35:58,247 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:35:58,353 - worker.extractor - INFO - Extracting USD/BNB/SELL
2025-12-03 15:35:58,439 - worker.extractor - INFO - Extracting USD/USDC/BUY
2025-12-03 15:35:58,506 - worker.extractor - ERROR - Error extracting ARS/ETH/SELL: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:35:58,562 - worker.extractor - INFO - Extracting USD/USDC/SELL
2025-12-03 15:35:58,661 - worker.extractor - INFO - Extracted 5 offers for ARS/ETH/BUY
2025-12-03 15:35:58,828 - worker.extractor - ERROR - Error extracting USD/ETH/SELL: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:35:58,907 - worker.extractor - ERROR - Error extracting USD/ETH/BUY: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:35:59,031 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:35:59,121 - worker.extractor - ERROR - Error extracting VES/BTC/BUY: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:35:59,187 - worker.extractor - ERROR - Error extracting USD/BTC/BUY: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:35:59,277 - worker.extractor - INFO - Extracted 6 offers for ARS/USDT/BUY
2025-12-03 15:35:59,438 - worker.extractor - INFO - Extracted 6 offers for COP/USDT/SELL
2025-12-03 15:35:59,535 - worker.extractor - INFO - Extracted 5 offers for ARS/BNB/SELL
2025-12-03 15:35:59,903 - worker.extractor - INFO - Extracted 5 offers for ARS/BTC/BUY
2025-12-03 15:36:00,004 - worker.extractor - INFO - Extracted 6 offers for VES/USDT/BUY
2025-12-03 15:36:00,080 - worker.extractor - INFO - Response status: 200
2025-12-03 15:36:00,092 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:36:00,221 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:36:00,301 - worker.extractor - INFO - Extracted 5 offers for ARS/ETH/SELL
2025-12-03 15:36:00,391 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:36:00,508 - worker.extractor - INFO - Extracted 5 offers for USD/ETH/SELL
2025-12-03 15:36:00,539 - worker.extractor - INFO - Extracted 5 offers for USD/ETH/BUY
2025-12-03 15:36:00,641 - worker.extractor - INFO - Extracted 5 offers for VES/BTC/BUY
2025-12-03 15:36:00,650 - worker.extractor - INFO - Extracted 5 offers for USD/BTC/BUY
2025-12-03 15:36:00,895 - worker.extractor - INFO - Response status: 200
2025-12-03 15:36:00,901 - worker.extractor - ERROR - Error extracting USD/BTC/SELL: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:36:01,253 - worker.extractor - ERROR - Error extracting USD/BNB/BUY: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:36:01,256 - worker.extractor - INFO - Response status: 200
2025-12-03 15:36:01,303 - worker.extractor - INFO - Response status: 200
2025-12-03 15:36:01,394 - worker.extractor - INFO - Response status: 200
2025-12-03 15:36:01,402 - worker.extractor - INFO - Extracted 5 offers for USD/BTC/SELL
2025-12-03 15:36:01,520 - worker.extractor - INFO - Extracted 5 offers for USD/BNB/BUY
2025-12-03 15:36:01,731 - worker.extractor - ERROR - Error extracting USD/BNB/SELL: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:36:01,959 - worker.extractor - ERROR - Error extracting USD/USDC/BUY: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:36:02,059 - worker.extractor - ERROR - Error extracting USD/USDC/SELL: 'WorkerSettings' object has no attribute 'max_pages_per_pair'
2025-12-03 15:36:02,206 - worker.extractor - INFO - Extracted 5 offers for USD/BNB/SELL
2025-12-03 15:36:02,250 - worker.extractor - INFO - Extracted 5 offers for USD/USDC/BUY
2025-12-03 15:36:02,304 - worker.extractor - INFO - Extracted 5 offers for USD/USDC/SELL
2025-12-03 15:36:02,332 - worker.extractor - INFO - Total offers extracted: 150
2025-12-03 15:36:02,342 - worker.loader - INFO - Starting to load 150 offers for batch ca1579dc-e747-441c-998d-22114347ae17...
2025-12-03 15:36:03,119 - worker.loader - ERROR - Error loading offers for batch ca1579dc-e747-441c-998d-22114347ae17: 
(psycopg2.errors.UndefinedTable) relation "dim_cryptocurrencies" does not exist
LINE 2: FROM dim_cryptocurrencies
             ^

[SQL: SELECT dim_cryptocurrencies.crypto_id AS dim_cryptocurrencies_crypto_id, dim_cryptocurrencies.symbol AS dim_cryptocurrencies_symbol, dim_cryptocurrencies.name AS dim_cryptocurrencies_name, dim_cryptocurrencies.binance_asset_code AS 
dim_cryptocurrencies_binance_asset_code, dim_cryptocurrencies.is_active AS dim_cryptocurrencies_is_active, dim_cryptocurrencies.created_at AS dim_cryptocurrencies_created_at, dim_cryptocurrencies.updated_at AS dim_cryptocurrencies_updated_at
FROM dim_cryptocurrencies
WHERE dim_cryptocurrencies.symbol = %(symbol_1)s
 LIMIT %(param_1)s]
[parameters: {'symbol_1': 'USDT', 'param_1': 1}]
(Background on this error at: https://sqlalche.me/e/20/f405)
Traceback (most recent call last):
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1963, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\default.py", line 943, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
psycopg2.errors.UndefinedTable: relation "dim_cryptocurrencies" does not exist
LINE 2: FROM dim_cryptocurrencies
             ^


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 50, in load_offers
    self._load_dimensions(session, offers)
    ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 154, in _load_dimensions
    self._get_or_create_crypto(session, offer['asset'])
    ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 79, in _get_or_create_crypto
    crypto = session.query(DimCryptocurrencies).filter_by(symbol=symbol).first()
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\query.py", line 2759, in first     
    return self.limit(1)._iter().first()  # type: ignore
           ~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\query.py", line 2857, in _iter     
    result: Union[ScalarResult[_T], Result[_T]] = self.session.execute(
                                                  ~~~~~~~~~~~~~~~~~~~~^
        statement,
        ^^^^^^^^^^
        params,
        ^^^^^^^
        execution_options={"_sa_orm_load_options": self.load_options},
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\session.py", line 2365, in execute 
    return self._execute_internal(
           ~~~~~~~~~~~~~~~~~~~~~~^
        statement,
        ^^^^^^^^^^
    ...<4 lines>...
        _add_event=_add_event,
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\session.py", line 2251, in _execute_internal
    result: Result[Any] = compile_state_cls.orm_execute_statement(
                          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self,
        ^^^^^
    ...<4 lines>...
        conn,
        ^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\context.py", line 306, in orm_execute_statement
    result = conn.execute(
        statement, params or {}, execution_options=execution_options
    )
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1415, in execute 
    return meth(
        self,
        distilled_parameters,
        execution_options or NO_OPTIONS,
    )
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\sql\elements.py", line 523, in _execute_on_connection
    return connection._execute_clauseelement(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self, distilled_params, execution_options
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1637, in _execute_clauseelement
    ret = self._execute_context(
        dialect,
    ...<8 lines>...
        cache_hit=cache_hit,
    )
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1842, in _execute_context
    return self._exec_single_context(
           ~~~~~~~~~~~~~~~~~~~~~~~~~^
        dialect, context, statement, parameters
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1982, in _exec_single_context
    self._handle_dbapi_exception(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        e, str_statement, effective_parameters, cursor, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 2351, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1963, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\default.py", line 943, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
sqlalchemy.exc.ProgrammingError: (psycopg2.errors.UndefinedTable) relation "dim_cryptocurrencies" does not exist       
LINE 2: FROM dim_cryptocurrencies
             ^

[SQL: SELECT dim_cryptocurrencies.crypto_id AS dim_cryptocurrencies_crypto_id, dim_cryptocurrencies.symbol AS dim_cryptocurrencies_symbol, dim_cryptocurrencies.name AS dim_cryptocurrencies_name, dim_cryptocurrencies.binance_asset_code AS 
dim_cryptocurrencies_binance_asset_code, dim_cryptocurrencies.is_active AS dim_cryptocurrencies_is_active, dim_cryptocurrencies.created_at AS dim_cryptocurrencies_created_at, dim_cryptocurrencies.updated_at AS dim_cryptocurrencies_updated_at
FROM dim_cryptocurrencies
WHERE dim_cryptocurrencies.symbol = %(symbol_1)s
 LIMIT %(param_1)s]
[parameters: {'symbol_1': 'USDT', 'param_1': 1}]
(Background on this error at: https://sqlalche.me/e/20/f405)
2025-12-03 15:36:04,326 - worker.db - ERROR - Database session error: (psycopg2.errors.UndefinedTable) relation "dim_cryptocurrencies" does not exist
LINE 2: FROM dim_cryptocurrencies
             ^

[SQL: SELECT dim_cryptocurrencies.crypto_id AS dim_cryptocurrencies_crypto_id, dim_cryptocurrencies.symbol AS dim_cryptocurrencies_symbol, dim_cryptocurrencies.name AS dim_cryptocurrencies_name, dim_cryptocurrencies.binance_asset_code AS 
dim_cryptocurrencies_binance_asset_code, dim_cryptocurrencies.is_active AS dim_cryptocurrencies_is_active, dim_cryptocurrencies.created_at AS dim_cryptocurrencies_created_at, dim_cryptocurrencies.updated_at AS dim_cryptocurrencies_updated_at
FROM dim_cryptocurrencies
WHERE dim_cryptocurrencies.symbol = %(symbol_1)s
 LIMIT %(param_1)s]
[parameters: {'symbol_1': 'USDT', 'param_1': 1}]
(Background on this error at: https://sqlalche.me/e/20/f405)
2025-12-03 15:36:04,340 - __main__ - ERROR - An error occurred during the job: (psycopg2.errors.UndefinedTable) relation "dim_cryptocurrencies" does not exist
LINE 2: FROM dim_cryptocurrencies
             ^

[SQL: SELECT dim_cryptocurrencies.crypto_id AS dim_cryptocurrencies_crypto_id, dim_cryptocurrencies.symbol AS dim_cryptocurrencies_symbol, dim_cryptocurrencies.name AS dim_cryptocurrencies_name, dim_cryptocurrencies.binance_asset_code AS 
dim_cryptocurrencies_binance_asset_code, dim_cryptocurrencies.is_active AS dim_cryptocurrencies_is_active, dim_cryptocurrencies.created_at AS dim_cryptocurrencies_created_at, dim_cryptocurrencies.updated_at AS dim_cryptocurrencies_updated_at
FROM dim_cryptocurrencies
WHERE dim_cryptocurrencies.symbol = %(symbol_1)s
 LIMIT %(param_1)s]
[parameters: {'symbol_1': 'USDT', 'param_1': 1}]
(Background on this error at: https://sqlalche.me/e/20/f405)
Traceback (most recent call last):
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1963, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\default.py", line 943, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
psycopg2.errors.UndefinedTable: relation "dim_cryptocurrencies" does not exist
LINE 2: FROM dim_cryptocurrencies
             ^


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\DELL\Desktop\dashboards\worker\main.py", line 31, in job
    loader.load_offers(offers, batch_id)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 50, in load_offers
    self._load_dimensions(session, offers)
    ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 154, in _load_dimensions
    self._get_or_create_crypto(session, offer['asset'])
    ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 79, in _get_or_create_crypto
    crypto = session.query(DimCryptocurrencies).filter_by(symbol=symbol).first()
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\query.py", line 2759, in first     
    return self.limit(1)._iter().first()  # type: ignore
           ~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\query.py", line 2857, in _iter     
    result: Union[ScalarResult[_T], Result[_T]] = self.session.execute(
                                                  ~~~~~~~~~~~~~~~~~~~~^
        statement,
        ^^^^^^^^^^
        params,
        ^^^^^^^
        execution_options={"_sa_orm_load_options": self.load_options},
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\session.py", line 2365, in execute 
    return self._execute_internal(
           ~~~~~~~~~~~~~~~~~~~~~~^
        statement,
        ^^^^^^^^^^
    ...<4 lines>...
        _add_event=_add_event,
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\session.py", line 2251, in _execute_internal
    result: Result[Any] = compile_state_cls.orm_execute_statement(
                          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self,
        ^^^^^
    ...<4 lines>...
        conn,
        ^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\context.py", line 306, in orm_execute_statement
    result = conn.execute(
        statement, params or {}, execution_options=execution_options
    )
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1415, in execute 
    return meth(
        self,
        distilled_parameters,
        execution_options or NO_OPTIONS,
    )
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\sql\elements.py", line 523, in _execute_on_connection
    return connection._execute_clauseelement(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self, distilled_params, execution_options
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1637, in _execute_clauseelement
    ret = self._execute_context(
        dialect,
    ...<8 lines>...
        cache_hit=cache_hit,
    )
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1842, in _execute_context
    return self._exec_single_context(
           ~~~~~~~~~~~~~~~~~~~~~~~~~^
        dialect, context, statement, parameters
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1982, in _exec_single_context
    self._handle_dbapi_exception(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        e, str_statement, effective_parameters, cursor, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 2351, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1963, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\default.py", line 943, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
sqlalchemy.exc.ProgrammingError: (psycopg2.errors.UndefinedTable) relation "dim_cryptocurrencies" does not exist       
LINE 2: FROM dim_cryptocurrencies
             ^

[SQL: SELECT dim_cryptocurrencies.crypto_id AS dim_cryptocurrencies_crypto_id, dim_cryptocurrencies.symbol AS dim_cryptocurrencies_symbol, dim_cryptocurrencies.name AS dim_cryptocurrencies_name, dim_cryptocurrencies.binance_asset_code AS 
dim_cryptocurrencies_binance_asset_code, dim_cryptocurrencies.is_active AS dim_cryptocurrencies_is_active, dim_cryptocurrencies.created_at AS dim_cryptocurrencies_created_at, dim_cryptocurrencies.updated_at AS dim_cryptocurrencies_updated_at
FROM dim_cryptocurrencies
WHERE dim_cryptocurrencies.symbol = %(symbol_1)s
 LIMIT %(param_1)s]
[parameters: {'symbol_1': 'USDT', 'param_1': 1}]
(Background on this error at: https://sqlalche.me/e/20/f405)

# Eight Run 

(.venv) PS C:\Users\DELL\Desktop\dashboards> python -m worker.main 
2025-12-03 15:49:01,638 - __main__ - INFO - Worker starting. Job will run every 10 minutes.
2025-12-03 15:49:01,648 - __main__ - INFO - Starting P2P data extraction job...
2025-12-03 15:49:01,660 - worker.extractor - INFO - Fetching all trading pairs...
2025-12-03 15:49:01,665 - worker.extractor - INFO - Generating trading pairs from p2p_config.json...
2025-12-03 15:49:01,674 - worker.extractor - INFO - Generated 28 trading pairs from configuration.
2025-12-03 15:49:01,689 - worker.extractor - INFO - Starting parallel extraction for 28 pairs...
2025-12-03 15:49:01,712 - worker.extractor - INFO - Extracting ARS/USDT/BUY
2025-12-03 15:49:01,729 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:01,737 - worker.extractor - INFO - Extracting ARS/USDT/SELL
2025-12-03 15:49:01,759 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:01,775 - worker.extractor - INFO - Extracting ARS/BTC/BUY
2025-12-03 15:49:01,799 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:01,801 - worker.extractor - INFO - Extracting ARS/BTC/SELL
2025-12-03 15:49:01,821 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:01,841 - worker.extractor - INFO - Extracting ARS/ETH/BUY
2025-12-03 15:49:01,857 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:01,869 - worker.extractor - INFO - Extracting ARS/ETH/SELL
2025-12-03 15:49:01,885 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:02,049 - worker.extractor - INFO - Extracting ARS/BNB/BUY
2025-12-03 15:49:02,316 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:02,317 - worker.extractor - INFO - Extracting ARS/BNB/SELL
2025-12-03 15:49:02,722 - worker.extractor - INFO - Extracting COP/USDT/BUY
2025-12-03 15:49:02,745 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:02,947 - worker.extractor - INFO - Extracting COP/USDT/SELL
2025-12-03 15:49:02,949 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:03,158 - worker.extractor - INFO - Extracting COP/BTC/BUY
2025-12-03 15:49:03,339 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:03,521 - worker.extractor - INFO - Extracting COP/BTC/SELL
2025-12-03 15:49:03,656 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:03,902 - worker.extractor - INFO - Extracting COP/ETH/BUY
2025-12-03 15:49:03,952 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:03,952 - worker.extractor - INFO - Extracting COP/ETH/SELL
2025-12-03 15:49:04,153 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:04,160 - worker.extractor - INFO - Extracting VES/USDT/BUY
2025-12-03 15:49:04,418 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:04,418 - worker.extractor - INFO - Extracting VES/USDT/SELL
2025-12-03 15:49:04,732 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:04,751 - worker.extractor - INFO - Extracting VES/BTC/BUY
2025-12-03 15:49:04,956 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:05,177 - worker.extractor - INFO - Extracting VES/BTC/SELL
2025-12-03 15:49:05,315 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:05,315 - worker.extractor - INFO - Extracting USD/USDT/BUY
2025-12-03 15:49:05,322 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:05,318 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:05,507 - worker.extractor - INFO - Extracting USD/USDT/SELL
2025-12-03 15:49:05,913 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:10,201 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:10,201 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:10,261 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:10,329 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:10,517 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:10,579 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:10,733 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:10,859 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:10,986 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:11,232 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:11,451 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:11,605 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:11,745 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:11,807 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:11,835 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:12,035 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:12,161 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:12,294 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:12,500 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:12,533 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:12,704 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:12,850 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:13,003 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:13,107 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:13,182 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:13,186 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:13,216 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:49:13,530 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:13,537 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:49:13,656 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:13,699 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:13,741 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:13,836 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:13,850 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:49:13,851 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:13,898 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:49:13,985 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:14,002 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:14,015 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:14,037 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:49:14,131 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:14,146 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:14,260 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:14,265 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:14,303 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:14,378 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:14,379 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:14,436 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:14,436 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:14,449 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:49:14,522 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:49:14,588 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:14,612 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:14,614 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:49:14,683 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:14,691 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:14,740 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:14,754 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:14,769 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:14,835 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:14,927 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:14,937 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:14,940 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:14,940 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:14,940 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:14,970 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:15,213 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:15,342 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:15,462 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:15,515 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:15,564 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:15,605 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:49:15,631 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:49:15,691 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:15,696 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:15,974 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:16,170 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:16,487 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:16,771 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:17,082 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:17,371 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:17,648 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:17,972 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:18,246 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:18,573 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:18,868 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:19,174 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:19,444 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:19,774 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:20,062 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:20,374 - worker.rate_limiter - WARNING - Rate limiter active: 10 waits, 51 total requests
2025-12-03 15:49:20,375 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:20,679 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:20,974 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:21,245 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:21,575 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:21,844 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:22,176 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:22,776 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:22,911 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:23,056 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:23,376 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:23,702 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:23,977 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:24,259 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:24,577 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:24,866 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:24,868 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BTC/BUY
2025-12-03 15:49:24,869 - worker.extractor - INFO - Extracted 25 offers for ARS/BTC/BUY
2025-12-03 15:49:24,871 - worker.extractor - INFO - Extracting USD/BTC/BUY
2025-12-03 15:49:25,178 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:25,455 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:25,780 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:26,058 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:26,380 - worker.rate_limiter - WARNING - Rate limiter active: 20 waits, 61 total requests
2025-12-03 15:49:26,381 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:26,652 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:26,981 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:27,260 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:27,582 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:27,843 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:28,182 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:28,447 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:28,448 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/ETH/SELL
2025-12-03 15:49:28,449 - worker.extractor - INFO - Extracted 25 offers for ARS/ETH/SELL
2025-12-03 15:49:28,449 - worker.extractor - INFO - Extracting USD/BTC/SELL
2025-12-03 15:49:28,783 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:29,045 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:29,383 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:29,739 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:29,984 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:30,283 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:30,588 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:30,869 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:30,870 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/ETH/BUY
2025-12-03 15:49:30,871 - worker.extractor - INFO - Extracted 22 offers for ARS/ETH/BUY
2025-12-03 15:49:30,871 - worker.extractor - INFO - Extracting USD/ETH/BUY
2025-12-03 15:49:31,188 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:31,467 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:31,789 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:32,390 - worker.rate_limiter - WARNING - Rate limiter active: 30 waits, 71 total requests
2025-12-03 15:49:32,391 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:32,408 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:32,991 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:33,143 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:33,146 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/USDT/SELL
2025-12-03 15:49:33,147 - worker.extractor - INFO - Extracted 26 offers for ARS/USDT/SELL
2025-12-03 15:49:33,148 - worker.extractor - INFO - Extracting USD/ETH/SELL
2025-12-03 15:49:33,340 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:33,592 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:33,972 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:34,193 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:34,456 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:34,458 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/USDT/BUY
2025-12-03 15:49:34,459 - worker.extractor - INFO - Extracted 26 offers for ARS/USDT/BUY
2025-12-03 15:49:34,460 - worker.extractor - INFO - Extracting USD/BNB/BUY
2025-12-03 15:49:34,793 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:35,060 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:35,062 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BTC/SELL
2025-12-03 15:49:35,062 - worker.extractor - INFO - Extracted 26 offers for ARS/BTC/SELL
2025-12-03 15:49:35,063 - worker.extractor - INFO - Extracting USD/BNB/SELL
2025-12-03 15:49:35,394 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:35,684 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:35,994 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:36,316 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:36,317 - worker.extractor - INFO - No offers found for COP/ETH/BUY
2025-12-03 15:49:36,317 - worker.extractor - INFO - Extracted 14 offers for COP/ETH/BUY
2025-12-03 15:49:36,317 - worker.extractor - INFO - Extracting USD/USDC/BUY
2025-12-03 15:49:36,595 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:37,139 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:37,196 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:37,479 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:37,797 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:38,074 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:38,397 - worker.rate_limiter - WARNING - Rate limiter active: 40 waits, 81 total requests
2025-12-03 15:49:38,397 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:38,677 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:38,997 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:39,272 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:39,598 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:39,863 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:39,865 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BNB/SELL
2025-12-03 15:49:39,866 - worker.extractor - INFO - Extracted 25 offers for ARS/BNB/SELL
2025-12-03 15:49:39,867 - worker.extractor - INFO - Extracting USD/USDC/SELL
2025-12-03 15:49:40,198 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:40,511 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:40,799 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:41,077 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:41,402 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:41,676 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:41,677 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BNB/BUY
2025-12-03 15:49:41,677 - worker.extractor - INFO - Extracted 21 offers for ARS/BNB/BUY
2025-12-03 15:49:42,002 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:42,265 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:42,602 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:42,895 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:43,203 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:43,481 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:43,482 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/BTC/SELL
2025-12-03 15:49:43,482 - worker.extractor - INFO - Extracted 26 offers for COP/BTC/SELL
2025-12-03 15:49:43,803 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:44,118 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:44,404 - worker.rate_limiter - WARNING - Rate limiter active: 50 waits, 91 total requests
2025-12-03 15:49:44,404 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:44,678 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:45,004 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:45,605 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:45,700 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:45,885 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:45,888 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/USDT/BUY
2025-12-03 15:49:45,889 - worker.extractor - INFO - Extracted 26 offers for COP/USDT/BUY
2025-12-03 15:49:46,205 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:46,477 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:46,806 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:47,066 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:47,406 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:47,678 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:48,006 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:48,285 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:48,606 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:48,886 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:49,207 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:49,477 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:49,478 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/BTC/BUY
2025-12-03 15:49:49,478 - worker.extractor - INFO - Extracted 25 offers for VES/BTC/BUY
2025-12-03 15:49:49,808 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:50,075 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:50,076 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/BTC/BUY
2025-12-03 15:49:50,076 - worker.extractor - INFO - Extracted 25 offers for COP/BTC/BUY
2025-12-03 15:49:50,409 - worker.rate_limiter - WARNING - Rate limiter active: 60 waits, 101 total requests
2025-12-03 15:49:50,409 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:50,771 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:50,777 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/ETH/SELL
2025-12-03 15:49:50,778 - worker.extractor - INFO - Extracted 25 offers for COP/ETH/SELL
2025-12-03 15:49:51,009 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:51,282 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:51,283 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/USDT/SELL
2025-12-03 15:49:51,283 - worker.extractor - INFO - Extracted 26 offers for COP/USDT/SELL
2025-12-03 15:49:51,609 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:51,885 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:52,210 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:52,517 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:52,810 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:53,084 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:53,085 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/USDT/SELL
2025-12-03 15:49:53,086 - worker.extractor - INFO - Extracted 26 offers for VES/USDT/SELL
2025-12-03 15:49:53,411 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:53,679 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:53,680 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/USDT/BUY
2025-12-03 15:49:53,680 - worker.extractor - INFO - Extracted 26 offers for VES/USDT/BUY
2025-12-03 15:49:54,011 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:54,374 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:54,611 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:54,910 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:54,911 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/BTC/SELL
2025-12-03 15:49:54,911 - worker.extractor - INFO - Extracted 25 offers for VES/BTC/SELL
2025-12-03 15:49:55,212 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:55,501 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:55,812 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:56,168 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:56,169 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDT/BUY
2025-12-03 15:49:56,170 - worker.extractor - INFO - Extracted 26 offers for USD/USDT/BUY
2025-12-03 15:49:56,419 - worker.rate_limiter - WARNING - Rate limiter active: 70 waits, 111 total requests
2025-12-03 15:49:56,422 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:56,740 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:57,019 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:57,290 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:57,626 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:57,915 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:57,919 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDT/SELL
2025-12-03 15:49:57,921 - worker.extractor - INFO - Extracted 26 offers for USD/USDT/SELL
2025-12-03 15:49:58,227 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:58,501 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:58,836 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:59,137 - worker.extractor - INFO - Response status: 200
2025-12-03 15:49:59,437 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:49:59,725 - worker.extractor - INFO - Response status: 200
2025-12-03 15:50:00,106 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:50:00,521 - worker.extractor - INFO - Response status: 200
2025-12-03 15:50:00,713 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:50:01,000 - worker.extractor - INFO - Response status: 200
2025-12-03 15:50:01,314 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:50:01,654 - worker.extractor - INFO - Response status: 200
2025-12-03 15:50:01,914 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:50:02,515 - worker.rate_limiter - WARNING - Rate limiter active: 80 waits, 121 total requests
2025-12-03 15:50:02,516 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:50:02,612 - worker.extractor - INFO - Response status: 200
2025-12-03 15:50:02,870 - worker.extractor - INFO - Response status: 200
2025-12-03 15:50:03,117 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:50:03,400 - worker.extractor - INFO - Response status: 200
2025-12-03 15:50:03,718 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:50:04,008 - worker.extractor - INFO - Response status: 200
2025-12-03 15:50:04,318 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:50:04,582 - worker.extractor - INFO - Response status: 200
2025-12-03 15:50:04,919 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:50:05,271 - worker.extractor - INFO - Response status: 200
2025-12-03 15:50:05,518 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:50:05,798 - worker.extractor - INFO - Response status: 200
2025-12-03 15:50:06,119 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:50:06,385 - worker.extractor - INFO - Response status: 200
2025-12-03 15:50:06,719 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:50:06,987 - worker.extractor - INFO - Response status: 200
2025-12-03 15:50:07,320 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:50:07,602 - worker.extractor - INFO - Response status: 200
2025-12-03 15:50:07,923 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:50:08,220 - worker.extractor - INFO - Response status: 200
2025-12-03 15:50:08,524 - worker.rate_limiter - WARNING - Rate limiter active: 90 waits, 131 total requests
2025-12-03 15:50:08,525 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:50:08,828 - worker.extractor - INFO - Response status: 200
2025-12-03 15:50:08,828 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BTC/BUY
2025-12-03 15:50:08,829 - worker.extractor - INFO - Extracted 25 offers for USD/BTC/BUY
2025-12-03 15:50:09,124 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:50:09,399 - worker.extractor - INFO - Response status: 200
2025-12-03 15:50:09,725 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:50:10,004 - worker.extractor - INFO - Response status: 200
2025-12-03 15:50:10,005 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BTC/SELL
2025-12-03 15:50:10,006 - worker.extractor - INFO - Extracted 25 offers for USD/BTC/SELL
2025-12-03 15:50:10,329 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:50:10,625 - worker.extractor - INFO - Response status: 200
2025-12-03 15:50:10,627 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/ETH/BUY
2025-12-03 15:50:10,627 - worker.extractor - INFO - Extracted 25 offers for USD/ETH/BUY
2025-12-03 15:50:10,930 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:50:11,203 - worker.extractor - INFO - Response status: 200
2025-12-03 15:50:11,206 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/ETH/SELL
2025-12-03 15:50:11,206 - worker.extractor - INFO - Extracted 25 offers for USD/ETH/SELL
2025-12-03 15:50:11,530 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:50:11,822 - worker.extractor - INFO - Response status: 200
2025-12-03 15:50:11,822 - worker.extractor - INFO - No offers found for USD/BNB/BUY
2025-12-03 15:50:11,823 - worker.extractor - INFO - Extracted 20 offers for USD/BNB/BUY
2025-12-03 15:50:12,131 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:50:12,416 - worker.extractor - INFO - Response status: 200
2025-12-03 15:50:12,418 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BNB/SELL
2025-12-03 15:50:12,418 - worker.extractor - INFO - Extracted 25 offers for USD/BNB/SELL
2025-12-03 15:50:12,743 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:50:13,030 - worker.extractor - INFO - Response status: 200
2025-12-03 15:50:13,034 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDC/BUY
2025-12-03 15:50:13,038 - worker.extractor - INFO - Extracted 25 offers for USD/USDC/BUY
2025-12-03 15:50:13,352 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:50:13,681 - worker.extractor - INFO - Response status: 200
2025-12-03 15:50:13,683 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDC/SELL
2025-12-03 15:50:13,684 - worker.extractor - INFO - Extracted 25 offers for USD/USDC/SELL
2025-12-03 15:50:13,687 - worker.extractor - INFO - Total offers extracted: 687
2025-12-03 15:50:13,688 - worker.loader - INFO - Starting to load 687 offers for batch 0105a0a3-623d-4947-bf19-06aab03ed44e...
2025-12-03 15:50:14,778 - worker.loader - ERROR - Error loading offers for batch 0105a0a3-623d-4947-bf19-06aab03ed44e: 
'advertiser'
Traceback (most recent call last):
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 50, in load_offers
    self._load_dimensions(session, offers)
    ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 156, in _load_dimensions
    self._get_or_create_advertiser(session, offer['advertiser']['id'], offer['advertiser']['nickname'])
                                            ~~~~~^^^^^^^^^^^^^^
KeyError: 'advertiser'
2025-12-03 15:50:14,954 - worker.db - ERROR - Database session error: 'advertiser'
2025-12-03 15:50:14,955 - __main__ - ERROR - An error occurred during the job: 'advertiser'
Traceback (most recent call last):
  File "C:\Users\DELL\Desktop\dashboards\worker\main.py", line 31, in job
    loader.load_offers(offers, batch_id)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 50, in load_offers
    self._load_dimensions(session, offers)
    ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 156, in _load_dimensions
    self._get_or_create_advertiser(session, offer['advertiser']['id'], offer['advertiser']['nickname'])
                                            ~~~~~^^^^^^^^^^^^^^
KeyError: 'advertiser'

# Nineth Run

(.venv) PS C:\Users\DELL\Desktop\dashboards> python -m worker.main 
2025-12-03 15:56:26,776 - __main__ - INFO - Worker starting. Job will run every 10 minutes.
2025-12-03 15:56:26,778 - __main__ - INFO - Starting P2P data extraction job...
2025-12-03 15:56:26,778 - worker.extractor - INFO - Fetching all trading pairs...
2025-12-03 15:56:26,779 - worker.extractor - INFO - Generating trading pairs from p2p_config.json...
2025-12-03 15:56:26,781 - worker.extractor - INFO - Generated 28 trading pairs from configuration.
2025-12-03 15:56:26,782 - worker.extractor - INFO - Starting parallel extraction for 28 pairs...
2025-12-03 15:56:26,786 - worker.extractor - INFO - Extracting ARS/USDT/BUY
2025-12-03 15:56:26,787 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:26,789 - worker.extractor - INFO - Extracting ARS/USDT/SELL
2025-12-03 15:56:26,790 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:26,805 - worker.extractor - INFO - Extracting ARS/BTC/BUY
2025-12-03 15:56:26,816 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:26,820 - worker.extractor - INFO - Extracting ARS/BTC/SELL
2025-12-03 15:56:26,822 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:26,826 - worker.extractor - INFO - Extracting ARS/ETH/BUY
2025-12-03 15:56:26,833 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:26,836 - worker.extractor - INFO - Extracting ARS/ETH/SELL
2025-12-03 15:56:26,848 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:26,851 - worker.extractor - INFO - Extracting ARS/BNB/BUY
2025-12-03 15:56:26,856 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:26,858 - worker.extractor - INFO - Extracting ARS/BNB/SELL
2025-12-03 15:56:26,859 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:26,869 - worker.extractor - INFO - Extracting COP/USDT/BUY
2025-12-03 15:56:26,872 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:26,875 - worker.extractor - INFO - Extracting COP/USDT/SELL
2025-12-03 15:56:26,878 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:26,883 - worker.extractor - INFO - Extracting COP/BTC/BUY
2025-12-03 15:56:26,884 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:26,891 - worker.extractor - INFO - Extracting COP/BTC/SELL
2025-12-03 15:56:26,892 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:26,907 - worker.extractor - INFO - Extracting COP/ETH/BUY
2025-12-03 15:56:26,913 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:26,918 - worker.extractor - INFO - Extracting COP/ETH/SELL
2025-12-03 15:56:26,920 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:26,923 - worker.extractor - INFO - Extracting VES/USDT/BUY
2025-12-03 15:56:26,926 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:26,936 - worker.extractor - INFO - Extracting VES/USDT/SELL
2025-12-03 15:56:26,942 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:26,948 - worker.extractor - INFO - Extracting VES/BTC/BUY
2025-12-03 15:56:26,950 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:26,953 - worker.extractor - INFO - Extracting VES/BTC/SELL
2025-12-03 15:56:26,954 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:26,968 - worker.extractor - INFO - Extracting USD/USDT/BUY
2025-12-03 15:56:26,969 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:26,972 - worker.extractor - INFO - Extracting USD/USDT/SELL
2025-12-03 15:56:26,973 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:35,770 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:35,783 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:35,796 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:35,798 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:35,825 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:35,839 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:35,839 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:35,839 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:35,851 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:35,851 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:35,853 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:35,869 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:35,885 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:35,922 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:35,949 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:35,949 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:35,980 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:36,012 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:36,027 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:36,038 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:56:36,038 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:56:36,049 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:36,130 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:36,130 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:36,130 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:36,133 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:56:36,133 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:56:36,157 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:56:36,169 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:56:36,192 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:36,215 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:36,259 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:36,278 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:36,299 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:36,346 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:36,441 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:36,456 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:36,481 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:36,539 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:36,558 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:36,571 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:36,634 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:36,784 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:36,798 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:36,850 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:36,851 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:36,870 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:36,955 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:36,962 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:36,963 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:36,963 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:36,964 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:36,976 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:56:36,976 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:56:36,978 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:36,979 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:36,988 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:36,989 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:56:36,992 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:37,044 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:37,277 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:56:37,284 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:37,589 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:38,190 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:38,367 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:38,756 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:38,790 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:38,867 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:38,964 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:39,119 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 15:56:39,122 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:39,391 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:39,796 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:39,992 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:40,325 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:40,592 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:40,897 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:41,192 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:41,517 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:41,793 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:42,148 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:42,393 - worker.rate_limiter - WARNING - Rate limiter active: 10 waits, 46 total requests
2025-12-03 15:56:42,393 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:42,670 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:42,993 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:43,289 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:43,594 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:43,873 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:44,195 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:44,504 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:44,797 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:45,131 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:45,397 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:45,736 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:45,997 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:46,310 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:46,598 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:46,903 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:47,202 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:47,522 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:47,802 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:48,095 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:48,402 - worker.rate_limiter - WARNING - Rate limiter active: 20 waits, 56 total requests
2025-12-03 15:56:48,403 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:48,695 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:49,003 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:49,294 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:49,604 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:49,987 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:50,205 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:50,568 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:50,805 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:51,095 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:51,405 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:51,701 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:52,006 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:52,318 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:52,607 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:52,914 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:53,208 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:53,808 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:53,933 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:54,109 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:54,409 - worker.rate_limiter - WARNING - Rate limiter active: 30 waits, 66 total requests
2025-12-03 15:56:54,410 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:54,728 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:55,010 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:55,459 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:55,611 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:55,921 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:56,212 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:56,509 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:56,812 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:57,148 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:57,412 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:57,712 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:58,013 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:58,407 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:58,408 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BNB/SELL
2025-12-03 15:56:58,409 - worker.extractor - INFO - Extracted 25 offers for ARS/BNB/SELL
2025-12-03 15:56:58,409 - worker.extractor - INFO - Extracting USD/BTC/BUY
2025-12-03 15:56:58,623 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:58,942 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:59,268 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:56:59,751 - worker.extractor - INFO - Response status: 200
2025-12-03 15:56:59,868 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:00,187 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:00,468 - worker.rate_limiter - WARNING - Rate limiter active: 40 waits, 76 total requests
2025-12-03 15:57:00,470 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:00,832 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:01,069 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:01,510 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:01,670 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:02,201 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:02,270 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:02,679 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:02,871 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:03,336 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:03,339 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/USDT/SELL
2025-12-03 15:57:03,340 - worker.extractor - INFO - Extracted 26 offers for COP/USDT/SELL
2025-12-03 15:57:03,341 - worker.extractor - INFO - Extracting USD/BTC/SELL
2025-12-03 15:57:03,471 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:03,851 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:03,851 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/ETH/BUY
2025-12-03 15:57:03,852 - worker.extractor - INFO - Extracted 22 offers for ARS/ETH/BUY
2025-12-03 15:57:03,852 - worker.extractor - INFO - Extracting USD/ETH/BUY
2025-12-03 15:57:04,072 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:04,391 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:04,392 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BNB/BUY
2025-12-03 15:57:04,394 - worker.extractor - INFO - Extracted 21 offers for ARS/BNB/BUY
2025-12-03 15:57:04,395 - worker.extractor - INFO - Extracting USD/ETH/SELL
2025-12-03 15:57:04,672 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:05,018 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:05,019 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/BTC/SELL
2025-12-03 15:57:05,021 - worker.extractor - INFO - Extracted 25 offers for VES/BTC/SELL
2025-12-03 15:57:05,021 - worker.extractor - INFO - Extracting USD/BNB/BUY
2025-12-03 15:57:05,273 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:05,719 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:05,720 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/USDT/BUY
2025-12-03 15:57:05,721 - worker.extractor - INFO - Extracted 26 offers for ARS/USDT/BUY
2025-12-03 15:57:05,721 - worker.extractor - INFO - Extracting USD/BNB/SELL
2025-12-03 15:57:05,874 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:06,211 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:06,211 - worker.extractor - INFO - No offers found for COP/ETH/BUY
2025-12-03 15:57:06,212 - worker.extractor - INFO - Extracted 14 offers for COP/ETH/BUY
2025-12-03 15:57:06,212 - worker.extractor - INFO - Extracting USD/USDC/BUY
2025-12-03 15:57:06,475 - worker.rate_limiter - WARNING - Rate limiter active: 50 waits, 86 total requests
2025-12-03 15:57:06,476 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:06,784 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:06,786 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/BTC/SELL
2025-12-03 15:57:06,787 - worker.extractor - INFO - Extracted 26 offers for COP/BTC/SELL
2025-12-03 15:57:06,788 - worker.extractor - INFO - Extracting USD/USDC/SELL
2025-12-03 15:57:07,075 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:07,352 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:07,353 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDT/SELL
2025-12-03 15:57:07,354 - worker.extractor - INFO - Extracted 26 offers for USD/USDT/SELL
2025-12-03 15:57:07,675 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:07,991 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:07,992 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/BTC/BUY
2025-12-03 15:57:07,993 - worker.extractor - INFO - Extracted 25 offers for VES/BTC/BUY
2025-12-03 15:57:08,276 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:08,559 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:08,561 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/USDT/BUY
2025-12-03 15:57:08,561 - worker.extractor - INFO - Extracted 26 offers for COP/USDT/BUY
2025-12-03 15:57:08,877 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:09,192 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:09,194 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/USDT/SELL
2025-12-03 15:57:09,195 - worker.extractor - INFO - Extracted 26 offers for VES/USDT/SELL
2025-12-03 15:57:09,477 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:09,958 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:09,959 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/ETH/SELL
2025-12-03 15:57:09,959 - worker.extractor - INFO - Extracted 25 offers for COP/ETH/SELL
2025-12-03 15:57:10,077 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:10,412 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:10,678 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:10,986 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:10,987 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BTC/SELL
2025-12-03 15:57:10,988 - worker.extractor - INFO - Extracted 26 offers for ARS/BTC/SELL
2025-12-03 15:57:11,278 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:11,648 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:11,878 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:12,301 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:12,302 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/ETH/SELL
2025-12-03 15:57:12,303 - worker.extractor - INFO - Extracted 25 offers for ARS/ETH/SELL
2025-12-03 15:57:12,479 - worker.rate_limiter - WARNING - Rate limiter active: 60 waits, 96 total requests
2025-12-03 15:57:12,480 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:12,778 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:12,779 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/USDT/BUY
2025-12-03 15:57:12,780 - worker.extractor - INFO - Extracted 26 offers for VES/USDT/BUY
2025-12-03 15:57:13,080 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:13,396 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:13,397 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/USDT/SELL
2025-12-03 15:57:13,397 - worker.extractor - INFO - Extracted 26 offers for ARS/USDT/SELL
2025-12-03 15:57:13,681 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:14,281 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:14,454 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:14,455 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BTC/BUY
2025-12-03 15:57:14,455 - worker.extractor - INFO - Extracted 25 offers for ARS/BTC/BUY
2025-12-03 15:57:14,634 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:14,636 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDT/BUY
2025-12-03 15:57:14,636 - worker.extractor - INFO - Extracted 26 offers for USD/USDT/BUY
2025-12-03 15:57:14,882 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:15,272 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:15,482 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:15,809 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:16,086 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:16,686 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:16,838 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:16,992 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:17,287 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:17,587 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:17,887 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:18,239 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:18,488 - worker.rate_limiter - WARNING - Rate limiter active: 70 waits, 106 total requests
2025-12-03 15:57:18,490 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:18,848 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:19,090 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:19,637 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:19,691 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:20,292 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:20,587 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:20,588 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/BTC/BUY
2025-12-03 15:57:20,589 - worker.extractor - INFO - Extracted 25 offers for COP/BTC/BUY
2025-12-03 15:57:20,898 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:21,228 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:21,499 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:21,519 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:22,100 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:22,254 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:22,418 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:22,701 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:22,977 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:23,301 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:23,627 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:23,902 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:24,503 - worker.rate_limiter - WARNING - Rate limiter active: 80 waits, 116 total requests
2025-12-03 15:57:24,504 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:24,684 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:24,846 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:25,104 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:25,705 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:25,831 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:26,020 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:26,305 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:26,634 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:26,906 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:27,354 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:27,507 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:27,813 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:28,107 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:28,493 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:28,707 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:29,074 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:29,307 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:29,593 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:29,908 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:30,227 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:30,538 - worker.rate_limiter - WARNING - Rate limiter active: 90 waits, 126 total requests
2025-12-03 15:57:30,569 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:30,954 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:31,138 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:31,506 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:31,739 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:32,174 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:32,339 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:32,627 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:32,940 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:33,422 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:33,541 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:33,901 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:34,143 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:34,445 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:34,446 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BTC/BUY
2025-12-03 15:57:34,446 - worker.extractor - INFO - Extracted 25 offers for USD/BTC/BUY
2025-12-03 15:57:34,743 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:35,068 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:35,069 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BTC/SELL
2025-12-03 15:57:35,070 - worker.extractor - INFO - Extracted 25 offers for USD/BTC/SELL
2025-12-03 15:57:35,345 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:35,641 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:35,643 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/ETH/BUY
2025-12-03 15:57:35,644 - worker.extractor - INFO - Extracted 25 offers for USD/ETH/BUY
2025-12-03 15:57:35,945 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:36,257 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:36,259 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/ETH/SELL
2025-12-03 15:57:36,259 - worker.extractor - INFO - Extracted 25 offers for USD/ETH/SELL
2025-12-03 15:57:36,545 - worker.rate_limiter - WARNING - Rate limiter active: 100 waits, 136 total requests
2025-12-03 15:57:36,546 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:36,851 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:36,851 - worker.extractor - INFO - No offers found for USD/BNB/BUY
2025-12-03 15:57:36,852 - worker.extractor - INFO - Extracted 20 offers for USD/BNB/BUY
2025-12-03 15:57:37,147 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:37,747 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:37,871 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:37,872 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BNB/SELL
2025-12-03 15:57:37,872 - worker.extractor - INFO - Extracted 25 offers for USD/BNB/SELL
2025-12-03 15:57:38,148 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:38,149 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDC/BUY
2025-12-03 15:57:38,152 - worker.extractor - INFO - Extracted 25 offers for USD/USDC/BUY
2025-12-03 15:57:38,348 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 15:57:38,745 - worker.extractor - INFO - Response status: 200
2025-12-03 15:57:38,747 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDC/SELL
2025-12-03 15:57:38,747 - worker.extractor - INFO - Extracted 25 offers for USD/USDC/SELL
2025-12-03 15:57:38,757 - worker.extractor - INFO - Total offers extracted: 687
2025-12-03 15:57:38,758 - worker.loader - INFO - Starting to load 687 offers for batch 7492da06-0d75-4812-bf7f-04df64cf8a26...
2025-12-03 15:57:40,819 - worker.loader - ERROR - Error loading offers for batch 7492da06-0d75-4812-bf7f-04df64cf8a26: 
(psycopg2.errors.NotNullViolation) null value in column "advertiser_id" of relation "dim_advertisers" violates not-null constraint
DETAIL:  Failing row contains (1, null, Dagger1982, f, 0, 2025-12-03 20:57:40.250881, null, t, 2025-12-03 20:57:40.641387).

[SQL: INSERT INTO dim_advertisers (advertiser_id, nickname, is_merchant, registration_days, effective_date, expiration_date, is_current, created_at) VALUES (%(advertiser_id)s, %(nickname)s, %(is_merchant)s, %(registration_days)s, %(effective_date)s, %(expiration_date)s, %(is_current)s, now()) RETURNING dim_advertisers.advertiser_sk, dim_advertisers.created_at]
[parameters: {'advertiser_id': None, 'nickname': 'Dagger1982', 'is_merchant': False, 'registration_days': 0, 'effective_date': datetime.datetime(2025, 12, 3, 20, 57, 40, 250881), 'expiration_date': None, 'is_current': True}]
(Background on this error at: https://sqlalche.me/e/20/gkpj)
Traceback (most recent call last):
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1963, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\default.py", line 943, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
psycopg2.errors.NotNullViolation: null value in column "advertiser_id" of relation "dim_advertisers" violates not-null 
constraint
DETAIL:  Failing row contains (1, null, Dagger1982, f, 0, 2025-12-03 20:57:40.250881, null, t, 2025-12-03 20:57:40.641387).


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 50, in load_offers
    self._load_dimensions(session, offers)
    ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 156, in _load_dimensions
    self._get_or_create_advertiser(session, offer['advertiser']['id'], offer['advertiser']['nickname'])
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 147, in _get_or_create_advertiser
    session.flush()
    ~~~~~~~~~~~~~^^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\session.py", line 4345, in flush   
    self._flush(objects)
    ~~~~~~~~~~~^^^^^^^^^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\session.py", line 4480, in _flush  
    with util.safe_reraise():
         ~~~~~~~~~~~~~~~~~^^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\util\langhelpers.py", line 224, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\session.py", line 4441, in _flush  
    flush_context.execute()
    ~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\unitofwork.py", line 466, in execute
    rec.execute(self)
    ~~~~~~~~~~~^^^^^^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\unitofwork.py", line 642, in execute
    util.preloaded.orm_persistence.save_obj(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self.mapper,
        ^^^^^^^^^^^^
        uow.states_for_mapper_hierarchy(self.mapper, False, False),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        uow,
        ^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\persistence.py", line 93, in save_obj
    _emit_insert_statements(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        base_mapper,
        ^^^^^^^^^^^^
    ...<3 lines>...
        insert,
        ^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\persistence.py", line 1233, in _emit_insert_statements
    result = connection.execute(
        statement,
        params,
        execution_options=execution_options,
    )
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1415, in execute 
    return meth(
        self,
        distilled_parameters,
        execution_options or NO_OPTIONS,
    )
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\sql\elements.py", line 523, in _execute_on_connection
    return connection._execute_clauseelement(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self, distilled_params, execution_options
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1637, in _execute_clauseelement
    ret = self._execute_context(
        dialect,
    ...<8 lines>...
        cache_hit=cache_hit,
    )
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1842, in _execute_context
    return self._exec_single_context(
           ~~~~~~~~~~~~~~~~~~~~~~~~~^
        dialect, context, statement, parameters
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1982, in _exec_single_context
    self._handle_dbapi_exception(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        e, str_statement, effective_parameters, cursor, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 2351, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1963, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\default.py", line 943, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
sqlalchemy.exc.IntegrityError: (psycopg2.errors.NotNullViolation) null value in column "advertiser_id" of relation "dim_advertisers" violates not-null constraint
DETAIL:  Failing row contains (1, null, Dagger1982, f, 0, 2025-12-03 20:57:40.250881, null, t, 2025-12-03 20:57:40.641387).

[SQL: INSERT INTO dim_advertisers (advertiser_id, nickname, is_merchant, registration_days, effective_date, expiration_date, is_current, created_at) VALUES (%(advertiser_id)s, %(nickname)s, %(is_merchant)s, %(registration_days)s, %(effective_date)s, %(expiration_date)s, %(is_current)s, now()) RETURNING dim_advertisers.advertiser_sk, dim_advertisers.created_at]
[parameters: {'advertiser_id': None, 'nickname': 'Dagger1982', 'is_merchant': False, 'registration_days': 0, 'effective_date': datetime.datetime(2025, 12, 3, 20, 57, 40, 250881), 'expiration_date': None, 'is_current': True}]
(Background on this error at: https://sqlalche.me/e/20/gkpj)
2025-12-03 15:57:40,943 - worker.db - ERROR - Database session error: (psycopg2.errors.NotNullViolation) null value in 
column "advertiser_id" of relation "dim_advertisers" violates not-null constraint
DETAIL:  Failing row contains (1, null, Dagger1982, f, 0, 2025-12-03 20:57:40.250881, null, t, 2025-12-03 20:57:40.641387).

[SQL: INSERT INTO dim_advertisers (advertiser_id, nickname, is_merchant, registration_days, effective_date, expiration_date, is_current, created_at) VALUES (%(advertiser_id)s, %(nickname)s, %(is_merchant)s, %(registration_days)s, %(effective_date)s, %(expiration_date)s, %(is_current)s, now()) RETURNING dim_advertisers.advertiser_sk, dim_advertisers.created_at]
[parameters: {'advertiser_id': None, 'nickname': 'Dagger1982', 'is_merchant': False, 'registration_days': 0, 'effective_date': datetime.datetime(2025, 12, 3, 20, 57, 40, 250881), 'expiration_date': None, 'is_current': True}]
(Background on this error at: https://sqlalche.me/e/20/gkpj)
2025-12-03 15:57:40,945 - __main__ - ERROR - An error occurred during the job: (psycopg2.errors.NotNullViolation) null 
value in column "advertiser_id" of relation "dim_advertisers" violates not-null constraint
DETAIL:  Failing row contains (1, null, Dagger1982, f, 0, 2025-12-03 20:57:40.250881, null, t, 2025-12-03 20:57:40.641387).

[SQL: INSERT INTO dim_advertisers (advertiser_id, nickname, is_merchant, registration_days, effective_date, expiration_date, is_current, created_at) VALUES (%(advertiser_id)s, %(nickname)s, %(is_merchant)s, %(registration_days)s, %(effective_date)s, %(expiration_date)s, %(is_current)s, now()) RETURNING dim_advertisers.advertiser_sk, dim_advertisers.created_at]
[parameters: {'advertiser_id': None, 'nickname': 'Dagger1982', 'is_merchant': False, 'registration_days': 0, 'effective_date': datetime.datetime(2025, 12, 3, 20, 57, 40, 250881), 'expiration_date': None, 'is_current': True}]
(Background on this error at: https://sqlalche.me/e/20/gkpj)
Traceback (most recent call last):
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1963, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\default.py", line 943, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
psycopg2.errors.NotNullViolation: null value in column "advertiser_id" of relation "dim_advertisers" violates not-null 
constraint
DETAIL:  Failing row contains (1, null, Dagger1982, f, 0, 2025-12-03 20:57:40.250881, null, t, 2025-12-03 20:57:40.641387).


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\DELL\Desktop\dashboards\worker\main.py", line 31, in job
    loader.load_offers(offers, batch_id)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 50, in load_offers
    self._load_dimensions(session, offers)
    ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 156, in _load_dimensions
    self._get_or_create_advertiser(session, offer['advertiser']['id'], offer['advertiser']['nickname'])
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 147, in _get_or_create_advertiser
    session.flush()
    ~~~~~~~~~~~~~^^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\session.py", line 4345, in flush   
    self._flush(objects)
    ~~~~~~~~~~~^^^^^^^^^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\session.py", line 4480, in _flush  
    with util.safe_reraise():
         ~~~~~~~~~~~~~~~~~^^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\util\langhelpers.py", line 224, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\session.py", line 4441, in _flush  
    flush_context.execute()
    ~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\unitofwork.py", line 466, in execute
    rec.execute(self)
    ~~~~~~~~~~~^^^^^^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\unitofwork.py", line 642, in execute
    util.preloaded.orm_persistence.save_obj(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self.mapper,
        ^^^^^^^^^^^^
        uow.states_for_mapper_hierarchy(self.mapper, False, False),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        uow,
        ^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\persistence.py", line 93, in save_obj
    _emit_insert_statements(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        base_mapper,
        ^^^^^^^^^^^^
    ...<3 lines>...
        insert,
        ^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\persistence.py", line 1233, in _emit_insert_statements
    result = connection.execute(
        statement,
        params,
        execution_options=execution_options,
    )
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1415, in execute 
    return meth(
        self,
        distilled_parameters,
        execution_options or NO_OPTIONS,
    )
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\sql\elements.py", line 523, in _execute_on_connection
    return connection._execute_clauseelement(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self, distilled_params, execution_options
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1637, in _execute_clauseelement
    ret = self._execute_context(
        dialect,
    ...<8 lines>...
        cache_hit=cache_hit,
    )
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1842, in _execute_context
    return self._exec_single_context(
           ~~~~~~~~~~~~~~~~~~~~~~~~~^
        dialect, context, statement, parameters
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1982, in _exec_single_context
    self._handle_dbapi_exception(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        e, str_statement, effective_parameters, cursor, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 2351, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1963, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\default.py", line 943, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
sqlalchemy.exc.IntegrityError: (psycopg2.errors.NotNullViolation) null value in column "advertiser_id" of relation "dim_advertisers" violates not-null constraint
DETAIL:  Failing row contains (1, null, Dagger1982, f, 0, 2025-12-03 20:57:40.250881, null, t, 2025-12-03 20:57:40.641387).

[SQL: INSERT INTO dim_advertisers (advertiser_id, nickname, is_merchant, registration_days, effective_date, expiration_date, is_current, created_at) VALUES (%(advertiser_id)s, %(nickname)s, %(is_merchant)s, %(registration_days)s, %(effective_date)s, %(expiration_date)s, %(is_current)s, now()) RETURNING dim_advertisers.advertiser_sk, dim_advertisers.created_at]
[parameters: {'advertiser_id': None, 'nickname': 'Dagger1982', 'is_merchant': False, 'registration_days': 0, 'effective_date': datetime.datetime(2025, 12, 3, 20, 57, 40, 250881), 'expiration_date': None, 'is_current': True}]
(Background on this error at: https://sqlalche.me/e/20/gkpj)


# tenth run

(.venv) PS C:\Users\DELL\Desktop\dashboards> python -m worker.main 
2025-12-03 16:05:16,658 - __main__ - INFO - Worker starting. Job will run every 10 m
2025-12-03 16:05:16,658 - __main__ - INFO - Starting P2P data extraction job...
2025-12-03 16:05:16,659 - worker.extractor - INFO - Fetching all trading pairs...
2025-12-03 16:05:16,659 - worker.extractor - INFO - Generating trading pairs from p2
2025-12-03 16:05:16,661 - worker.extractor - INFO - Generated 28 trading pairs from 
2025-12-03 16:05:16,662 - worker.extractor - INFO - Starting parallel extraction for
2025-12-03 16:05:16,664 - worker.extractor - INFO - Extracting ARS/USDT/BUY
2025-12-03 16:05:16,665 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:16,667 - worker.extractor - INFO - Extracting ARS/USDT/SELL
2025-12-03 16:05:16,678 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:16,681 - worker.extractor - INFO - Extracting ARS/BTC/BUY
2025-12-03 16:05:16,701 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:16,701 - worker.extractor - INFO - Extracting ARS/BTC/SELL
2025-12-03 16:05:16,705 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:16,708 - worker.extractor - INFO - Extracting ARS/ETH/BUY
2025-12-03 16:05:16,718 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:16,724 - worker.extractor - INFO - Extracting ARS/ETH/SELL
2025-12-03 16:05:16,740 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:16,770 - worker.extractor - INFO - Extracting ARS/BNB/BUY
2025-12-03 16:05:16,790 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:16,801 - worker.extractor - INFO - Extracting ARS/BNB/SELL
2025-12-03 16:05:16,925 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:16,927 - worker.extractor - INFO - Extracting COP/USDT/BUY
2025-12-03 16:05:17,263 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:17,263 - worker.extractor - INFO - Extracting COP/USDT/SELL
2025-12-03 16:05:17,433 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:17,441 - worker.extractor - INFO - Extracting COP/BTC/BUY
2025-12-03 16:05:17,643 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:17,643 - worker.extractor - INFO - Extracting COP/BTC/SELL
2025-12-03 16:05:17,806 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:17,822 - worker.extractor - INFO - Extracting COP/ETH/BUY
2025-12-03 16:05:18,081 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:18,081 - worker.extractor - INFO - Extracting COP/ETH/SELL
2025-12-03 16:05:18,396 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:18,507 - worker.extractor - INFO - Extracting VES/USDT/BUY
2025-12-03 16:05:18,800 - worker.extractor - INFO - Extracting VES/USDT/SELL
2025-12-03 16:05:18,802 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:19,039 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:19,039 - worker.extractor - INFO - Extracting VES/BTC/BUY
2025-12-03 16:05:19,494 - worker.extractor - INFO - Extracting VES/BTC/SELL
2025-12-03 16:05:19,677 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:19,952 - worker.extractor - INFO - Extracting USD/USDT/BUY
2025-12-03 16:05:19,953 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:20,336 - worker.extractor - INFO - Extracting USD/USDT/SELL
2025-12-03 16:05:20,421 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:20,720 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:24,114 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:24,149 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:24,666 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:24,720 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:24,725 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:24,796 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:24,838 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:24,871 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:25,052 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:25,060 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:25,182 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:25,197 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:25,272 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:25,345 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:25,347 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:25,370 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:25,518 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:25,567 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:25,804 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:25,933 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:25,984 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:26,061 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:26,129 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:26,342 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:26,406 - urllib3.connectionpool - WARNING - Connection pool is fulle.com. Connection pool size: 10
2025-12-03 16:05:26,468 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:26,469 - urllib3.connectionpool - WARNING - Connection pool is fulle.com. Connection pool size: 10
2025-12-03 16:05:26,565 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:26,725 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:26,858 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:26,877 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:26,889 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:26,890 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:26,972 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,191 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,243 - urllib3.connectionpool - WARNING - Connection pool is fulle.com. Connection pool size: 8
2025-12-03 16:05:27,305 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,346 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,375 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,396 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,428 - urllib3.connectionpool - WARNING - Connection pool is fulle.com. Connection pool size: 10
2025-12-03 16:05:27,560 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,570 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:27,625 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:27,645 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,659 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,679 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:27,718 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:27,760 - urllib3.connectionpool - WARNING - Connection pool is fulle.com. Connection pool size: 10
2025-12-03 16:05:27,769 - urllib3.connectionpool - WARNING - Connection pool is fulle.com. Connection pool size: 10
2025-12-03 16:05:27,778 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,849 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,912 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,939 - urllib3.connectionpool - WARNING - Connection pool is fulle.com. Connection pool size: 10
2025-12-03 16:05:27,940 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,957 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,958 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:28,004 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:28,067 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:28,193 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:28,195 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:28,220 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:28,222 - urllib3.connectionpool - WARNING - Connection pool is fulle.com. Connection pool size: 10
2025-12-03 16:05:28,232 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:28,267 - urllib3.connectionpool - WARNING - Connection pool is fulle.com. Connection pool size: 10
2025-12-03 16:05:28,268 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:28,377 - urllib3.connectionpool - WARNING - Connection pool is fulle.com. Connection pool size: 10
2025-12-03 16:05:28,381 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:28,667 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:29,267 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:29,388 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:29,597 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:29,868 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:30,131 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:30,468 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:30,779 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:31,068 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:31,338 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:31,669 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:31,923 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:32,269 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:32,555 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:32,870 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:33,162 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:33,471 - worker.rate_limiter - WARNING - Rate limiter active: 10 wa
2025-12-03 16:05:33,471 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:33,756 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:34,071 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:34,347 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:34,672 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:35,028 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:35,273 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:35,581 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:35,875 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:36,476 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:36,577 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:36,763 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:37,076 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:37,390 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:37,706 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:38,021 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:38,335 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:38,637 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:38,935 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:39,222 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:39,536 - worker.rate_limiter - WARNING - Rate limiter active: 20 wa
2025-12-03 16:05:39,537 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:39,819 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:40,137 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:40,419 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:40,759 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:41,045 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:41,360 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:41,701 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:41,960 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:42,229 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:42,230 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:05:42,231 - worker.extractor - INFO - Extracted 26 offers for ARS/USDT
2025-12-03 16:05:42,231 - worker.extractor - INFO - Extracting USD/BTC/BUY
2025-12-03 16:05:42,561 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:42,842 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:43,161 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:43,524 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:43,762 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:44,031 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:44,362 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:44,732 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:44,962 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:45,243 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:45,563 - worker.rate_limiter - WARNING - Rate limiter active: 30 wa
2025-12-03 16:05:45,563 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:45,836 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:45,841 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:05:45,842 - worker.extractor - INFO - Extracted 26 offers for ARS/BTC/
2025-12-03 16:05:45,843 - worker.extractor - INFO - Extracting USD/BTC/SELL
2025-12-03 16:05:46,164 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:46,436 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:46,764 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:47,097 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:47,365 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:47,718 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:47,966 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:48,243 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:48,245 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:05:48,246 - worker.extractor - INFO - Extracted 26 offers for ARS/USDT
2025-12-03 16:05:48,246 - worker.extractor - INFO - Extracting USD/ETH/BUY
2025-12-03 16:05:48,567 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:48,895 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:49,167 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:49,466 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:49,468 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:05:49,469 - worker.extractor - INFO - Extracted 22 offers for ARS/ETH/
2025-12-03 16:05:49,469 - worker.extractor - INFO - Extracting USD/ETH/SELL
2025-12-03 16:05:49,767 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:50,039 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:50,368 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:50,637 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:50,637 - worker.extractor - INFO - No offers found for COP/ETH/BUY
2025-12-03 16:05:50,637 - worker.extractor - INFO - Extracted 14 offers for COP/ETH/
2025-12-03 16:05:50,638 - worker.extractor - INFO - Extracting USD/BNB/BUY
2025-12-03 16:05:50,968 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:51,255 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:51,569 - worker.rate_limiter - WARNING - Rate limiter active: 40 wa
2025-12-03 16:05:51,572 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:51,907 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:52,170 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:52,443 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:52,449 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:05:52,455 - worker.extractor - INFO - Extracted 21 offers for ARS/BNB/
2025-12-03 16:05:52,457 - worker.extractor - INFO - Extracting USD/BNB/SELL
2025-12-03 16:05:52,771 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:53,050 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:53,051 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:05:53,052 - worker.extractor - INFO - Extracted 26 offers for ARS/BTC/
2025-12-03 16:05:53,052 - worker.extractor - INFO - Extracting USD/USDC/BUY
2025-12-03 16:05:53,371 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:53,658 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:53,659 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:05:53,659 - worker.extractor - INFO - Extracted 26 offers for COP/USDT
2025-12-03 16:05:53,660 - worker.extractor - INFO - Extracting USD/USDC/SELL
2025-12-03 16:05:53,971 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:54,242 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:54,572 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:54,874 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:55,172 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:55,460 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:55,772 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:56,114 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:56,115 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:05:56,116 - worker.extractor - INFO - Extracted 25 offers for ARS/BNB/
2025-12-03 16:05:56,373 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:56,643 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:56,973 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:57,259 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:57,263 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:05:57,264 - worker.extractor - INFO - Extracted 25 offers for ARS/ETH/
2025-12-03 16:05:57,575 - worker.rate_limiter - WARNING - Rate limiter active: 50 wa
2025-12-03 16:05:57,577 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:57,852 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:58,175 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:58,455 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:58,457 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:05:58,457 - worker.extractor - INFO - Extracted 26 offers for COP/BTC/
2025-12-03 16:05:58,775 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:59,059 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:59,376 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:59,661 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:59,662 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:05:59,662 - worker.extractor - INFO - Extracted 26 offers for COP/USDT
2025-12-03 16:05:59,977 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:06:00,292 - worker.extractor - INFO - Response status: 200
2025-12-03 16:06:00,578 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:06:00,857 - worker.extractor - INFO - Response status: 200
2025-12-03 16:06:01,178 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:06:01,464 - worker.extractor - INFO - Response status: 200
2025-12-03 16:06:01,779 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:06:02,134 - worker.extractor - INFO - Response status: 200
2025-12-03 16:06:02,137 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:06:02,137 - worker.extractor - INFO - Extracted 26 offers for VES/USDT
2025-12-03 16:06:02,380 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:06:02,697 - worker.extractor - INFO - Response status: 200
2025-12-03 16:06:02,981 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:06:03,279 - worker.extractor - INFO - Response status: 200
2025-12-03 16:06:03,282 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:06:03,283 - worker.extractor - INFO - Extracted 25 offers for COP/ETH/
2025-12-03 16:06:03,581 - worker.rate_limiter - WARNING - Rate limiter active: 60 wa
2025-12-03 16:06:03,582 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:06:03,844 - worker.extractor - INFO - Response status: 200
2025-12-03 16:06:04,181 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:06:04,469 - worker.extractor - INFO - Response status: 200
2025-12-03 16:06:04,786 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:06:05,053 - worker.extractor - INFO - Response status: 200
2025-12-03 16:06:05,387 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:06:05,669 - worker.extractor - INFO - Response status: 200
2025-12-03 16:06:05,987 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:06:06,281 - worker.extractor - INFO - Response status: 200
2025-12-03 16:06:06,588 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:06:06,860 - worker.extractor - INFO - Response status: 200
2025-12-03 16:06:06,861 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:06:06,861 - worker.extractor - INFO - Extracted 25 offers for COP/BTC/
2025-12-03 16:06:07,189 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:06:07,476 - worker.extractor - INFO - Response status: 200
2025-12-03 16:06:07,494 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:06:07,503 - worker.extractor - INFO - Extracted 25 offers for VES/BTC/
2025-12-03 16:06:07,789 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search

# Eleventh run

(.venv) PS C:\Users\DELL\Desktop\dashboards> python -m worker.main 
2025-12-03 16:05:16,658 - __main__ - INFO - Worker starting. Job will run every 10 m
2025-12-03 16:05:16,658 - __main__ - INFO - Starting P2P data extraction job...
2025-12-03 16:05:16,659 - worker.extractor - INFO - Fetching all trading pairs...
2025-12-03 16:05:16,659 - worker.extractor - INFO - Generating trading pairs from p2
2025-12-03 16:05:16,661 - worker.extractor - INFO - Generated 28 trading pairs from 
2025-12-03 16:05:16,662 - worker.extractor - INFO - Starting parallel extraction for
2025-12-03 16:05:16,664 - worker.extractor - INFO - Extracting ARS/USDT/BUY
2025-12-03 16:05:16,665 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:16,667 - worker.extractor - INFO - Extracting ARS/USDT/SELL
2025-12-03 16:05:16,678 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:16,681 - worker.extractor - INFO - Extracting ARS/BTC/BUY
2025-12-03 16:05:16,701 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:16,701 - worker.extractor - INFO - Extracting ARS/BTC/SELL
2025-12-03 16:05:16,705 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:16,708 - worker.extractor - INFO - Extracting ARS/ETH/BUY
2025-12-03 16:05:16,718 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:16,724 - worker.extractor - INFO - Extracting ARS/ETH/SELL
2025-12-03 16:05:16,740 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:16,770 - worker.extractor - INFO - Extracting ARS/BNB/BUY
2025-12-03 16:05:16,790 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:16,801 - worker.extractor - INFO - Extracting ARS/BNB/SELL
2025-12-03 16:05:16,925 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:16,927 - worker.extractor - INFO - Extracting COP/USDT/BUY
2025-12-03 16:05:17,263 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:17,263 - worker.extractor - INFO - Extracting COP/USDT/SELL
2025-12-03 16:05:17,433 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:17,441 - worker.extractor - INFO - Extracting COP/BTC/BUY
2025-12-03 16:05:17,643 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:17,643 - worker.extractor - INFO - Extracting COP/BTC/SELL
2025-12-03 16:05:17,806 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:17,822 - worker.extractor - INFO - Extracting COP/ETH/BUY
2025-12-03 16:05:18,081 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:18,081 - worker.extractor - INFO - Extracting COP/ETH/SELL
2025-12-03 16:05:18,396 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:18,507 - worker.extractor - INFO - Extracting VES/USDT/BUY
2025-12-03 16:05:18,800 - worker.extractor - INFO - Extracting VES/USDT/SELL
2025-12-03 16:05:18,802 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:19,039 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:19,039 - worker.extractor - INFO - Extracting VES/BTC/BUY
2025-12-03 16:05:19,494 - worker.extractor - INFO - Extracting VES/BTC/SELL
2025-12-03 16:05:19,677 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:19,952 - worker.extractor - INFO - Extracting USD/USDT/BUY
2025-12-03 16:05:19,953 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:20,336 - worker.extractor - INFO - Extracting USD/USDT/SELL
2025-12-03 16:05:20,421 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:20,720 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:24,114 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:24,149 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:24,666 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:24,720 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:24,725 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:24,796 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:24,838 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:24,871 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:25,052 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:25,060 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:25,182 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:25,197 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:25,272 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:25,345 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:25,347 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:25,370 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:25,518 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:25,567 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:25,804 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:25,933 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:25,984 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:26,061 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:26,129 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:26,342 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:26,406 - urllib3.connectionpool - WARNING - Connection pool is fulle.com. Connection pool size: 10
2025-12-03 16:05:26,468 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:26,469 - urllib3.connectionpool - WARNING - Connection pool is fulle.com. Connection pool size: 10
2025-12-03 16:05:26,565 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:26,725 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:26,858 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:26,877 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:26,889 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:26,890 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:26,972 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,191 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,243 - urllib3.connectionpool - WARNING - Connection pool is fulle.com. Connection pool size: 8
2025-12-03 16:05:27,305 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,346 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,375 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,396 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,428 - urllib3.connectionpool - WARNING - Connection pool is fulle.com. Connection pool size: 10
2025-12-03 16:05:27,560 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,570 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:27,625 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:27,645 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,659 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,679 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:27,718 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:27,760 - urllib3.connectionpool - WARNING - Connection pool is fulle.com. Connection pool size: 10
2025-12-03 16:05:27,769 - urllib3.connectionpool - WARNING - Connection pool is fulle.com. Connection pool size: 10
2025-12-03 16:05:27,778 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,849 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,912 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,939 - urllib3.connectionpool - WARNING - Connection pool is fulle.com. Connection pool size: 10
2025-12-03 16:05:27,940 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,957 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:27,958 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:28,004 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:28,067 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:28,193 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:28,195 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:28,220 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:28,222 - urllib3.connectionpool - WARNING - Connection pool is fulle.com. Connection pool size: 10
2025-12-03 16:05:28,232 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:28,267 - urllib3.connectionpool - WARNING - Connection pool is fulle.com. Connection pool size: 10
2025-12-03 16:05:28,268 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:28,377 - urllib3.connectionpool - WARNING - Connection pool is fulle.com. Connection pool size: 10
2025-12-03 16:05:28,381 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:28,667 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:29,267 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:29,388 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:29,597 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:29,868 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:30,131 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:30,468 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:30,779 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:31,068 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:31,338 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:31,669 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:31,923 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:32,269 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:32,555 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:32,870 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:33,162 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:33,471 - worker.rate_limiter - WARNING - Rate limiter active: 10 wa
2025-12-03 16:05:33,471 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:33,756 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:34,071 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:34,347 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:34,672 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:35,028 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:35,273 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:35,581 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:35,875 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:36,476 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:36,577 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:36,763 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:37,076 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:37,390 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:37,706 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:38,021 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:38,335 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:38,637 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:38,935 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:39,222 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:39,536 - worker.rate_limiter - WARNING - Rate limiter active: 20 wa
2025-12-03 16:05:39,537 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:39,819 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:40,137 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:40,419 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:40,759 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:41,045 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:41,360 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:41,701 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:41,960 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:42,229 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:42,230 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:05:42,231 - worker.extractor - INFO - Extracted 26 offers for ARS/USDT
2025-12-03 16:05:42,231 - worker.extractor - INFO - Extracting USD/BTC/BUY
2025-12-03 16:05:42,561 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:42,842 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:43,161 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:43,524 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:43,762 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:44,031 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:44,362 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:44,732 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:44,962 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:45,243 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:45,563 - worker.rate_limiter - WARNING - Rate limiter active: 30 wa
2025-12-03 16:05:45,563 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:45,836 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:45,841 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:05:45,842 - worker.extractor - INFO - Extracted 26 offers for ARS/BTC/
2025-12-03 16:05:45,843 - worker.extractor - INFO - Extracting USD/BTC/SELL
2025-12-03 16:05:46,164 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:46,436 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:46,764 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:47,097 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:47,365 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:47,718 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:47,966 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:48,243 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:48,245 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:05:48,246 - worker.extractor - INFO - Extracted 26 offers for ARS/USDT
2025-12-03 16:05:48,246 - worker.extractor - INFO - Extracting USD/ETH/BUY
2025-12-03 16:05:48,567 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:48,895 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:49,167 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:49,466 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:49,468 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:05:49,469 - worker.extractor - INFO - Extracted 22 offers for ARS/ETH/
2025-12-03 16:05:49,469 - worker.extractor - INFO - Extracting USD/ETH/SELL
2025-12-03 16:05:49,767 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:50,039 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:50,368 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:50,637 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:50,637 - worker.extractor - INFO - No offers found for COP/ETH/BUY
2025-12-03 16:05:50,637 - worker.extractor - INFO - Extracted 14 offers for COP/ETH/
2025-12-03 16:05:50,638 - worker.extractor - INFO - Extracting USD/BNB/BUY
2025-12-03 16:05:50,968 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:51,255 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:51,569 - worker.rate_limiter - WARNING - Rate limiter active: 40 wa
2025-12-03 16:05:51,572 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:51,907 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:52,170 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:52,443 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:52,449 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:05:52,455 - worker.extractor - INFO - Extracted 21 offers for ARS/BNB/
2025-12-03 16:05:52,457 - worker.extractor - INFO - Extracting USD/BNB/SELL
2025-12-03 16:05:52,771 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:53,050 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:53,051 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:05:53,052 - worker.extractor - INFO - Extracted 26 offers for ARS/BTC/
2025-12-03 16:05:53,052 - worker.extractor - INFO - Extracting USD/USDC/BUY
2025-12-03 16:05:53,371 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:53,658 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:53,659 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:05:53,659 - worker.extractor - INFO - Extracted 26 offers for COP/USDT
2025-12-03 16:05:53,660 - worker.extractor - INFO - Extracting USD/USDC/SELL
2025-12-03 16:05:53,971 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:54,242 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:54,572 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:54,874 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:55,172 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:55,460 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:55,772 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:56,114 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:56,115 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:05:56,116 - worker.extractor - INFO - Extracted 25 offers for ARS/BNB/
2025-12-03 16:05:56,373 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:56,643 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:56,973 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:57,259 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:57,263 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:05:57,264 - worker.extractor - INFO - Extracted 25 offers for ARS/ETH/
2025-12-03 16:05:57,575 - worker.rate_limiter - WARNING - Rate limiter active: 50 wa
2025-12-03 16:05:57,577 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:57,852 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:58,175 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:58,455 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:58,457 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:05:58,457 - worker.extractor - INFO - Extracted 26 offers for COP/BTC/
2025-12-03 16:05:58,775 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:59,059 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:59,376 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:05:59,661 - worker.extractor - INFO - Response status: 200
2025-12-03 16:05:59,662 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:05:59,662 - worker.extractor - INFO - Extracted 26 offers for COP/USDT
2025-12-03 16:05:59,977 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:06:00,292 - worker.extractor - INFO - Response status: 200
2025-12-03 16:06:00,578 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:06:00,857 - worker.extractor - INFO - Response status: 200
2025-12-03 16:06:01,178 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:06:01,464 - worker.extractor - INFO - Response status: 200
2025-12-03 16:06:01,779 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:06:02,134 - worker.extractor - INFO - Response status: 200
2025-12-03 16:06:02,137 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:06:02,137 - worker.extractor - INFO - Extracted 26 offers for VES/USDT
2025-12-03 16:06:02,380 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:06:02,697 - worker.extractor - INFO - Response status: 200
2025-12-03 16:06:02,981 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:06:03,279 - worker.extractor - INFO - Response status: 200
2025-12-03 16:06:03,282 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:06:03,283 - worker.extractor - INFO - Extracted 25 offers for COP/ETH/
2025-12-03 16:06:03,581 - worker.rate_limiter - WARNING - Rate limiter active: 60 wa
2025-12-03 16:06:03,582 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:06:03,844 - worker.extractor - INFO - Response status: 200
2025-12-03 16:06:04,181 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:06:04,469 - worker.extractor - INFO - Response status: 200
2025-12-03 16:06:04,786 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:06:05,053 - worker.extractor - INFO - Response status: 200
2025-12-03 16:06:05,387 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:06:05,669 - worker.extractor - INFO - Response status: 200
2025-12-03 16:06:05,987 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:06:06,281 - worker.extractor - INFO - Response status: 200
2025-12-03 16:06:06,588 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:06:06,860 - worker.extractor - INFO - Response status: 200
2025-12-03 16:06:06,861 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:06:06,861 - worker.extractor - INFO - Extracted 25 offers for COP/BTC/
2025-12-03 16:06:07,189 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search
2025-12-03 16:06:07,476 - worker.extractor - INFO - Response status: 200
2025-12-03 16:06:07,494 - worker.extractor - WARNING - Reached max pages per pair (5
2025-12-03 16:06:07,503 - worker.extractor - INFO - Extracted 25 offers for VES/BTC/
2025-12-03 16:06:07,789 - worker.extractor - INFO - Binance API request to https://p/c2c/adv/search


# Twelveth run
(.venv) PS C:\Users\DELL\Desktop\dashboards> python -m worker.main 
2025-12-03 16:17:02,226 - __main__ - INFO - Worker starting. Job will run every 10 minutes.
2025-12-03 16:17:02,227 - __main__ - INFO - Starting P2P data extraction job...
2025-12-03 16:17:02,228 - worker.extractor - INFO - Fetching all trading pairs...
2025-12-03 16:17:02,229 - worker.extractor - INFO - Generating trading pairs from p2p_config.json...
2025-12-03 16:17:02,231 - worker.extractor - INFO - Generated 28 trading pairs from configuration.
2025-12-03 16:17:02,231 - worker.extractor - INFO - Starting parallel extraction for 28 pairs...
2025-12-03 16:17:02,232 - worker.extractor - INFO - Extracting ARS/USDT/BUY
2025-12-03 16:17:02,233 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:02,235 - worker.extractor - INFO - Extracting ARS/USDT/SELL
2025-12-03 16:17:02,239 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:02,244 - worker.extractor - INFO - Extracting ARS/BTC/BUY
2025-12-03 16:17:02,261 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:02,264 - worker.extractor - INFO - Extracting ARS/BTC/SELL
2025-12-03 16:17:02,269 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:02,277 - worker.extractor - INFO - Extracting ARS/ETH/BUY
2025-12-03 16:17:02,282 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:02,297 - worker.extractor - INFO - Extracting ARS/ETH/SELL
2025-12-03 16:17:02,328 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:02,333 - worker.extractor - INFO - Extracting ARS/BNB/BUY
2025-12-03 16:17:02,355 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:02,393 - worker.extractor - INFO - Extracting ARS/BNB/SELL
2025-12-03 16:17:02,446 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:02,463 - worker.extractor - INFO - Extracting COP/USDT/BUY
2025-12-03 16:17:02,513 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:02,527 - worker.extractor - INFO - Extracting COP/USDT/SELL
2025-12-03 16:17:02,842 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:02,842 - worker.extractor - INFO - Extracting COP/BTC/BUY
2025-12-03 16:17:03,153 - worker.extractor - INFO - Extracting COP/BTC/SELL
2025-12-03 16:17:03,157 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:03,179 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:03,217 - worker.extractor - INFO - Extracting COP/ETH/BUY
2025-12-03 16:17:03,542 - worker.extractor - INFO - Extracting COP/ETH/SELL
2025-12-03 16:17:03,772 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:03,773 - worker.extractor - INFO - Extracting VES/USDT/BUY
2025-12-03 16:17:04,006 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:04,131 - worker.extractor - INFO - Extracting VES/USDT/SELL
2025-12-03 16:17:04,248 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:04,459 - worker.extractor - INFO - Extracting VES/BTC/BUY
2025-12-03 16:17:04,464 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:04,471 - worker.extractor - INFO - Extracting VES/BTC/SELL
2025-12-03 16:17:04,744 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:04,746 - worker.extractor - INFO - Extracting USD/USDT/BUY
2025-12-03 16:17:05,027 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:05,046 - worker.extractor - INFO - Extracting USD/USDT/SELL
2025-12-03 16:17:05,358 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:05,731 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:09,961 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:10,117 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:10,118 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:10,242 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:10,274 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:10,274 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:10,288 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:10,411 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:10,495 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:10,585 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:10,585 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:10,646 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:10,810 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:10,881 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:10,960 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:17:10,960 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:17:11,055 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:11,162 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:17:11,175 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:11,332 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:11,534 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:11,611 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:11,730 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:11,952 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:12,228 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:12,235 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:12,298 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:12,327 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:12,398 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:12,493 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:17:12,563 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:12,604 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:12,813 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:12,942 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:17:13,038 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:13,089 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:13,098 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:17:13,149 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:13,230 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:13,261 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:13,308 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:13,357 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:13,377 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:13,382 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:13,398 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:13,414 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:13,433 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:13,447 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:13,450 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:13,452 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:13,452 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:13,529 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:13,546 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:13,629 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:13,647 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:13,782 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:13,782 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:13,799 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:13,799 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:13,854 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:17:13,857 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:17:13,858 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:13,858 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:17:13,861 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:13,865 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:13,883 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:13,966 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:17:13,980 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:14,247 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:14,545 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:14,848 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:15,156 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:15,448 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:15,751 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:16,053 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:16,653 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:16,880 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:16,989 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:17,256 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:17,857 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:17,997 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:18,472 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:18,798 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:18,840 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:19,073 - worker.rate_limiter - WARNING - Rate limiter active: 10 waits, 48 total requests
2025-12-03 16:17:19,077 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:19,674 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:19,835 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:19,956 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:20,275 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:20,557 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:20,878 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:21,170 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:21,478 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:21,803 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:22,078 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:22,679 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:22,838 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:22,991 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:23,297 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:23,653 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:23,898 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:24,306 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:24,498 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:24,818 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:25,099 - worker.rate_limiter - WARNING - Rate limiter active: 20 waits, 58 total requests
2025-12-03 16:17:25,099 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:25,411 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:25,699 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:26,060 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:26,300 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:26,605 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:26,900 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:27,183 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:27,501 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:27,787 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:28,102 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:28,393 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:28,702 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:28,998 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:29,302 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:29,618 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:29,909 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:30,509 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:30,588 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:30,869 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:31,110 - worker.rate_limiter - WARNING - Rate limiter active: 30 waits, 68 total requests
2025-12-03 16:17:31,110 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:31,469 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:31,710 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:31,985 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:32,311 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:32,683 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:32,911 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:33,225 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:33,233 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/ETH/SELL
2025-12-03 16:17:33,235 - worker.extractor - INFO - Extracted 25 offers for ARS/ETH/SELL
2025-12-03 16:17:33,238 - worker.extractor - INFO - Extracting USD/BTC/BUY
2025-12-03 16:17:33,512 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:33,818 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:33,821 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BTC/SELL
2025-12-03 16:17:33,822 - worker.extractor - INFO - Extracted 26 offers for ARS/BTC/SELL
2025-12-03 16:17:33,822 - worker.extractor - INFO - Extracting USD/BTC/SELL
2025-12-03 16:17:34,113 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:34,428 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:34,713 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:35,028 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:35,047 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/USDT/BUY
2025-12-03 16:17:35,052 - worker.extractor - INFO - Extracted 26 offers for COP/USDT/BUY
2025-12-03 16:17:35,053 - worker.extractor - INFO - Extracting USD/ETH/BUY
2025-12-03 16:17:35,314 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:35,610 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:35,914 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:36,262 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:36,514 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:36,885 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:37,115 - worker.rate_limiter - WARNING - Rate limiter active: 40 waits, 78 total requests
2025-12-03 16:17:37,116 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:37,388 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:37,390 - worker.extractor - INFO - No offers found for COP/ETH/BUY
2025-12-03 16:17:37,391 - worker.extractor - INFO - Extracted 14 offers for COP/ETH/BUY
2025-12-03 16:17:37,392 - worker.extractor - INFO - Extracting USD/ETH/SELL
2025-12-03 16:17:37,716 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:38,025 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:38,029 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/USDT/SELL
2025-12-03 16:17:38,032 - worker.extractor - INFO - Extracted 26 offers for ARS/USDT/SELL
2025-12-03 16:17:38,037 - worker.extractor - INFO - Extracting USD/BNB/BUY
2025-12-03 16:17:38,316 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:38,627 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:38,917 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:39,309 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:39,312 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/ETH/BUY
2025-12-03 16:17:39,312 - worker.extractor - INFO - Extracted 22 offers for ARS/ETH/BUY
2025-12-03 16:17:39,313 - worker.extractor - INFO - Extracting USD/BNB/SELL
2025-12-03 16:17:39,517 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:39,810 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:39,813 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BNB/BUY
2025-12-03 16:17:39,813 - worker.extractor - INFO - Extracted 21 offers for ARS/BNB/BUY
2025-12-03 16:17:39,814 - worker.extractor - INFO - Extracting USD/USDC/BUY
2025-12-03 16:17:40,117 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:40,476 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:40,717 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:41,000 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:41,004 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/USDT/BUY
2025-12-03 16:17:41,005 - worker.extractor - INFO - Extracted 25 offers for ARS/USDT/BUY
2025-12-03 16:17:41,006 - worker.extractor - INFO - Extracting USD/USDC/SELL
2025-12-03 16:17:41,318 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:41,652 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:41,918 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:42,227 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:42,230 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BTC/BUY
2025-12-03 16:17:42,231 - worker.extractor - INFO - Extracted 26 offers for ARS/BTC/BUY
2025-12-03 16:17:42,519 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:42,902 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:42,911 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BNB/SELL
2025-12-03 16:17:42,913 - worker.extractor - INFO - Extracted 25 offers for ARS/BNB/SELL
2025-12-03 16:17:43,119 - worker.rate_limiter - WARNING - Rate limiter active: 50 waits, 88 total requests
2025-12-03 16:17:43,120 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:43,450 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:43,720 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:44,009 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:44,320 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:44,680 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:44,683 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/USDT/SELL
2025-12-03 16:17:44,683 - worker.extractor - INFO - Extracted 26 offers for COP/USDT/SELL
2025-12-03 16:17:44,921 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:45,205 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:45,521 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:45,833 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:46,121 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:46,434 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:46,438 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/BTC/SELL
2025-12-03 16:17:46,439 - worker.extractor - INFO - Extracted 26 offers for COP/BTC/SELL
2025-12-03 16:17:46,722 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:47,012 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:47,323 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:47,673 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:47,676 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/ETH/SELL
2025-12-03 16:17:47,677 - worker.extractor - INFO - Extracted 25 offers for COP/ETH/SELL
2025-12-03 16:17:47,923 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:48,248 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:48,251 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/USDT/BUY
2025-12-03 16:17:48,251 - worker.extractor - INFO - Extracted 26 offers for VES/USDT/BUY
2025-12-03 16:17:48,525 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:48,803 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:48,806 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/BTC/BUY
2025-12-03 16:17:48,807 - worker.extractor - INFO - Extracted 25 offers for COP/BTC/BUY
2025-12-03 16:17:49,125 - worker.rate_limiter - WARNING - Rate limiter active: 60 waits, 98 total requests
2025-12-03 16:17:49,126 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:49,464 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:49,734 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:50,079 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:50,334 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:50,617 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:50,621 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/BTC/BUY
2025-12-03 16:17:50,623 - worker.extractor - INFO - Extracted 24 offers for VES/BTC/BUY
2025-12-03 16:17:50,935 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:51,219 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:51,537 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:51,903 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:52,137 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:52,420 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:52,433 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/USDT/SELL
2025-12-03 16:17:52,440 - worker.extractor - INFO - Extracted 26 offers for VES/USDT/SELL
2025-12-03 16:17:52,737 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:53,099 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:53,338 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:53,658 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:53,661 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDT/SELL
2025-12-03 16:17:53,662 - worker.extractor - INFO - Extracted 26 offers for USD/USDT/SELL
2025-12-03 16:17:53,938 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:54,247 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:54,250 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDT/BUY
2025-12-03 16:17:54,251 - worker.extractor - INFO - Extracted 26 offers for USD/USDT/BUY
2025-12-03 16:17:54,538 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:55,139 - worker.rate_limiter - WARNING - Rate limiter active: 70 waits, 108 total requests
2025-12-03 16:17:55,140 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:55,319 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:55,322 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/BTC/SELL
2025-12-03 16:17:55,323 - worker.extractor - INFO - Extracted 26 offers for VES/BTC/SELL
2025-12-03 16:17:55,449 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:55,748 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:56,064 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:56,349 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:56,727 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:56,950 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:57,307 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:57,552 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:57,824 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:58,152 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:58,426 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:58,752 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:59,210 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:59,354 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:17:59,731 - worker.extractor - INFO - Response status: 200
2025-12-03 16:17:59,957 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:18:00,270 - worker.extractor - INFO - Response status: 200
2025-12-03 16:18:00,557 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:18:00,958 - worker.extractor - INFO - Response status: 200
2025-12-03 16:18:01,197 - worker.rate_limiter - WARNING - Rate limiter active: 80 waits, 118 total requests
2025-12-03 16:18:01,277 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:18:01,753 - worker.extractor - INFO - Response status: 200
2025-12-03 16:18:01,801 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:18:02,402 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:18:02,468 - worker.extractor - INFO - Response status: 200
2025-12-03 16:18:02,872 - worker.extractor - INFO - Response status: 200
2025-12-03 16:18:03,003 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:18:03,405 - worker.extractor - INFO - Response status: 200
2025-12-03 16:18:03,612 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:18:03,901 - worker.extractor - INFO - Response status: 200
2025-12-03 16:18:04,226 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:18:04,576 - worker.extractor - INFO - Response status: 200
2025-12-03 16:18:04,827 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:18:05,112 - worker.extractor - INFO - Response status: 200
2025-12-03 16:18:05,427 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:18:05,702 - worker.extractor - INFO - Response status: 200
2025-12-03 16:18:06,028 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:18:06,345 - worker.extractor - INFO - Response status: 200
2025-12-03 16:18:06,628 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:18:06,913 - worker.extractor - INFO - Response status: 200
2025-12-03 16:18:07,229 - worker.rate_limiter - WARNING - Rate limiter active: 90 waits, 128 total requests
2025-12-03 16:18:07,229 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:18:07,629 - worker.extractor - INFO - Response status: 200
2025-12-03 16:18:07,829 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:18:08,120 - worker.extractor - INFO - Response status: 200
2025-12-03 16:18:08,430 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:18:08,822 - worker.extractor - INFO - Response status: 200
2025-12-03 16:18:09,037 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:18:09,321 - worker.extractor - INFO - Response status: 200
2025-12-03 16:18:09,638 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:18:09,930 - worker.extractor - INFO - Response status: 200
2025-12-03 16:18:09,933 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BTC/BUY
2025-12-03 16:18:09,934 - worker.extractor - INFO - Extracted 25 offers for USD/BTC/BUY
2025-12-03 16:18:10,238 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:18:10,839 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:18:10,967 - worker.extractor - INFO - Response status: 200
2025-12-03 16:18:10,970 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BTC/SELL
2025-12-03 16:18:10,970 - worker.extractor - INFO - Extracted 25 offers for USD/BTC/SELL
2025-12-03 16:18:11,114 - worker.extractor - INFO - Response status: 200
2025-12-03 16:18:11,130 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/ETH/BUY
2025-12-03 16:18:11,142 - worker.extractor - INFO - Extracted 25 offers for USD/ETH/BUY
2025-12-03 16:18:11,447 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:18:11,756 - worker.extractor - INFO - Response status: 200
2025-12-03 16:18:11,768 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/ETH/SELL
2025-12-03 16:18:11,771 - worker.extractor - INFO - Extracted 25 offers for USD/ETH/SELL
2025-12-03 16:18:12,048 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:18:12,427 - worker.extractor - INFO - Response status: 200
2025-12-03 16:18:12,430 - worker.extractor - INFO - No offers found for USD/BNB/BUY
2025-12-03 16:18:12,431 - worker.extractor - INFO - Extracted 20 offers for USD/BNB/BUY
2025-12-03 16:18:12,648 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:18:12,928 - worker.extractor - INFO - Response status: 200
2025-12-03 16:18:12,931 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BNB/SELL
2025-12-03 16:18:12,931 - worker.extractor - INFO - Extracted 25 offers for USD/BNB/SELL
2025-12-03 16:18:13,249 - worker.rate_limiter - WARNING - Rate limiter active: 100 waits, 138 total requests
2025-12-03 16:18:13,249 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:18:13,554 - worker.extractor - INFO - Response status: 200
2025-12-03 16:18:13,587 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDC/BUY
2025-12-03 16:18:13,601 - worker.extractor - INFO - Extracted 25 offers for USD/USDC/BUY
2025-12-03 16:18:13,850 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:18:14,143 - worker.extractor - INFO - Response status: 200
2025-12-03 16:18:14,152 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDC/SELL
2025-12-03 16:18:14,154 - worker.extractor - INFO - Extracted 25 offers for USD/USDC/SELL
2025-12-03 16:18:14,160 - worker.extractor - INFO - Total offers extracted: 687
2025-12-03 16:18:14,165 - worker.loader - INFO - Starting to load 687 offers for batch d769afbf-abad-45dd-aff3-e49bb8776aec...
2025-12-03 16:18:15,866 - worker.loader - ERROR - Error loading offers for batch d769afbf-abad-45dd-aff3-e49bb8776aec: (psycopg2.errors.NotNullViolation) null value in column "advertiser_id" of relation "dim_advertisers" violates not-null constraint
DETAIL:  Failing row contains (4, null, MoniMom, f, 0, 2025-12-03 21:18:15.484763, null, t, 2025-12-03 21:18:16.013335).

[SQL: INSERT INTO dim_advertisers (advertiser_id, nickname, is_merchant, registration_days, effective_date, expiration_date, is_current, created_at) VALUES (%(advertiser_id)s, %(nickname)s, %(is_merchant)s, %(registration_days)s, %(effective_date)s, %(expiration_date)s, %(is_current)s, now()) RETURNING dim_advertisers.advertiser_sk, dim_advertisers.created_at]
[parameters: {'advertiser_id': None, 'nickname': 'MoniMom', 'is_merchant': False, 'registration_days': 0, 'effective_date': datetime.datetime(2025, 12, 3, 21, 18, 15, 484763), 'expiration_date': None, 'is_current': True}]
(Background on this error at: https://sqlalche.me/e/20/gkpj)
Traceback (most recent call last):
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1963, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\default.py", line 943, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
psycopg2.errors.NotNullViolation: null value in column "advertiser_id" of relation "dim_advertisers" violates not-null constraint
DETAIL:  Failing row contains (4, null, MoniMom, f, 0, 2025-12-03 21:18:15.484763, null, t, 2025-12-03 21:18:16.013335).


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 50, in load_offers
    self._load_dimensions(session, offers)
    ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 156, in _load_dimensions
    self._get_or_create_advertiser(session, offer['advertiser']['id'], offer['advertiser']['nickname'])
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 147, in _get_or_create_advertiser
    session.flush()
    ~~~~~~~~~~~~~^^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\session.py", line 4345, in flush    self._flush(objects)
    ~~~~~~~~~~~^^^^^^^^^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\session.py", line 4480, in _flush
    with util.safe_reraise():
         ~~~~~~~~~~~~~~~~~^^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\util\langhelpers.py", line 224, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\session.py", line 4441, in _flush
    flush_context.execute()
    ~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\unitofwork.py", line 466, in execute
    rec.execute(self)
    ~~~~~~~~~~~^^^^^^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\unitofwork.py", line 642, in execute
    util.preloaded.orm_persistence.save_obj(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self.mapper,
        ^^^^^^^^^^^^
        uow.states_for_mapper_hierarchy(self.mapper, False, False),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        uow,
        ^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\persistence.py", line 93, in save_obj
    _emit_insert_statements(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        base_mapper,
        ^^^^^^^^^^^^
    ...<3 lines>...
        insert,
        ^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\persistence.py", line 1233, in _emit_insert_statements
    result = connection.execute(
        statement,
        params,
        execution_options=execution_options,
    )
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1415, in execute
    return meth(
        self,
        distilled_parameters,
        execution_options or NO_OPTIONS,
    )
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\sql\elements.py", line 523, in _execute_on_connection
    return connection._execute_clauseelement(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self, distilled_params, execution_options
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1637, in _execute_clauseelement
    ret = self._execute_context(
        dialect,
    ...<8 lines>...
        cache_hit=cache_hit,
    )
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1842, in _execute_context
    return self._exec_single_context(
           ~~~~~~~~~~~~~~~~~~~~~~~~~^
        dialect, context, statement, parameters
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1982, in _exec_single_context
    self._handle_dbapi_exception(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        e, str_statement, effective_parameters, cursor, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 2351, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1963, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\default.py", line 943, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
sqlalchemy.exc.IntegrityError: (psycopg2.errors.NotNullViolation) null value in column "advertiser_id" of relation "dim_advertisers" violates not-null constraint
DETAIL:  Failing row contains (4, null, MoniMom, f, 0, 2025-12-03 21:18:15.484763, null, t, 2025-12-03 21:18:16.013335).

[SQL: INSERT INTO dim_advertisers (advertiser_id, nickname, is_merchant, registration_days, effective_date, expiration_date, is_current, created_at) VALUES (%(advertiser_id)s, %(nickname)s, %(is_merchant)s, %(registration_days)s, %(effective_date)s, %(expiration_date)s, %(is_current)s, now()) RETURNING dim_advertisers.advertiser_sk, dim_advertisers.created_at]
[parameters: {'advertiser_id': None, 'nickname': 'MoniMom', 'is_merchant': False, 'registration_days': 0, 'effective_date': datetime.datetime(2025, 12, 3, 21, 18, 15, 484763), 'expiration_date': None, 'is_current': True}]
(Background on this error at: https://sqlalche.me/e/20/gkpj)
2025-12-03 16:18:15,947 - worker.db - ERROR - Database session error: (psycopg2.errors.NotNullViolation) null value 
in column "advertiser_id" of relation "dim_advertisers" violates not-null constraint
DETAIL:  Failing row contains (4, null, MoniMom, f, 0, 2025-12-03 21:18:15.484763, null, t, 2025-12-03 21:18:16.013335).

[SQL: INSERT INTO dim_advertisers (advertiser_id, nickname, is_merchant, registration_days, effective_date, expiration_date, is_current, created_at) VALUES (%(advertiser_id)s, %(nickname)s, %(is_merchant)s, %(registration_days)s, %(effective_date)s, %(expiration_date)s, %(is_current)s, now()) RETURNING dim_advertisers.advertiser_sk, dim_advertisers.created_at]
[parameters: {'advertiser_id': None, 'nickname': 'MoniMom', 'is_merchant': False, 'registration_days': 0, 'effective_date': datetime.datetime(2025, 12, 3, 21, 18, 15, 484763), 'expiration_date': None, 'is_current': True}]
(Background on this error at: https://sqlalche.me/e/20/gkpj)
2025-12-03 16:18:15,952 - __main__ - ERROR - An error occurred during the job: (psycopg2.errors.NotNullViolation) null value in column "advertiser_id" of relation "dim_advertisers" violates not-null constraint
DETAIL:  Failing row contains (4, null, MoniMom, f, 0, 2025-12-03 21:18:15.484763, null, t, 2025-12-03 21:18:16.013335).

[SQL: INSERT INTO dim_advertisers (advertiser_id, nickname, is_merchant, registration_days, effective_date, expiration_date, is_current, created_at) VALUES (%(advertiser_id)s, %(nickname)s, %(is_merchant)s, %(registration_days)s, %(effective_date)s, %(expiration_date)s, %(is_current)s, now()) RETURNING dim_advertisers.advertiser_sk, dim_advertisers.created_at]
[parameters: {'advertiser_id': None, 'nickname': 'MoniMom', 'is_merchant': False, 'registration_days': 0, 'effective_date': datetime.datetime(2025, 12, 3, 21, 18, 15, 484763), 'expiration_date': None, 'is_current': True}]
(Background on this error at: https://sqlalche.me/e/20/gkpj)
Traceback (most recent call last):
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1963, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\default.py", line 943, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
psycopg2.errors.NotNullViolation: null value in column "advertiser_id" of relation "dim_advertisers" violates not-null constraint
DETAIL:  Failing row contains (4, null, MoniMom, f, 0, 2025-12-03 21:18:15.484763, null, t, 2025-12-03 21:18:16.013335).


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\DELL\Desktop\dashboards\worker\main.py", line 31, in job
    loader.load_offers(offers, batch_id)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 50, in load_offers
    self._load_dimensions(session, offers)
    ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 156, in _load_dimensions
    self._get_or_create_advertiser(session, offer['advertiser']['id'], offer['advertiser']['nickname'])
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 147, in _get_or_create_advertiser
    session.flush()
    ~~~~~~~~~~~~~^^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\session.py", line 4345, in flush    self._flush(objects)
    ~~~~~~~~~~~^^^^^^^^^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\session.py", line 4480, in _flush
    with util.safe_reraise():
         ~~~~~~~~~~~~~~~~~^^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\util\langhelpers.py", line 224, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\session.py", line 4441, in _flush
    flush_context.execute()
    ~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\unitofwork.py", line 466, in execute
    rec.execute(self)
    ~~~~~~~~~~~^^^^^^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\unitofwork.py", line 642, in execute
    util.preloaded.orm_persistence.save_obj(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self.mapper,
        ^^^^^^^^^^^^
        uow.states_for_mapper_hierarchy(self.mapper, False, False),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        uow,
        ^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\persistence.py", line 93, in save_obj
    _emit_insert_statements(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        base_mapper,
        ^^^^^^^^^^^^
    ...<3 lines>...
        insert,
        ^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\orm\persistence.py", line 1233, in _emit_insert_statements
    result = connection.execute(
        statement,
        params,
        execution_options=execution_options,
    )
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1415, in execute
    return meth(
        self,
        distilled_parameters,
        execution_options or NO_OPTIONS,
    )
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\sql\elements.py", line 523, in _execute_on_connection
    return connection._execute_clauseelement(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self, distilled_params, execution_options
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1637, in _execute_clauseelement
    ret = self._execute_context(
        dialect,
    ...<8 lines>...
        cache_hit=cache_hit,
    )
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1842, in _execute_context
    return self._exec_single_context(
           ~~~~~~~~~~~~~~~~~~~~~~~~~^
        dialect, context, statement, parameters
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1982, in _exec_single_context
    self._handle_dbapi_exception(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        e, str_statement, effective_parameters, cursor, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 2351, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\base.py", line 1963, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\sqlalchemy\engine\default.py", line 943, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
sqlalchemy.exc.IntegrityError: (psycopg2.errors.NotNullViolation) null value in column "advertiser_id" of relation "dim_advertisers" violates not-null constraint
DETAIL:  Failing row contains (4, null, MoniMom, f, 0, 2025-12-03 21:18:15.484763, null, t, 2025-12-03 21:18:16.013335).

[SQL: INSERT INTO dim_advertisers (advertiser_id, nickname, is_merchant, registration_days, effective_date, expiration_date, is_current, created_at) VALUES (%(advertiser_id)s, %(nickname)s, %(is_merchant)s, %(registration_days)s, %(effective_date)s, %(expiration_date)s, %(is_current)s, now()) RETURNING dim_advertisers.advertiser_sk, dim_advertisers.created_at]
[parameters: {'advertiser_id': None, 'nickname': 'MoniMom', 'is_merchant': False, 'registration_days': 0, 'effective_date': datetime.datetime(2025, 12, 3, 21, 18, 15, 484763), 'expiration_date': None, 'is_current': True}]
(Background on this error at: https://sqlalche.me/e/20/gkpj)

# Thirteenth run


(.venv) PS C:\Users\DELL\Desktop\dashboards> python -m worker.main 
2025-12-03 16:27:35,014 - __main__ - INFO - Worker starting. Job will run every 10 minutes.
2025-12-03 16:27:35,091 - __main__ - INFO - Starting P2P data extraction job...
2025-12-03 16:27:35,123 - worker.extractor - INFO - Fetching all trading pairs...
2025-12-03 16:27:35,178 - worker.extractor - INFO - Generating trading pairs from p2p_config.json...
2025-12-03 16:27:35,235 - worker.extractor - INFO - Generated 28 trading pairs from configuration.
2025-12-03 16:27:35,250 - worker.extractor - INFO - Starting parallel extraction for 28 pairs...
2025-12-03 16:27:35,336 - worker.extractor - INFO - Extracting ARS/USDT/BUY
2025-12-03 16:27:35,350 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:35,376 - worker.extractor - INFO - Extracting ARS/USDT/SELL
2025-12-03 16:27:35,403 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:35,423 - worker.extractor - INFO - Extracting ARS/BTC/BUY
2025-12-03 16:27:35,437 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:35,452 - worker.extractor - INFO - Extracting ARS/BTC/SELL
2025-12-03 16:27:35,489 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:35,520 - worker.extractor - INFO - Extracting ARS/ETH/BUY
2025-12-03 16:27:35,626 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:35,627 - worker.extractor - INFO - Extracting ARS/ETH/SELL
2025-12-03 16:27:35,750 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:35,793 - worker.extractor - INFO - Extracting ARS/BNB/BUY
2025-12-03 16:27:35,877 - worker.extractor - INFO - Extracting ARS/BNB/SELL
2025-12-03 16:27:35,878 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:35,957 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:35,957 - worker.extractor - INFO - Extracting COP/USDT/BUY
2025-12-03 16:27:36,127 - worker.extractor - INFO - Extracting COP/USDT/SELL
2025-12-03 16:27:36,177 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:36,309 - worker.extractor - INFO - Extracting COP/BTC/BUY
2025-12-03 16:27:36,310 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:36,405 - worker.extractor - INFO - Extracting COP/BTC/SELL
2025-12-03 16:27:36,418 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:36,547 - worker.extractor - INFO - Extracting COP/ETH/BUY
2025-12-03 16:27:36,547 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:36,777 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:36,789 - worker.extractor - INFO - Extracting COP/ETH/SELL
2025-12-03 16:27:37,110 - worker.extractor - INFO - Extracting VES/USDT/BUY
2025-12-03 16:27:37,404 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:37,406 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:37,559 - worker.extractor - INFO - Extracting VES/USDT/SELL
2025-12-03 16:27:37,790 - worker.extractor - INFO - Extracting VES/BTC/BUY
2025-12-03 16:27:38,074 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:38,074 - worker.extractor - INFO - Extracting VES/BTC/SELL
2025-12-03 16:27:38,427 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:38,612 - worker.extractor - INFO - Extracting USD/USDT/BUY
2025-12-03 16:27:38,823 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:39,327 - worker.extractor - INFO - Extracting USD/USDT/SELL
2025-12-03 16:27:39,423 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:39,723 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:42,661 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:42,842 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:42,992 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:43,231 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:43,273 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:43,371 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:43,668 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:43,681 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:44,120 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:44,284 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:44,287 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:44,609 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:44,685 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:44,759 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:44,918 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:45,010 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:45,042 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:45,152 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:45,290 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:45,440 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:45,470 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:45,472 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:45,562 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:45,589 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:45,603 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:45,738 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:45,860 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:45,920 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:45,964 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:46,062 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:46,104 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:46,127 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:27:46,185 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:27:46,248 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:27:46,287 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:46,491 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:46,599 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:46,600 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:46,622 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:46,831 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:46,883 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:46,967 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:47,018 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:47,035 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:47,106 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:47,198 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:47,201 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:27:47,369 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:47,370 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:27:47,381 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:27:47,478 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:47,486 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:47,498 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:47,533 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:47,660 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:47,686 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:47,745 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:47,746 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:27:47,752 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:27:47,763 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:27:47,893 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:27:47,971 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:47,974 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:48,146 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:48,193 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:48,429 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:48,454 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:48,520 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:48,534 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:48,595 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:48,596 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:48,649 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:48,968 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:49,085 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:49,089 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BTC/SELL
2025-12-03 16:27:49,092 - worker.extractor - INFO - Extracted 26 offers for ARS/BTC/SELL
2025-12-03 16:27:49,093 - worker.extractor - INFO - Extracting USD/BTC/BUY
2025-12-03 16:27:49,201 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:49,478 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:49,481 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BTC/BUY
2025-12-03 16:27:49,484 - worker.extractor - INFO - Extracted 26 offers for ARS/BTC/BUY
2025-12-03 16:27:49,485 - worker.extractor - INFO - Extracting USD/BTC/SELL
2025-12-03 16:27:49,804 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:50,091 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:50,407 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:50,698 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:51,005 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:51,274 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:51,606 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:51,870 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:52,206 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:52,494 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:52,807 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:53,099 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:53,408 - worker.rate_limiter - WARNING - Rate limiter active: 10 waits, 50 total requests
2025-12-03 16:27:53,409 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:53,703 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:54,009 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:54,289 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:54,609 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:54,914 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:55,220 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:55,535 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:55,821 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:56,171 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:56,422 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:57,022 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:57,145 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:57,350 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:57,623 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:57,918 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:57,920 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/USDT/SELL
2025-12-03 16:27:57,922 - worker.extractor - INFO - Extracted 26 offers for ARS/USDT/SELL
2025-12-03 16:27:57,925 - worker.extractor - INFO - Extracting USD/ETH/BUY
2025-12-03 16:27:58,223 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:58,509 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:58,824 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:59,108 - worker.extractor - INFO - Response status: 200
2025-12-03 16:27:59,425 - worker.rate_limiter - WARNING - Rate limiter active: 20 waits, 60 total requests
2025-12-03 16:27:59,426 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:27:59,707 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:00,032 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:00,341 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:00,633 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:00,909 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:01,234 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:01,512 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:01,834 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:02,121 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:02,434 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:02,712 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:03,037 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:03,365 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:03,366 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/USDT/BUY
2025-12-03 16:28:03,366 - worker.extractor - INFO - Extracted 26 offers for ARS/USDT/BUY
2025-12-03 16:28:03,367 - worker.extractor - INFO - Extracting USD/ETH/SELL
2025-12-03 16:28:03,638 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:03,998 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:04,238 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:04,785 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:04,851 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:05,452 - worker.rate_limiter - WARNING - Rate limiter active: 30 waits, 70 total requests
2025-12-03 16:28:05,453 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:06,052 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:06,654 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:06,913 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:06,970 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:07,143 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:07,254 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:07,365 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:07,540 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:07,862 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:08,320 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:08,463 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:09,064 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:09,126 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:09,664 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:10,265 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:10,337 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:10,624 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:10,866 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:11,141 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:11,466 - worker.rate_limiter - WARNING - Rate limiter active: 40 waits, 80 total requests
2025-12-03 16:28:11,467 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:11,712 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:11,718 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/ETH/SELL
2025-12-03 16:28:11,720 - worker.extractor - INFO - Extracted 25 offers for ARS/ETH/SELL
2025-12-03 16:28:11,721 - worker.extractor - INFO - Extracting USD/BNB/BUY
2025-12-03 16:28:11,804 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:12,067 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:12,363 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:12,690 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:13,042 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:13,290 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:13,715 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:13,891 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:14,271 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:14,497 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:15,121 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:15,540 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:15,540 - worker.extractor - INFO - No offers found for COP/ETH/BUY
2025-12-03 16:28:15,541 - worker.extractor - INFO - Extracted 14 offers for COP/ETH/BUY
2025-12-03 16:28:15,542 - worker.extractor - INFO - Extracting USD/BNB/SELL
2025-12-03 16:28:15,559 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:15,722 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:16,076 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:16,322 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:16,732 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:16,923 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:17,208 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:17,523 - worker.rate_limiter - WARNING - Rate limiter active: 50 waits, 90 total requests
2025-12-03 16:28:17,524 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:17,808 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:17,810 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BNB/BUY
2025-12-03 16:28:17,811 - worker.extractor - INFO - Extracted 21 offers for ARS/BNB/BUY
2025-12-03 16:28:17,817 - worker.extractor - INFO - Extracting USD/USDC/BUY
2025-12-03 16:28:18,126 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:18,516 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:18,726 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:19,327 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:19,460 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:19,463 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/BTC/BUY
2025-12-03 16:28:19,466 - worker.extractor - INFO - Extracted 25 offers for COP/BTC/BUY
2025-12-03 16:28:19,468 - worker.extractor - INFO - Extracting USD/USDC/SELL
2025-12-03 16:28:19,625 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:19,626 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/USDT/BUY
2025-12-03 16:28:19,626 - worker.extractor - INFO - Extracted 26 offers for COP/USDT/BUY
2025-12-03 16:28:19,927 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:20,201 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:20,202 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BNB/SELL
2025-12-03 16:28:20,203 - worker.extractor - INFO - Extracted 25 offers for ARS/BNB/SELL
2025-12-03 16:28:20,528 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:20,863 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:21,128 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:21,415 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:21,728 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:22,017 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:22,018 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/ETH/BUY
2025-12-03 16:28:22,019 - worker.extractor - INFO - Extracted 22 offers for ARS/ETH/BUY
2025-12-03 16:28:22,331 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:22,625 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:22,627 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/USDT/SELL
2025-12-03 16:28:22,628 - worker.extractor - INFO - Extracted 26 offers for COP/USDT/SELL
2025-12-03 16:28:22,931 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:23,202 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:23,532 - worker.rate_limiter - WARNING - Rate limiter active: 60 waits, 100 total requests
2025-12-03 16:28:23,533 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:23,900 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:23,901 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/USDT/BUY
2025-12-03 16:28:23,902 - worker.extractor - INFO - Extracted 26 offers for VES/USDT/BUY
2025-12-03 16:28:24,133 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:24,395 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:24,397 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/ETH/SELL
2025-12-03 16:28:24,398 - worker.extractor - INFO - Extracted 25 offers for COP/ETH/SELL
2025-12-03 16:28:24,735 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:25,014 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:25,336 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:25,637 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:25,936 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:26,208 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:26,209 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/BTC/SELL
2025-12-03 16:28:26,209 - worker.extractor - INFO - Extracted 26 offers for COP/BTC/SELL
2025-12-03 16:28:26,537 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:26,805 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:27,137 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:27,404 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:27,738 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:27,995 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:27,996 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/BTC/BUY
2025-12-03 16:28:27,997 - worker.extractor - INFO - Extracted 23 offers for VES/BTC/BUY
2025-12-03 16:28:28,338 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:28,606 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:28,608 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/BTC/SELL
2025-12-03 16:28:28,608 - worker.extractor - INFO - Extracted 26 offers for VES/BTC/SELL
2025-12-03 16:28:28,938 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:29,220 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:29,221 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDT/SELL
2025-12-03 16:28:29,222 - worker.extractor - INFO - Extracted 26 offers for USD/USDT/SELL
2025-12-03 16:28:29,538 - worker.rate_limiter - WARNING - Rate limiter active: 70 waits, 110 total requests
2025-12-03 16:28:29,540 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:29,817 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:30,139 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:30,422 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:30,424 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/USDT/SELL
2025-12-03 16:28:30,424 - worker.extractor - INFO - Extracted 26 offers for VES/USDT/SELL
2025-12-03 16:28:30,739 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:31,008 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:31,340 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:31,608 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:31,609 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDT/BUY
2025-12-03 16:28:31,609 - worker.extractor - INFO - Extracted 26 offers for USD/USDT/BUY
2025-12-03 16:28:31,942 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:32,229 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:32,542 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:32,828 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:33,151 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:33,459 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:33,752 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:34,021 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:34,353 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:34,618 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:34,953 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:35,319 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:35,553 - worker.rate_limiter - WARNING - Rate limiter active: 80 waits, 120 total requests
2025-12-03 16:28:35,554 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:35,836 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:36,154 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:36,429 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:36,755 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:37,130 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:37,355 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:37,661 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:37,960 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:38,250 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:38,251 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BTC/BUY
2025-12-03 16:28:38,252 - worker.extractor - INFO - Extracted 25 offers for USD/BTC/BUY
2025-12-03 16:28:38,561 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:38,835 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:38,842 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BTC/SELL
2025-12-03 16:28:38,844 - worker.extractor - INFO - Extracted 25 offers for USD/BTC/SELL
2025-12-03 16:28:39,161 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:39,445 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:39,761 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:40,040 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:40,362 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:40,645 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:40,962 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:41,246 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:41,562 - worker.rate_limiter - WARNING - Rate limiter active: 90 waits, 130 total requests
2025-12-03 16:28:41,563 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:41,830 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:41,831 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/ETH/BUY
2025-12-03 16:28:41,832 - worker.extractor - INFO - Extracted 25 offers for USD/ETH/BUY
2025-12-03 16:28:42,164 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:42,444 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:42,764 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:43,185 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:43,365 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:43,659 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:43,663 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/ETH/SELL
2025-12-03 16:28:43,664 - worker.extractor - INFO - Extracted 25 offers for USD/ETH/SELL
2025-12-03 16:28:43,965 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:44,302 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:44,567 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:45,167 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:45,282 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:45,426 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:45,427 - worker.extractor - INFO - No offers found for USD/BNB/BUY
2025-12-03 16:28:45,427 - worker.extractor - INFO - Extracted 20 offers for USD/BNB/BUY
2025-12-03 16:28:45,768 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:46,051 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:46,053 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BNB/SELL
2025-12-03 16:28:46,054 - worker.extractor - INFO - Extracted 25 offers for USD/BNB/SELL
2025-12-03 16:28:46,369 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:46,667 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:46,668 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDC/BUY
2025-12-03 16:28:46,669 - worker.extractor - INFO - Extracted 25 offers for USD/USDC/BUY
2025-12-03 16:28:46,969 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:28:47,607 - worker.extractor - INFO - Response status: 200
2025-12-03 16:28:47,608 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDC/SELL
2025-12-03 16:28:47,608 - worker.extractor - INFO - Extracted 25 offers for USD/USDC/SELL
2025-12-03 16:28:47,611 - worker.extractor - INFO - Total offers extracted: 687
2025-12-03 16:28:47,613 - worker.loader - INFO - Starting to load 687 offers for batch 74665141-13c5-4434-bef0-442b51df2b1d...
2025-12-03 16:28:49,214 - worker.loader - ERROR - Error loading offers for batch 74665141-13c5-4434-bef0-442b51df2b1d: string indices must be integers, not 'str'
Traceback (most recent call last):
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 50, in load_offers
    self._load_dimensions(session, offers)
    ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 158, in _load_dimensions
    self._get_or_create_payment_method(session, pm['identifier'], pm['tradeMethodName'])
                                                ~~^^^^^^^^^^^^^^
TypeError: string indices must be integers, not 'str'
2025-12-03 16:28:49,381 - worker.db - ERROR - Database session error: string indices must be integers, not 'str'
2025-12-03 16:28:49,383 - __main__ - ERROR - An error occurred during the job: string indices must be integers, not 
'str'
Traceback (most recent call last):
  File "C:\Users\DELL\Desktop\dashboards\worker\main.py", line 31, in job
    loader.load_offers(offers, batch_id)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 50, in load_offers
    self._load_dimensions(session, offers)
    ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 158, in _load_dimensions
    self._get_or_create_payment_method(session, pm['identifier'], pm['tradeMethodName'])
                                                ~~^^^^^^^^^^^^^^
TypeError: string indices must be integers, not 'str'

# Fourteenth run


(.venv) PS C:\Users\DELL\Desktop\dashboards> python -m worker.main 
2025-12-03 16:41:16,342 - __main__ - INFO - Worker starting. Job will run every 10 minutes.
2025-12-03 16:41:16,346 - __main__ - INFO - Starting P2P data extraction job...
2025-12-03 16:41:16,348 - worker.extractor - INFO - Fetching all trading pairs...
2025-12-03 16:41:16,351 - worker.extractor - INFO - Generating trading pairs from p2p_config.json...
2025-12-03 16:41:16,354 - worker.extractor - INFO - Generated 28 trading pairs from configuration.
2025-12-03 16:41:16,358 - worker.extractor - INFO - Starting parallel extraction for 28 pairs...
2025-12-03 16:41:16,378 - worker.extractor - INFO - Extracting ARS/USDT/BUY
2025-12-03 16:41:16,389 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:16,389 - worker.extractor - INFO - Extracting ARS/USDT/SELL
2025-12-03 16:41:16,399 - worker.extractor - INFO - Extracting ARS/BTC/BUY
2025-12-03 16:41:16,407 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:16,440 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:16,440 - worker.extractor - INFO - Extracting ARS/BTC/SELL
2025-12-03 16:41:16,468 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:16,450 - worker.extractor - INFO - Extracting ARS/ETH/BUY
2025-12-03 16:41:16,486 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:16,490 - worker.extractor - INFO - Extracting ARS/ETH/SELL
2025-12-03 16:41:16,503 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:16,504 - worker.extractor - INFO - Extracting ARS/BNB/BUY
2025-12-03 16:41:16,507 - worker.extractor - INFO - Extracting ARS/BNB/SELL
2025-12-03 16:41:16,507 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:16,513 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:16,522 - worker.extractor - INFO - Extracting COP/USDT/BUY
2025-12-03 16:41:16,537 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:16,539 - worker.extractor - INFO - Extracting COP/USDT/SELL
2025-12-03 16:41:16,560 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:16,571 - worker.extractor - INFO - Extracting COP/BTC/BUY
2025-12-03 16:41:16,578 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:16,578 - worker.extractor - INFO - Extracting COP/BTC/SELL
2025-12-03 16:41:16,606 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:16,631 - worker.extractor - INFO - Extracting COP/ETH/BUY
2025-12-03 16:41:16,643 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:16,645 - worker.extractor - INFO - Extracting COP/ETH/SELL
2025-12-03 16:41:16,651 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:16,655 - worker.extractor - INFO - Extracting VES/USDT/BUY
2025-12-03 16:41:16,656 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:16,673 - worker.extractor - INFO - Extracting VES/USDT/SELL
2025-12-03 16:41:16,684 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:16,688 - worker.extractor - INFO - Extracting VES/BTC/BUY
2025-12-03 16:41:16,698 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:16,760 - worker.extractor - INFO - Extracting VES/BTC/SELL
2025-12-03 16:41:17,103 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:17,248 - worker.extractor - INFO - Extracting USD/USDT/BUY
2025-12-03 16:41:17,266 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:17,270 - worker.extractor - INFO - Extracting USD/USDT/SELL
2025-12-03 16:41:17,599 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:24,750 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:24,764 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:25,030 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,049 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:25,117 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,117 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,117 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,139 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:25,150 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,178 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:25,190 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:25,198 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,209 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:25,221 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,222 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,222 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,253 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,279 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,303 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,329 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:25,338 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:25,350 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:25,357 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:25,359 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,370 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:25,371 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:25,373 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,412 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:25,418 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,451 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,483 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,484 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:41:25,534 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:25,548 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,592 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:25,614 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,765 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,813 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,864 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,865 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,866 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,890 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,890 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:41:25,901 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,939 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:41:25,940 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:41:25,941 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:41:25,941 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:41:25,950 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,951 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,952 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,954 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:25,992 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:25,992 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:41:25,994 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:41:25,996 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:41:25,997 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:41:26,005 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:26,006 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:26,010 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:26,011 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:26,309 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:26,592 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:26,879 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:27,193 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:27,494 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:27,793 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:28,083 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:28,394 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:28,694 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:28,695 - worker.extractor - INFO - No offers found for COP/ETH/BUY
2025-12-03 16:41:28,695 - worker.extractor - INFO - Extracted 14 offers for COP/ETH/BUY
2025-12-03 16:41:28,696 - worker.extractor - INFO - Extracting USD/BTC/BUY
2025-12-03 16:41:28,995 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:29,291 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:29,595 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:29,859 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:30,195 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:30,470 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:30,796 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:31,096 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:31,397 - worker.rate_limiter - WARNING - Rate limiter active: 10 waits, 45 total requests
2025-12-03 16:41:31,398 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:31,688 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:31,998 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:32,299 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:32,599 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:32,893 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:33,199 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:33,467 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:33,800 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:34,077 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:34,401 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:34,696 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:35,010 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:35,291 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:35,610 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:35,877 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:36,210 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:36,479 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:36,811 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:37,099 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:37,418 - worker.rate_limiter - WARNING - Rate limiter active: 20 waits, 55 total requests
2025-12-03 16:41:37,430 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:37,791 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:38,022 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:38,299 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:38,622 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:38,910 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:39,223 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:39,584 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:39,830 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:40,130 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:40,430 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:40,709 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:41,030 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:41,310 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:41,631 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:41,891 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:42,233 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:42,519 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:42,833 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:43,112 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:43,434 - worker.rate_limiter - WARNING - Rate limiter active: 30 waits, 65 total requests
2025-12-03 16:41:43,434 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:43,716 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:44,034 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:44,320 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:44,634 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:44,912 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:45,235 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:45,538 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:45,836 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:46,119 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:46,437 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:46,728 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:47,037 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:47,350 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:47,638 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:47,902 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:48,239 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:48,839 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:48,959 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:49,138 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:49,138 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/BTC/BUY
2025-12-03 16:41:49,139 - worker.extractor - INFO - Extracted 23 offers for VES/BTC/BUY
2025-12-03 16:41:49,139 - worker.extractor - INFO - Extracting USD/BTC/SELL
2025-12-03 16:41:49,440 - worker.rate_limiter - WARNING - Rate limiter active: 40 waits, 75 total requests
2025-12-03 16:41:49,440 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:49,724 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:50,041 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:50,308 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:50,641 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:50,905 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:51,242 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:51,525 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:51,842 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:52,129 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:52,443 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:52,715 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:53,044 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:53,324 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:53,325 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/USDT/SELL
2025-12-03 16:41:53,325 - worker.extractor - INFO - Extracted 26 offers for VES/USDT/SELL
2025-12-03 16:41:53,326 - worker.extractor - INFO - Extracting USD/ETH/BUY
2025-12-03 16:41:53,645 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:53,906 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:53,908 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/BTC/BUY
2025-12-03 16:41:53,910 - worker.extractor - INFO - Extracted 25 offers for COP/BTC/BUY
2025-12-03 16:41:53,911 - worker.extractor - INFO - Extracting USD/ETH/SELL
2025-12-03 16:41:54,245 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:54,526 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:54,527 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/ETH/SELL
2025-12-03 16:41:54,528 - worker.extractor - INFO - Extracted 25 offers for COP/ETH/SELL
2025-12-03 16:41:54,528 - worker.extractor - INFO - Extracting USD/BNB/BUY
2025-12-03 16:41:54,846 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:55,122 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:55,123 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/USDT/SELL
2025-12-03 16:41:55,123 - worker.extractor - INFO - Extracted 26 offers for COP/USDT/SELL
2025-12-03 16:41:55,124 - worker.extractor - INFO - Extracting USD/BNB/SELL
2025-12-03 16:41:55,446 - worker.rate_limiter - WARNING - Rate limiter active: 50 waits, 85 total requests
2025-12-03 16:41:55,447 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:55,714 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:56,047 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:56,348 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:56,351 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/USDT/BUY
2025-12-03 16:41:56,353 - worker.extractor - INFO - Extracted 26 offers for COP/USDT/BUY
2025-12-03 16:41:56,358 - worker.extractor - INFO - Extracting USD/USDC/BUY
2025-12-03 16:41:56,647 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:56,919 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:56,921 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BTC/BUY
2025-12-03 16:41:56,921 - worker.extractor - INFO - Extracted 26 offers for ARS/BTC/BUY
2025-12-03 16:41:56,922 - worker.extractor - INFO - Extracting USD/USDC/SELL
2025-12-03 16:41:57,248 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:57,580 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:57,582 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/BTC/SELL
2025-12-03 16:41:57,584 - worker.extractor - INFO - Extracted 26 offers for COP/BTC/SELL
2025-12-03 16:41:57,848 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:58,134 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:58,449 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:58,711 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:58,712 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/USDT/BUY
2025-12-03 16:41:58,714 - worker.extractor - INFO - Extracted 26 offers for VES/USDT/BUY
2025-12-03 16:41:59,049 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:59,331 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:59,650 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:41:59,932 - worker.extractor - INFO - Response status: 200
2025-12-03 16:41:59,933 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/ETH/BUY
2025-12-03 16:41:59,934 - worker.extractor - INFO - Extracted 22 offers for ARS/ETH/BUY
2025-12-03 16:42:00,250 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:00,603 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:00,605 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/ETH/SELL
2025-12-03 16:42:00,606 - worker.extractor - INFO - Extracted 25 offers for ARS/ETH/SELL
2025-12-03 16:42:00,850 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:01,170 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:01,451 - worker.rate_limiter - WARNING - Rate limiter active: 60 waits, 95 total requests
2025-12-03 16:42:01,451 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:01,815 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:01,817 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/USDT/SELL
2025-12-03 16:42:01,818 - worker.extractor - INFO - Extracted 26 offers for ARS/USDT/SELL
2025-12-03 16:42:02,051 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:02,444 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:02,445 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BNB/BUY
2025-12-03 16:42:02,446 - worker.extractor - INFO - Extracted 21 offers for ARS/BNB/BUY
2025-12-03 16:42:02,652 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:02,929 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:02,930 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BTC/SELL
2025-12-03 16:42:02,931 - worker.extractor - INFO - Extracted 26 offers for ARS/BTC/SELL
2025-12-03 16:42:03,252 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:03,608 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:03,609 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDT/SELL
2025-12-03 16:42:03,610 - worker.extractor - INFO - Extracted 26 offers for USD/USDT/SELL
2025-12-03 16:42:03,853 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:04,138 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:04,139 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/USDT/BUY
2025-12-03 16:42:04,139 - worker.extractor - INFO - Extracted 26 offers for ARS/USDT/BUY
2025-12-03 16:42:04,453 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:04,723 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:05,054 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:05,342 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:05,661 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:05,965 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:06,261 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:06,581 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:06,861 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:07,142 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:07,462 - worker.rate_limiter - WARNING - Rate limiter active: 70 waits, 105 total requests
2025-12-03 16:42:07,462 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:07,752 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:07,754 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BNB/SELL
2025-12-03 16:42:07,755 - worker.extractor - INFO - Extracted 25 offers for ARS/BNB/SELL
2025-12-03 16:42:08,062 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:08,348 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:08,663 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:08,949 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:09,264 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:09,864 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:09,979 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:09,981 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDT/BUY
2025-12-03 16:42:09,982 - worker.extractor - INFO - Extracted 26 offers for USD/USDT/BUY
2025-12-03 16:42:10,141 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:10,142 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/BTC/SELL
2025-12-03 16:42:10,143 - worker.extractor - INFO - Extracted 26 offers for VES/BTC/SELL
2025-12-03 16:42:10,466 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:10,777 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:11,066 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:11,368 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:11,666 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:11,932 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:12,267 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:12,566 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:12,868 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:13,168 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:13,469 - worker.rate_limiter - WARNING - Rate limiter active: 80 waits, 115 total requests
2025-12-03 16:42:13,469 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:13,745 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:14,069 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:14,360 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:14,670 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:15,018 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:15,271 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:15,546 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:15,872 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:16,152 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:16,153 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BTC/BUY
2025-12-03 16:42:16,153 - worker.extractor - INFO - Extracted 25 offers for USD/BTC/BUY
2025-12-03 16:42:16,473 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:16,745 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:17,073 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:17,352 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:17,674 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:17,954 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:18,274 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:18,567 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:18,875 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:19,158 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:19,476 - worker.rate_limiter - WARNING - Rate limiter active: 90 waits, 125 total requests
2025-12-03 16:42:19,476 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:19,753 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:20,077 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:20,364 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:20,677 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:20,942 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:21,277 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:21,565 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:21,878 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:22,174 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:22,487 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:22,786 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:23,088 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:23,373 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:23,688 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:23,978 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:24,289 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:24,630 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:24,634 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BTC/SELL
2025-12-03 16:42:24,639 - worker.extractor - INFO - Extracted 25 offers for USD/BTC/SELL
2025-12-03 16:42:24,904 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:25,505 - worker.rate_limiter - WARNING - Rate limiter active: 100 waits, 135 total requests
2025-12-03 16:42:25,506 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:25,672 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:25,673 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/ETH/BUY
2025-12-03 16:42:25,673 - worker.extractor - INFO - Extracted 25 offers for USD/ETH/BUY
2025-12-03 16:42:25,790 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:25,791 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/ETH/SELL
2025-12-03 16:42:25,791 - worker.extractor - INFO - Extracted 25 offers for USD/ETH/SELL
2025-12-03 16:42:26,105 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:26,369 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:26,370 - worker.extractor - INFO - No offers found for USD/BNB/BUY
2025-12-03 16:42:26,371 - worker.extractor - INFO - Extracted 20 offers for USD/BNB/BUY
2025-12-03 16:42:26,705 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:26,994 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:26,995 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BNB/SELL
2025-12-03 16:42:26,995 - worker.extractor - INFO - Extracted 25 offers for USD/BNB/SELL
2025-12-03 16:42:27,307 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:27,593 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:27,595 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDC/BUY
2025-12-03 16:42:27,597 - worker.extractor - INFO - Extracted 25 offers for USD/USDC/BUY
2025-12-03 16:42:27,907 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:42:28,482 - worker.extractor - INFO - Response status: 200
2025-12-03 16:42:28,483 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDC/SELL
2025-12-03 16:42:28,483 - worker.extractor - INFO - Extracted 25 offers for USD/USDC/SELL
2025-12-03 16:42:28,487 - worker.extractor - INFO - Total offers extracted: 687
2025-12-03 16:42:28,488 - worker.loader - INFO - Starting to load 687 offers for batch e8196a9c-e6d4-4e4e-903a-2bd41fdffdff...
2025-12-03 16:46:11,523 - worker.loader - ERROR - Error loading offers for batch e8196a9c-e6d4-4e4e-903a-2bd41fdffdff: 'id'
Traceback (most recent call last):
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 51, in load_offers
    self._load_facts(session, offers, batch_id)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 168, in _load_facts
    offer_external_id=offer['id'],
                      ~~~~~^^^^^^
KeyError: 'id'
2025-12-03 16:46:11,730 - worker.db - ERROR - Database session error: 'id'
2025-12-03 16:46:11,731 - __main__ - ERROR - An error occurred during the job: 'id'
Traceback (most recent call last):
  File "C:\Users\DELL\Desktop\dashboards\worker\main.py", line 31, in job
    loader.load_offers(offers, batch_id)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 51, in load_offers
    self._load_facts(session, offers, batch_id)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 168, in _load_facts
    offer_external_id=offer['id'],
                      ~~~~~^^^^^^
KeyError: 'id'


# fifteenth 

(.venv) PS C:\Users\DELL\Desktop\dashboards> python -m worker.main
2025-12-03 16:52:16,976 - __main__ - INFO - Worker starting. Job will run every 10 minutes.
2025-12-03 16:52:16,977 - __main__ - INFO - Starting P2P data extraction job...
2025-12-03 16:52:16,977 - worker.extractor - INFO - Fetching all trading pairs...
2025-12-03 16:52:16,978 - worker.extractor - INFO - Generating trading pairs from p2p_config.json...
2025-12-03 16:52:16,980 - worker.extractor - INFO - Generated 28 trading pairs from configuration.
2025-12-03 16:52:16,981 - worker.extractor - INFO - Starting parallel extraction for 28 pairs...
2025-12-03 16:52:16,983 - worker.extractor - INFO - Extracting ARS/USDT/BUY
2025-12-03 16:52:16,984 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:16,984 - worker.extractor - INFO - Extracting ARS/USDT/SELL
2025-12-03 16:52:16,988 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:16,988 - worker.extractor - INFO - Extracting ARS/BTC/BUY
2025-12-03 16:52:16,995 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:16,995 - worker.extractor - INFO - Extracting ARS/BTC/SELL
2025-12-03 16:52:17,011 - worker.extractor - INFO - Extracting ARS/ETH/BUY
2025-12-03 16:52:17,014 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:17,020 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:17,021 - worker.extractor - INFO - Extracting ARS/ETH/SELL
2025-12-03 16:52:17,025 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:17,024 - worker.extractor - INFO - Extracting ARS/BNB/BUY
2025-12-03 16:52:17,038 - worker.extractor - INFO - Extracting ARS/BNB/SELL
2025-12-03 16:52:17,040 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:17,045 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:17,050 - worker.extractor - INFO - Extracting COP/USDT/BUY
2025-12-03 16:52:17,063 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:17,070 - worker.extractor - INFO - Extracting COP/USDT/SELL
2025-12-03 16:52:17,079 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:17,084 - worker.extractor - INFO - Extracting COP/BTC/BUY
2025-12-03 16:52:17,084 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:17,085 - worker.extractor - INFO - Extracting COP/BTC/SELL
2025-12-03 16:52:17,086 - worker.extractor - INFO - Extracting COP/ETH/BUY
2025-12-03 16:52:17,087 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:17,088 - worker.extractor - INFO - Extracting COP/ETH/SELL
2025-12-03 16:52:17,089 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:17,089 - worker.extractor - INFO - Extracting VES/USDT/BUY
2025-12-03 16:52:17,129 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:17,112 - worker.extractor - INFO - Extracting VES/USDT/SELL
2025-12-03 16:52:17,109 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:17,143 - worker.extractor - INFO - Extracting VES/BTC/BUY
2025-12-03 16:52:17,144 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:17,157 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:17,162 - worker.extractor - INFO - Extracting VES/BTC/SELL
2025-12-03 16:52:17,211 - worker.extractor - INFO - Extracting USD/USDT/BUY
2025-12-03 16:52:17,223 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:17,228 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:17,241 - worker.extractor - INFO - Extracting USD/USDT/SELL
2025-12-03 16:52:17,684 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:25,765 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:25,779 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:25,809 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:25,831 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:25,881 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:25,882 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:25,891 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:25,892 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:25,958 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:26,026 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:26,072 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:26,104 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:26,112 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:26,129 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:26,139 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:52:26,181 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:52:26,278 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:26,394 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:52:26,394 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:52:26,399 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:26,408 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:52:26,462 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:26,522 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:26,535 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:26,541 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:26,560 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:26,578 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:26,595 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:26,606 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:26,616 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:26,632 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:26,636 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:26,653 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:26,679 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:26,689 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:26,708 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:26,716 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:26,721 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:26,722 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:26,746 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:26,802 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:26,824 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:26,825 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:26,939 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:26,958 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:27,009 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:27,009 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:27,023 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:27,023 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:27,034 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:27,036 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:52:27,037 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:52:27,039 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:52:27,055 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:27,062 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:27,069 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:27,205 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:27,374 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:27,468 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:52:27,470 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:27,494 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:52:27,503 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:27,810 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:28,132 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:28,411 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:28,763 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:28,795 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:52:28,801 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:28,969 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 16:52:28,970 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:29,012 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:29,304 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:29,612 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:29,889 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:30,213 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:30,504 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:30,813 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:31,172 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:31,414 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:31,725 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:32,014 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:32,297 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:32,615 - worker.rate_limiter - WARNING - Rate limiter active: 10 waits, 46 total requests
2025-12-03 16:52:32,615 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:33,094 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:33,216 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:33,506 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:33,816 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:34,110 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:34,417 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:34,705 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:35,018 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:35,342 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:35,619 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:35,948 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:36,220 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:36,543 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:36,821 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:37,105 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:37,434 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:37,783 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:38,035 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:38,371 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:38,635 - worker.rate_limiter - WARNING - Rate limiter active: 20 waits, 56 total requests
2025-12-03 16:52:38,636 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:38,918 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:39,236 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:39,550 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:39,836 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:40,128 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:40,437 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:40,729 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:41,038 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:41,639 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:41,746 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:41,988 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:42,239 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:42,549 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:42,839 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:43,156 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:43,444 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:43,790 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:44,046 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:44,358 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:44,645 - worker.rate_limiter - WARNING - Rate limiter active: 30 waits, 66 total requests
2025-12-03 16:52:44,646 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:44,944 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:45,246 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:45,550 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:45,847 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:46,240 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:46,448 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:46,770 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:47,054 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:47,376 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:47,655 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:48,256 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:48,553 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:48,553 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:48,554 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BTC/BUY
2025-12-03 16:52:48,555 - worker.extractor - INFO - Extracted 26 offers for ARS/BTC/BUY
2025-12-03 16:52:48,555 - worker.extractor - INFO - Extracting USD/BTC/BUY
2025-12-03 16:52:48,858 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:49,162 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:49,460 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:49,802 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:50,060 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:50,329 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:50,330 - worker.extractor - INFO - No offers found for COP/ETH/BUY
2025-12-03 16:52:50,330 - worker.extractor - INFO - Extracted 14 offers for COP/ETH/BUY
2025-12-03 16:52:50,331 - worker.extractor - INFO - Extracting USD/BTC/SELL
2025-12-03 16:52:50,661 - worker.rate_limiter - WARNING - Rate limiter active: 40 waits, 76 total requests
2025-12-03 16:52:50,662 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:50,979 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:51,262 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:51,612 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:51,863 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:52,211 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:52,463 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:52,842 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:53,063 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:53,392 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:53,393 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDT/BUY
2025-12-03 16:52:53,394 - worker.extractor - INFO - Extracted 26 offers for USD/USDT/BUY
2025-12-03 16:52:53,394 - worker.extractor - INFO - Extracting USD/ETH/BUY
2025-12-03 16:52:53,664 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:53,941 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:53,942 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/ETH/SELL
2025-12-03 16:52:53,943 - worker.extractor - INFO - Extracted 25 offers for ARS/ETH/SELL
2025-12-03 16:52:53,944 - worker.extractor - INFO - Extracting USD/ETH/SELL
2025-12-03 16:52:54,265 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:54,599 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:54,866 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:55,163 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:55,168 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/BTC/BUY
2025-12-03 16:52:55,169 - worker.extractor - INFO - Extracted 23 offers for VES/BTC/BUY
2025-12-03 16:52:55,172 - worker.extractor - INFO - Extracting USD/BNB/BUY
2025-12-03 16:52:55,466 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:55,757 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:55,759 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/USDT/SELL
2025-12-03 16:52:55,760 - worker.extractor - INFO - Extracted 26 offers for VES/USDT/SELL
2025-12-03 16:52:55,760 - worker.extractor - INFO - Extracting USD/BNB/SELL
2025-12-03 16:52:56,067 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:56,349 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:56,350 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/BTC/BUY
2025-12-03 16:52:56,351 - worker.extractor - INFO - Extracted 25 offers for COP/BTC/BUY
2025-12-03 16:52:56,351 - worker.extractor - INFO - Extracting USD/USDC/BUY
2025-12-03 16:52:56,667 - worker.rate_limiter - WARNING - Rate limiter active: 50 waits, 86 total requests
2025-12-03 16:52:56,668 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:56,949 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:56,950 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/BTC/SELL
2025-12-03 16:52:56,951 - worker.extractor - INFO - Extracted 26 offers for VES/BTC/SELL
2025-12-03 16:52:56,951 - worker.extractor - INFO - Extracting USD/USDC/SELL
2025-12-03 16:52:57,268 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:57,538 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:57,539 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDT/SELL
2025-12-03 16:52:57,540 - worker.extractor - INFO - Extracted 26 offers for USD/USDT/SELL
2025-12-03 16:52:57,868 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:58,164 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:58,165 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/USDT/BUY
2025-12-03 16:52:58,166 - worker.extractor - INFO - Extracted 26 offers for COP/USDT/BUY
2025-12-03 16:52:58,469 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:58,765 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:58,769 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/USDT/SELL
2025-12-03 16:52:58,771 - worker.extractor - INFO - Extracted 26 offers for COP/USDT/SELL
2025-12-03 16:52:59,070 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:52:59,513 - worker.extractor - INFO - Response status: 200
2025-12-03 16:52:59,515 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/ETH/SELL
2025-12-03 16:52:59,520 - worker.extractor - INFO - Extracted 25 offers for COP/ETH/SELL
2025-12-03 16:52:59,670 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:00,033 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:00,059 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/BTC/SELL
2025-12-03 16:53:00,064 - worker.extractor - INFO - Extracted 26 offers for COP/BTC/SELL
2025-12-03 16:53:00,271 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:00,608 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:00,872 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:01,144 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:01,147 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BNB/SELL
2025-12-03 16:53:01,148 - worker.extractor - INFO - Extracted 25 offers for ARS/BNB/SELL
2025-12-03 16:53:01,473 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:01,767 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:02,073 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:02,337 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:02,674 - worker.rate_limiter - WARNING - Rate limiter active: 60 waits, 96 total requests
2025-12-03 16:53:02,675 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:02,998 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:02,999 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/USDT/BUY
2025-12-03 16:53:03,000 - worker.extractor - INFO - Extracted 26 offers for VES/USDT/BUY
2025-12-03 16:53:03,274 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:03,639 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:03,640 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/USDT/SELL
2025-12-03 16:53:03,641 - worker.extractor - INFO - Extracted 26 offers for ARS/USDT/SELL
2025-12-03 16:53:03,875 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:04,190 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:04,190 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/ETH/BUY
2025-12-03 16:53:04,191 - worker.extractor - INFO - Extracted 22 offers for ARS/ETH/BUY
2025-12-03 16:53:04,476 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:04,758 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:04,760 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BTC/SELL
2025-12-03 16:53:04,760 - worker.extractor - INFO - Extracted 26 offers for ARS/BTC/SELL
2025-12-03 16:53:05,077 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:05,364 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:05,678 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:06,027 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:06,284 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:06,742 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:06,755 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BNB/BUY
2025-12-03 16:53:06,760 - worker.extractor - INFO - Extracted 21 offers for ARS/BNB/BUY
2025-12-03 16:53:06,924 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:07,315 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:07,519 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:07,788 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:08,119 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:08,430 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:08,721 - worker.rate_limiter - WARNING - Rate limiter active: 70 waits, 106 total requests
2025-12-03 16:53:08,723 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:09,130 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:09,321 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:09,616 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:09,923 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:10,212 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:10,213 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/USDT/BUY
2025-12-03 16:53:10,213 - worker.extractor - INFO - Extracted 26 offers for ARS/USDT/BUY
2025-12-03 16:53:10,524 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:10,794 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:11,129 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:11,418 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:11,729 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:12,025 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:12,330 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:12,668 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:12,930 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:13,307 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:13,530 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:13,859 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:14,131 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:14,517 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:14,731 - worker.rate_limiter - WARNING - Rate limiter active: 80 waits, 116 total requests
2025-12-03 16:53:14,731 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:15,028 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:15,332 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:15,624 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:15,936 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:16,263 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:16,537 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:16,889 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:17,137 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:17,468 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:17,738 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:18,018 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:18,338 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:18,646 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:18,938 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:19,210 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:19,539 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:19,819 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:20,139 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:20,541 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:20,740 - worker.rate_limiter - WARNING - Rate limiter active: 90 waits, 126 total requests
2025-12-03 16:53:20,741 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:21,032 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:21,341 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:21,618 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:21,941 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:22,213 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:22,541 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:22,940 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:23,142 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:23,434 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:23,743 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:24,045 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:24,343 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:24,631 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:24,633 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BTC/BUY
2025-12-03 16:53:24,638 - worker.extractor - INFO - Extracted 25 offers for USD/BTC/BUY
2025-12-03 16:53:24,944 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:25,242 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:25,243 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BTC/SELL
2025-12-03 16:53:25,244 - worker.extractor - INFO - Extracted 25 offers for USD/BTC/SELL
2025-12-03 16:53:25,544 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:25,816 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:25,817 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/ETH/BUY
2025-12-03 16:53:25,818 - worker.extractor - INFO - Extracted 25 offers for USD/ETH/BUY
2025-12-03 16:53:26,145 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:26,481 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:26,482 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/ETH/SELL
2025-12-03 16:53:26,482 - worker.extractor - INFO - Extracted 25 offers for USD/ETH/SELL
2025-12-03 16:53:26,745 - worker.rate_limiter - WARNING - Rate limiter active: 100 waits, 136 total requests
2025-12-03 16:53:26,746 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:27,003 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:27,004 - worker.extractor - INFO - No offers found for USD/BNB/BUY
2025-12-03 16:53:27,004 - worker.extractor - INFO - Extracted 20 offers for USD/BNB/BUY
2025-12-03 16:53:27,346 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:27,626 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:27,627 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BNB/SELL
2025-12-03 16:53:27,628 - worker.extractor - INFO - Extracted 25 offers for USD/BNB/SELL
2025-12-03 16:53:27,947 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:28,223 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:28,224 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDC/BUY
2025-12-03 16:53:28,225 - worker.extractor - INFO - Extracted 25 offers for USD/USDC/BUY
2025-12-03 16:53:28,548 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 16:53:28,817 - worker.extractor - INFO - Response status: 200
2025-12-03 16:53:28,818 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDC/SELL
2025-12-03 16:53:28,819 - worker.extractor - INFO - Extracted 25 offers for USD/USDC/SELL
2025-12-03 16:53:28,822 - worker.extractor - INFO - Total offers extracted: 687
2025-12-03 16:53:28,823 - worker.loader - INFO - Starting to load 687 offers for batch 093a784b-d55f-4775-8254-b19eda308b26...
2025-12-03 16:56:50,333 - worker.loader - ERROR - Error loading offers for batch 093a784b-d55f-4775-8254-b19eda308b26: 'completion_rate'
Traceback (most recent call last):
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 51, in load_offers
    self._load_facts(session, offers, batch_id)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 179, in _load_facts
    completion_rate=offer['advertiser']['completion_rate'],
                    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
KeyError: 'completion_rate'
2025-12-03 16:56:50,527 - worker.db - ERROR - Database session error: 'completion_rate'
2025-12-03 16:56:50,527 - __main__ - ERROR - An error occurred during the job: 'completion_rate'
Traceback (most recent call last):
  File "C:\Users\DELL\Desktop\dashboards\worker\main.py", line 31, in job
    loader.load_offers(offers, batch_id)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 51, in load_offers
    self._load_facts(session, offers, batch_id)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 179, in _load_facts
    completion_rate=offer['advertiser']['completion_rate'],
                    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
KeyError: 'completion_rate'

# sixteenth run

(.venv) PS C:\Users\DELL\Desktop\dashboards> python -m worker.main
2025-12-03 17:27:30,382 - __main__ - INFO - Worker starting. Job will run every 10 minutes.
2025-12-03 17:27:30,383 - __main__ - INFO - Starting P2P data extraction job...
2025-12-03 17:27:30,384 - worker.extractor - INFO - Fetching all trading pairs...
2025-12-03 17:27:30,385 - worker.extractor - INFO - Generating trading pairs from p2p_config.json...
2025-12-03 17:27:30,389 - worker.extractor - INFO - Generated 28 trading pairs from configuration.
2025-12-03 17:27:30,390 - worker.extractor - INFO - Starting parallel extraction for 28 pairs...
2025-12-03 17:27:30,398 - worker.extractor - INFO - Extracting ARS/USDT/BUY
2025-12-03 17:27:30,402 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:30,404 - worker.extractor - INFO - Extracting ARS/USDT/SELL
2025-12-03 17:27:30,435 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:30,453 - worker.extractor - INFO - Extracting ARS/BTC/BUY
2025-12-03 17:27:30,468 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:30,512 - worker.extractor - INFO - Extracting ARS/BTC/SELL
2025-12-03 17:27:30,613 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:30,615 - worker.extractor - INFO - Extracting ARS/ETH/BUY
2025-12-03 17:27:30,639 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:30,645 - worker.extractor - INFO - Extracting ARS/ETH/SELL
2025-12-03 17:27:30,653 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:30,775 - worker.extractor - INFO - Extracting ARS/BNB/BUY
2025-12-03 17:27:30,895 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:30,936 - worker.extractor - INFO - Extracting ARS/BNB/SELL
2025-12-03 17:27:31,093 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:31,093 - worker.extractor - INFO - Extracting COP/USDT/BUY
2025-12-03 17:27:31,222 - worker.extractor - INFO - Extracting COP/USDT/SELL
2025-12-03 17:27:31,230 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:31,364 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:31,365 - worker.extractor - INFO - Extracting COP/BTC/BUY
2025-12-03 17:27:31,619 - worker.extractor - INFO - Extracting COP/BTC/SELL
2025-12-03 17:27:31,728 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:31,875 - worker.extractor - INFO - Extracting COP/ETH/BUY
2025-12-03 17:27:31,878 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:32,055 - worker.extractor - INFO - Extracting COP/ETH/SELL
2025-12-03 17:27:32,065 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:32,209 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:32,210 - worker.extractor - INFO - Extracting VES/USDT/BUY
2025-12-03 17:27:32,546 - worker.extractor - INFO - Extracting VES/USDT/SELL
2025-12-03 17:27:32,651 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:32,668 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:32,684 - worker.extractor - INFO - Extracting VES/BTC/BUY
2025-12-03 17:27:32,957 - worker.extractor - INFO - Extracting VES/BTC/SELL
2025-12-03 17:27:33,292 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:33,292 - worker.extractor - INFO - Extracting USD/USDT/BUY
2025-12-03 17:27:33,674 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:33,910 - worker.extractor - INFO - Extracting USD/USDT/SELL
2025-12-03 17:27:34,103 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:34,528 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:38,899 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:39,111 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:39,490 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:39,502 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:39,949 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:39,959 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:40,062 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:40,062 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:40,208 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:40,282 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:40,519 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:40,723 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:40,908 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:40,998 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:41,183 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:41,305 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:41,426 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:41,700 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:41,724 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:41,792 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:42,127 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:42,160 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:42,345 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:42,357 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:42,411 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:42,415 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:27:42,527 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:42,531 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:42,731 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:42,744 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:42,790 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:42,831 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:42,836 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:42,843 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:42,931 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:42,982 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:42,983 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:42,990 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:43,015 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:27:43,440 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:43,126 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:43,150 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:43,151 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:43,153 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:27:43,208 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:43,328 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:43,344 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:43,347 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:43,367 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:43,367 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:43,029 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:27:43,517 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:43,573 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:43,599 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:43,601 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:43,618 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:43,641 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:43,664 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:43,702 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:43,712 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:43,826 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:43,868 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:43,909 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:27:43,913 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:43,931 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:27:43,931 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:27:43,934 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:43,936 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:43,984 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:27:43,986 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:44,001 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:27:44,004 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:44,045 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:27:44,047 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:44,219 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:44,492 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:44,822 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:45,130 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:45,425 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:45,725 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:46,055 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:46,400 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:46,658 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:46,984 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:47,259 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:47,553 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:47,859 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:48,140 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:48,459 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:48,818 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:48,819 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/ETH/BUY
2025-12-03 17:27:48,821 - worker.extractor - INFO - Extracted 23 offers for ARS/ETH/BUY
2025-12-03 17:27:48,823 - worker.extractor - INFO - Extracting USD/BTC/BUY
2025-12-03 17:27:49,059 - worker.rate_limiter - WARNING - Rate limiter active: 10 waits, 51 total requests
2025-12-03 17:27:49,060 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:49,333 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:49,660 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:49,948 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:50,260 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:50,547 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:50,861 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:51,124 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:51,462 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:51,839 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:52,062 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:52,480 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:52,663 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:52,934 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:53,264 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:53,538 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:53,864 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:54,140 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:54,465 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:54,732 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:55,066 - worker.rate_limiter - WARNING - Rate limiter active: 20 waits, 61 total requests
2025-12-03 17:27:55,068 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:55,394 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:55,666 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:56,087 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:56,267 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:56,541 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:56,867 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:57,164 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:57,165 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/ETH/SELL
2025-12-03 17:27:57,165 - worker.extractor - INFO - Extracted 25 offers for ARS/ETH/SELL
2025-12-03 17:27:57,166 - worker.extractor - INFO - Extracting USD/BTC/SELL
2025-12-03 17:27:57,468 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:57,765 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:57,768 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BTC/BUY
2025-12-03 17:27:57,769 - worker.extractor - INFO - Extracted 26 offers for ARS/BTC/BUY
2025-12-03 17:27:57,769 - worker.extractor - INFO - Extracting USD/ETH/BUY
2025-12-03 17:27:58,073 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:58,388 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:58,670 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:58,955 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:58,957 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BTC/SELL
2025-12-03 17:27:58,957 - worker.extractor - INFO - Extracted 26 offers for ARS/BTC/SELL
2025-12-03 17:27:58,959 - worker.extractor - INFO - Extracting USD/ETH/SELL
2025-12-03 17:27:59,271 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:27:59,549 - worker.extractor - INFO - Response status: 200
2025-12-03 17:27:59,871 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:00,145 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:00,478 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:00,870 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:01,076 - worker.rate_limiter - WARNING - Rate limiter active: 30 waits, 71 total requests
2025-12-03 17:28:01,076 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:01,686 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:01,837 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:02,110 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:02,286 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:02,569 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:02,891 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:03,177 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:03,189 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/USDT/BUY
2025-12-03 17:28:03,201 - worker.extractor - INFO - Extracted 26 offers for ARS/USDT/BUY
2025-12-03 17:28:03,204 - worker.extractor - INFO - Extracting USD/BNB/BUY
2025-12-03 17:28:03,514 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:03,879 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:04,115 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:04,391 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:04,392 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BNB/BUY
2025-12-03 17:28:04,392 - worker.extractor - INFO - Extracted 21 offers for ARS/BNB/BUY
2025-12-03 17:28:04,393 - worker.extractor - INFO - Extracting USD/BNB/SELL
2025-12-03 17:28:04,716 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:04,998 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:05,353 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:05,758 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:05,962 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:06,258 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:06,562 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:06,832 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:06,833 - worker.extractor - INFO - No offers found for COP/ETH/BUY
2025-12-03 17:28:06,834 - worker.extractor - INFO - Extracted 14 offers for COP/ETH/BUY
2025-12-03 17:28:06,835 - worker.extractor - INFO - Extracting USD/USDC/BUY
2025-12-03 17:28:07,163 - worker.rate_limiter - WARNING - Rate limiter active: 40 waits, 81 total requests
2025-12-03 17:28:07,163 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:07,444 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:07,445 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/USDT/SELL
2025-12-03 17:28:07,445 - worker.extractor - INFO - Extracted 26 offers for ARS/USDT/SELL
2025-12-03 17:28:07,446 - worker.extractor - INFO - Extracting USD/USDC/SELL
2025-12-03 17:28:07,763 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:08,034 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:08,364 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:08,636 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:08,639 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BNB/SELL
2025-12-03 17:28:08,643 - worker.extractor - INFO - Extracted 25 offers for ARS/BNB/SELL
2025-12-03 17:28:08,965 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:09,252 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:09,579 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:09,914 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:10,185 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:10,456 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:10,457 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/USDT/SELL
2025-12-03 17:28:10,459 - worker.extractor - INFO - Extracted 26 offers for COP/USDT/SELL
2025-12-03 17:28:10,786 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:11,097 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:11,395 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:11,712 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:11,996 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:12,278 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:12,282 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/USDT/BUY
2025-12-03 17:28:12,283 - worker.extractor - INFO - Extracted 26 offers for COP/USDT/BUY
2025-12-03 17:28:12,597 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:12,885 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:13,198 - worker.rate_limiter - WARNING - Rate limiter active: 50 waits, 91 total requests
2025-12-03 17:28:13,199 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:13,489 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:13,798 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:14,089 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:14,399 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:14,669 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:14,670 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/BTC/SELL
2025-12-03 17:28:14,670 - worker.extractor - INFO - Extracted 26 offers for COP/BTC/SELL
2025-12-03 17:28:14,999 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:15,289 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:15,604 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:15,886 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:16,205 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:16,469 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:16,805 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:17,120 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:17,121 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/ETH/SELL
2025-12-03 17:28:17,121 - worker.extractor - INFO - Extracted 25 offers for COP/ETH/SELL
2025-12-03 17:28:17,406 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:17,702 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:18,007 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:18,284 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:18,286 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/BTC/BUY
2025-12-03 17:28:18,287 - worker.extractor - INFO - Extracted 25 offers for COP/BTC/BUY
2025-12-03 17:28:18,607 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:18,913 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:19,208 - worker.rate_limiter - WARNING - Rate limiter active: 60 waits, 101 total requests
2025-12-03 17:28:19,208 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:19,490 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:19,808 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:20,094 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:20,408 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:20,780 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:21,009 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:21,308 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:21,609 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:21,893 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:22,210 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:22,501 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:22,505 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/USDT/SELL
2025-12-03 17:28:22,510 - worker.extractor - INFO - Extracted 26 offers for VES/USDT/SELL
2025-12-03 17:28:22,811 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:23,104 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:23,411 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:23,696 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:23,700 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/BTC/BUY
2025-12-03 17:28:23,702 - worker.extractor - INFO - Extracted 22 offers for VES/BTC/BUY
2025-12-03 17:28:24,011 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:24,299 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:24,300 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/USDT/BUY
2025-12-03 17:28:24,300 - worker.extractor - INFO - Extracted 26 offers for VES/USDT/BUY
2025-12-03 17:28:24,613 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:24,889 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:25,213 - worker.rate_limiter - WARNING - Rate limiter active: 70 waits, 111 total requests
2025-12-03 17:28:25,214 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:25,629 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:25,633 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/BTC/SELL
2025-12-03 17:28:25,638 - worker.extractor - INFO - Extracted 26 offers for VES/BTC/SELL
2025-12-03 17:28:25,814 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:26,094 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:26,415 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:26,693 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:26,694 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDT/SELL
2025-12-03 17:28:26,695 - worker.extractor - INFO - Extracted 26 offers for USD/USDT/SELL
2025-12-03 17:28:27,018 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:27,292 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:27,619 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:27,921 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:28,219 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:28,502 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:28,503 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDT/BUY
2025-12-03 17:28:28,504 - worker.extractor - INFO - Extracted 26 offers for USD/USDT/BUY
2025-12-03 17:28:28,820 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:29,092 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:29,421 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:29,697 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:30,022 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:30,300 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:30,622 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:31,222 - worker.rate_limiter - WARNING - Rate limiter active: 80 waits, 121 total requests
2025-12-03 17:28:31,222 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:31,382 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:31,488 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:31,822 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:32,096 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:32,423 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:32,750 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:33,026 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:33,313 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:33,626 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:33,911 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:34,226 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:34,514 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:34,826 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:35,138 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:35,427 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:35,708 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:35,709 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BTC/BUY
2025-12-03 17:28:35,710 - worker.extractor - INFO - Extracted 25 offers for USD/BTC/BUY
2025-12-03 17:28:36,028 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:36,312 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:36,628 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:36,914 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:37,228 - worker.rate_limiter - WARNING - Rate limiter active: 90 waits, 131 total requests
2025-12-03 17:28:37,229 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:37,532 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:37,830 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:38,165 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:38,433 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:38,767 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:38,774 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BTC/SELL
2025-12-03 17:28:38,778 - worker.extractor - INFO - Extracted 25 offers for USD/BTC/SELL
2025-12-03 17:28:39,033 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:39,338 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:39,340 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/ETH/BUY
2025-12-03 17:28:39,341 - worker.extractor - INFO - Extracted 25 offers for USD/ETH/BUY
2025-12-03 17:28:39,634 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:39,907 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:39,909 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/ETH/SELL
2025-12-03 17:28:39,909 - worker.extractor - INFO - Extracted 25 offers for USD/ETH/SELL
2025-12-03 17:28:40,234 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:40,508 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:40,509 - worker.extractor - INFO - No offers found for USD/BNB/BUY
2025-12-03 17:28:40,510 - worker.extractor - INFO - Extracted 19 offers for USD/BNB/BUY
2025-12-03 17:28:40,835 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:41,157 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:41,164 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BNB/SELL
2025-12-03 17:28:41,168 - worker.extractor - INFO - Extracted 25 offers for USD/BNB/SELL
2025-12-03 17:28:41,442 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:41,741 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:41,743 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDC/BUY
2025-12-03 17:28:41,743 - worker.extractor - INFO - Extracted 25 offers for USD/USDC/BUY
2025-12-03 17:28:42,042 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:28:42,748 - worker.extractor - INFO - Response status: 200
2025-12-03 17:28:42,749 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDC/SELL
2025-12-03 17:28:42,750 - worker.extractor - INFO - Extracted 25 offers for USD/USDC/SELL
2025-12-03 17:28:42,753 - worker.extractor - INFO - Total offers extracted: 686
2025-12-03 17:28:42,754 - worker.loader - INFO - Starting to load 686 offers for batch 985c320f-d1a5-445e-95f8-74db13f65d78...
2025-12-03 17:31:41,743 - worker.loader - ERROR - Error loading offers for batch 985c320f-d1a5-445e-95f8-74db13f65d78: 'completion_rate'
Traceback (most recent call last):
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 51, in load_offers
    self._load_facts(session, offers, batch_id)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 179, in _load_facts
    completion_rate=offer['advertiser']['completion_rate'],
                    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
KeyError: 'completion_rate'
2025-12-03 17:31:41,946 - worker.db - ERROR - Database session error: 'completion_rate'
2025-12-03 17:31:41,947 - __main__ - ERROR - An error occurred during the job: 'completion_rate'
Traceback (most recent call last):
  File "C:\Users\DELL\Desktop\dashboards\worker\main.py", line 31, in job
    loader.load_offers(offers, batch_id)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 51, in load_offers
    self._load_facts(session, offers, batch_id)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Desktop\dashboards\worker\loader.py", line 179, in _load_facts
    completion_rate=offer['advertiser']['completion_rate'],
                    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
KeyError: 'completion_rate'

# seventeenth

dly/c2c/adv/search
2025-12-03 17:36:46,362 - worker.extractor - INFO - Extracting VES/BTC/SELL
2025-12-03 17:36:46,373 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:36:46,391 - worker.extractor - INFO - Extracting USD/USDT/BUY
2025-12-03 17:36:46,411 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:36:46,412 - worker.extractor - INFO - Extracting USD/USDT/SELL
2025-12-03 17:36:46,439 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:36:57,121 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:57,234 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:36:57,590 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:57,603 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:57,606 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:36:57,622 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:36:57,691 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:57,710 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:36:57,803 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:57,811 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:36:57,827 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:57,843 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:36:57,874 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:57,879 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:57,890 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:36:57,912 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:36:58,135 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,136 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,140 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,140 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,142 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,144 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:36:58,144 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,145 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,145 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,147 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:36:58,150 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:36:58,152 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:36:58,159 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:36:58,162 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:36:58,172 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:36:58,175 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:36:58,227 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,227 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,227 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,237 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:36:58,242 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:36:58,245 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:36:58,259 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,276 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:36:58,287 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,287 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,306 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,339 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,341 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,530 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,533 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,533 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,629 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,631 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:36:58,632 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,632 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:36:58,640 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,652 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,660 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:36:58,670 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:36:58,670 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:36:58,673 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,677 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:36:58,704 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,686 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:36:58,686 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:36:58,689 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,697 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,680 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:36:58,710 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,712 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,730 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:58,959 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:36:58,960 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:59,003 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:36:59,261 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:36:59,323 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:59,560 - worker.extractor - INFO - Response status: 200
2025-12-03 17:36:59,874 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:00,249 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:00,474 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:00,793 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:01,085 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:01,465 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:01,687 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:01,957 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:02,288 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:02,570 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:02,888 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:03,209 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:03,489 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:03,809 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:04,089 - worker.rate_limiter - WARNING - Rate limiter active: 10 waits, 50 total requests
2025-12-03 17:37:04,090 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:04,382 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:04,690 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:05,002 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:05,291 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:05,644 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:05,891 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:06,251 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:06,494 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:07,094 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:07,340 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:07,385 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:07,695 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:08,089 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:08,298 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:08,606 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:08,898 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:09,228 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:09,520 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:09,891 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:10,120 - worker.rate_limiter - WARNING - Rate limiter active: 20 waits, 60 total requests
2025-12-03 17:37:10,123 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:10,585 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:10,739 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:11,153 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:11,342 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:11,914 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:11,942 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:12,543 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:12,605 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:12,916 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:13,144 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:13,502 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:13,506 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BTC/BUY
2025-12-03 17:37:13,507 - worker.extractor - INFO - Extracted 26 offers for ARS/BTC/BUY
2025-12-03 17:37:13,508 - worker.extractor - INFO - Extracting USD/BTC/BUY
2025-12-03 17:37:13,744 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:14,358 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:14,660 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:14,958 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:15,024 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:15,239 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:15,241 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/USDT/BUY
2025-12-03 17:37:15,241 - worker.extractor - INFO - Extracted 26 offers for ARS/USDT/BUY
2025-12-03 17:37:15,242 - worker.extractor - INFO - Extracting USD/BTC/SELL
2025-12-03 17:37:15,563 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:15,859 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:16,163 - worker.rate_limiter - WARNING - Rate limiter active: 30 waits, 70 total requests
2025-12-03 17:37:16,164 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:16,683 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:16,685 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BTC/SELL
2025-12-03 17:37:16,686 - worker.extractor - INFO - Extracted 26 offers for ARS/BTC/SELL
2025-12-03 17:37:16,686 - worker.extractor - INFO - Extracting USD/ETH/BUY
2025-12-03 17:37:16,764 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:17,202 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:17,364 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:17,879 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:17,966 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:18,303 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:18,567 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:18,999 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:19,168 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:19,623 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:19,768 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:20,101 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:20,371 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:20,804 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:20,971 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:21,381 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:21,382 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDT/SELL
2025-12-03 17:37:21,383 - worker.extractor - INFO - Extracted 26 offers for USD/USDT/SELL
2025-12-03 17:37:21,384 - worker.extractor - INFO - Extracting USD/ETH/SELL
2025-12-03 17:37:21,576 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:21,892 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:22,179 - worker.rate_limiter - WARNING - Rate limiter active: 40 waits, 80 total requests
2025-12-03 17:37:22,181 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:22,685 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:22,798 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:23,428 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:24,061 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:24,069 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:24,346 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:24,680 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:24,740 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:24,780 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/BTC/BUY
2025-12-03 17:37:24,802 - worker.extractor - INFO - Extracted 25 offers for COP/BTC/BUY
2025-12-03 17:37:24,821 - worker.extractor - INFO - Extracting USD/BNB/BUY
2025-12-03 17:37:25,011 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:25,092 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/USDT/BUY
2025-12-03 17:37:25,095 - worker.extractor - INFO - Extracted 26 offers for COP/USDT/BUY
2025-12-03 17:37:25,096 - worker.extractor - INFO - Extracting USD/BNB/SELL
2025-12-03 17:37:25,418 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:25,911 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:26,068 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:26,449 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:26,517 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/USDT/BUY
2025-12-03 17:37:26,518 - worker.extractor - INFO - Extracted 26 offers for VES/USDT/BUY
2025-12-03 17:37:26,519 - worker.extractor - INFO - Extracting USD/USDC/BUY
2025-12-03 17:37:26,728 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:27,102 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:27,134 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/ETH/BUY
2025-12-03 17:37:27,187 - worker.extractor - INFO - Extracted 23 offers for ARS/ETH/BUY
2025-12-03 17:37:27,238 - worker.extractor - INFO - Extracting USD/USDC/SELL
2025-12-03 17:37:27,345 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:27,814 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:28,003 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:28,630 - worker.rate_limiter - WARNING - Rate limiter active: 50 waits, 90 total requests
2025-12-03 17:37:28,676 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:28,918 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:29,238 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:29,559 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:29,642 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:29,653 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BNB/SELL
2025-12-03 17:37:29,654 - worker.extractor - INFO - Extracted 25 offers for ARS/BNB/SELL
2025-12-03 17:37:29,845 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:30,280 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:30,281 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BNB/BUY
2025-12-03 17:37:30,281 - worker.extractor - INFO - Extracted 21 offers for ARS/BNB/BUY
2025-12-03 17:37:30,446 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:30,771 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:30,773 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/ETH/SELL
2025-12-03 17:37:30,775 - worker.extractor - INFO - Extracted 25 offers for ARS/ETH/SELL
2025-12-03 17:37:31,047 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:31,648 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:31,894 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:31,899 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDT/BUY
2025-12-03 17:37:31,901 - worker.extractor - INFO - Extracted 26 offers for USD/USDT/BUY
2025-12-03 17:37:32,284 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:32,451 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:32,483 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/BTC/SELL
2025-12-03 17:37:32,487 - worker.extractor - INFO - Extracted 26 offers for COP/BTC/SELL
2025-12-03 17:37:32,895 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:33,120 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:33,121 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/ETH/SELL
2025-12-03 17:37:33,122 - worker.extractor - INFO - Extracted 25 offers for COP/ETH/SELL
2025-12-03 17:37:33,366 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:33,368 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/BTC/SELL
2025-12-03 17:37:33,370 - worker.extractor - INFO - Extracted 26 offers for VES/BTC/SELL
2025-12-03 17:37:33,495 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:33,917 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:34,095 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:34,414 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:34,415 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/BTC/BUY
2025-12-03 17:37:34,415 - worker.extractor - INFO - Extracted 22 offers for VES/BTC/BUY
2025-12-03 17:37:34,696 - worker.rate_limiter - WARNING - Rate limiter active: 60 waits, 100 total requests
2025-12-03 17:37:34,699 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:35,297 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:35,369 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:35,370 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/USDT/SELL
2025-12-03 17:37:35,370 - worker.extractor - INFO - Extracted 26 offers for ARS/USDT/SELL
2025-12-03 17:37:35,898 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:36,020 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:36,023 - worker.extractor - INFO - No offers found for COP/ETH/BUY
2025-12-03 17:37:36,028 - worker.extractor - INFO - Extracted 14 offers for COP/ETH/BUY
2025-12-03 17:37:36,383 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:36,384 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/USDT/SELL
2025-12-03 17:37:36,384 - worker.extractor - INFO - Extracted 26 offers for COP/USDT/SELL
2025-12-03 17:37:36,498 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:36,830 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:37,098 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:37,670 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:37,709 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:38,031 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:38,320 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:38,724 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:38,920 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:39,218 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:39,521 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:39,895 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:40,122 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:40,449 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:40,450 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/USDT/SELL
2025-12-03 17:37:40,451 - worker.extractor - INFO - Extracted 26 offers for VES/USDT/SELL
2025-12-03 17:37:40,722 - worker.rate_limiter - WARNING - Rate limiter active: 70 waits, 110 total requests
2025-12-03 17:37:40,722 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:41,010 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:41,322 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:41,740 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:41,922 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:42,240 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:42,522 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:42,784 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:43,123 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:43,431 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:43,724 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:44,324 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:44,449 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:44,651 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:44,929 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:45,225 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:45,534 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:45,853 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:46,135 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:46,456 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:46,735 - worker.rate_limiter - WARNING - Rate limiter active: 80 waits, 120 total requests
2025-12-03 17:37:46,736 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:47,338 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:47,407 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:47,652 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:47,942 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:48,243 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:48,543 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:48,822 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:49,143 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:49,743 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:49,950 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:50,206 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:50,348 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:50,666 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:50,949 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:51,460 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:51,551 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:51,821 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:52,151 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:52,434 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:52,755 - worker.rate_limiter - WARNING - Rate limiter active: 90 waits, 130 total requests
2025-12-03 17:37:52,759 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:53,092 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:53,093 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BTC/BUY
2025-12-03 17:37:53,093 - worker.extractor - INFO - Extracted 25 offers for USD/BTC/BUY
2025-12-03 17:37:53,355 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:53,733 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:53,956 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:54,271 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:54,557 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:54,908 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:54,909 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BTC/SELL
2025-12-03 17:37:54,910 - worker.extractor - INFO - Extracted 25 offers for USD/BTC/SELL
2025-12-03 17:37:55,157 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:55,516 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:55,522 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/ETH/BUY
2025-12-03 17:37:55,525 - worker.extractor - INFO - Extracted 25 offers for USD/ETH/BUY
2025-12-03 17:37:55,762 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:56,072 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:56,074 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/ETH/SELL
2025-12-03 17:37:56,074 - worker.extractor - INFO - Extracted 25 offers for USD/ETH/SELL
2025-12-03 17:37:56,363 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:56,688 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:56,691 - worker.extractor - INFO - No offers found for USD/BNB/BUY
2025-12-03 17:37:56,692 - worker.extractor - INFO - Extracted 20 offers for USD/BNB/BUY
2025-12-03 17:37:56,964 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:57,320 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:57,321 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BNB/SELL
2025-12-03 17:37:57,322 - worker.extractor - INFO - Extracted 25 offers for USD/BNB/SELL
2025-12-03 17:37:57,564 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:58,165 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:37:58,472 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:58,476 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDC/BUY
2025-12-03 17:37:58,478 - worker.extractor - INFO - Extracted 25 offers for USD/USDC/BUY
2025-12-03 17:37:58,485 - worker.extractor - INFO - Response status: 200
2025-12-03 17:37:58,492 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDC/SELL
2025-12-03 17:37:58,508 - worker.extractor - INFO - Extracted 25 offers for USD/USDC/SELL
2025-12-03 17:37:58,517 - worker.extractor - INFO - Total offers extracted: 687
2025-12-03 17:37:58,520 - worker.loader - INFO - Starting to load 687 offers for batch 679b54dc-a71e-4d71-984d-8b2e5080ac8a...
2025-12-03 17:47:14,648 - worker.loader - INFO - Successfully loaded 687 offers for batch 679b54dc-a71e-4d71-984d-8b2e5080ac8a.
2025-12-03 17:47:15,052 - __main__ - INFO - P2P data extraction job finished successfully.
2025-12-03 17:57:15,997 - __main__ - INFO - Starting P2P data extraction job...
2025-12-03 17:57:16,018 - worker.extractor - INFO - Fetching all trading pairs...
2025-12-03 17:57:16,019 - worker.extractor - INFO - Generating trading pairs from p2p_config.json...
2025-12-03 17:57:16,038 - worker.extractor - INFO - Generated 28 trading pairs from configuration.
2025-12-03 17:57:16,039 - worker.extractor - INFO - Starting parallel extraction for 28 pairs...
2025-12-03 17:57:16,078 - worker.extractor - INFO - Extracting ARS/USDT/BUY
2025-12-03 17:57:16,085 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:16,102 - worker.extractor - INFO - Extracting ARS/USDT/SELL
2025-12-03 17:57:16,111 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:16,141 - worker.extractor - INFO - Extracting ARS/BTC/BUY
2025-12-03 17:57:16,149 - worker.extractor - INFO - Extracting ARS/BTC/SELL
2025-12-03 17:57:16,152 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:16,153 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:16,153 - worker.extractor - INFO - Extracting ARS/ETH/BUY
2025-12-03 17:57:16,155 - worker.extractor - INFO - Extracting ARS/ETH/SELL
2025-12-03 17:57:16,210 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:16,166 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:16,167 - worker.extractor - INFO - Extracting ARS/BNB/SELL
2025-12-03 17:57:16,163 - worker.extractor - INFO - Extracting ARS/BNB/BUY
2025-12-03 17:57:16,346 - worker.extractor - INFO - Extracting COP/USDT/BUY
2025-12-03 17:57:16,370 - worker.extractor - INFO - Extracting COP/USDT/SELL
2025-12-03 17:57:16,371 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:16,373 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:16,373 - worker.extractor - INFO - Extracting COP/BTC/BUY
2025-12-03 17:57:16,383 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:16,383 - worker.extractor - INFO - Extracting COP/BTC/SELL
2025-12-03 17:57:16,393 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:16,396 - worker.extractor - INFO - Extracting COP/ETH/BUY
2025-12-03 17:57:16,403 - worker.extractor - INFO - Extracting COP/ETH/SELL
2025-12-03 17:57:16,406 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:16,414 - worker.extractor - INFO - Extracting VES/USDT/BUY
2025-12-03 17:57:16,415 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:16,416 - worker.extractor - INFO - Extracting VES/USDT/SELL
2025-12-03 17:57:16,429 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:16,430 - worker.extractor - INFO - Extracting VES/BTC/BUY
2025-12-03 17:57:16,431 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:16,448 - worker.extractor - INFO - Extracting VES/BTC/SELL
2025-12-03 17:57:16,450 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:16,452 - worker.extractor - INFO - Extracting USD/USDT/BUY
2025-12-03 17:57:16,454 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:16,455 - worker.extractor - INFO - Extracting USD/USDT/SELL
2025-12-03 17:57:16,463 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:16,465 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:16,469 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:16,471 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:24,522 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:24,558 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:24,585 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:24,642 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:24,698 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:24,736 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:24,810 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:24,871 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:24,874 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:24,887 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:24,937 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:24,996 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,000 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:25,043 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,072 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:25,109 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:25,206 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:25,220 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:25,233 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:25,284 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:25,285 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,311 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,324 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:25,329 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:25,380 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,381 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,383 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,406 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:25,463 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:25,467 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,473 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:25,525 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,530 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,536 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,536 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,551 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,580 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,596 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,603 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,611 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,611 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:57:25,611 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:57:25,614 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:57:25,615 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:57:25,615 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,619 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,620 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,621 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,626 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:57:25,630 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,655 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:57:25,658 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,673 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:57:25,675 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,685 - worker.rate_limiter - WARNING - Rate limiter active: 100 waits, 175 total requests
2025-12-03 17:57:25,688 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:25,750 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,770 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:57:25,770 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:57:25,771 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,772 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:25,971 - urllib3.connectionpool - WARNING - Connection pool is full, discarding connection: p2p.binance.com. Connection pool size: 10
2025-12-03 17:57:25,972 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:26,285 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:26,560 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:26,886 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:27,161 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:27,486 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:27,772 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:28,086 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:28,369 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:28,686 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:28,956 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:29,287 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:29,563 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:29,888 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:30,149 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:30,488 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:31,089 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:31,135 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:31,366 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:31,689 - worker.rate_limiter - WARNING - Rate limiter active: 110 waits, 185 total requests
2025-12-03 17:57:31,690 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:31,971 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:32,290 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:32,560 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:32,891 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:33,167 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:33,492 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:33,761 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:34,092 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:34,377 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:34,692 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:34,967 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:35,293 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:35,569 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:35,893 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:36,494 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:36,516 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:36,786 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:37,100 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:37,411 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:37,700 - worker.rate_limiter - WARNING - Rate limiter active: 120 waits, 195 total requests
2025-12-03 17:57:37,701 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:37,982 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:38,302 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:38,570 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:38,571 - worker.extractor - INFO - No offers found for COP/ETH/BUY
2025-12-03 17:57:38,571 - worker.extractor - INFO - Extracted 14 offers for COP/ETH/BUY
2025-12-03 17:57:38,573 - worker.extractor - INFO - Extracting USD/BTC/BUY
2025-12-03 17:57:38,921 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:39,209 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:39,521 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:39,794 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:40,122 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:40,393 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:40,723 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:41,014 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:41,324 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:41,613 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:41,924 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:42,219 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:42,524 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:42,814 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:43,125 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:43,420 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:43,725 - worker.rate_limiter - WARNING - Rate limiter active: 130 waits, 205 total requests
2025-12-03 17:57:43,726 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:44,009 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:44,326 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:44,613 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:44,926 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:45,209 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:45,210 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BTC/SELL
2025-12-03 17:57:45,211 - worker.extractor - INFO - Extracted 26 offers for ARS/BTC/SELL
2025-12-03 17:57:45,211 - worker.extractor - INFO - Extracting USD/BTC/SELL
2025-12-03 17:57:45,526 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:45,799 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:46,126 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:46,391 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:46,728 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:47,000 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:47,329 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:47,610 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:47,930 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:48,197 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:48,531 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:48,796 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:49,132 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:49,429 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:49,430 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/USDT/BUY
2025-12-03 17:57:49,431 - worker.extractor - INFO - Extracted 26 offers for VES/USDT/BUY
2025-12-03 17:57:49,431 - worker.extractor - INFO - Extracting USD/ETH/BUY
2025-12-03 17:57:49,732 - worker.rate_limiter - WARNING - Rate limiter active: 140 waits, 215 total requests
2025-12-03 17:57:49,733 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:50,026 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:50,027 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/ETH/SELL
2025-12-03 17:57:50,027 - worker.extractor - INFO - Extracted 25 offers for COP/ETH/SELL
2025-12-03 17:57:50,028 - worker.extractor - INFO - Extracting USD/ETH/SELL
2025-12-03 17:57:50,332 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:50,618 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:50,933 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:51,210 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:51,535 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:51,813 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:52,135 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:52,414 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:52,736 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:53,018 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:53,336 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:53,631 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:53,955 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:54,555 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:54,655 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:54,656 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/USDT/BUY
2025-12-03 17:57:54,656 - worker.extractor - INFO - Extracted 26 offers for COP/USDT/BUY
2025-12-03 17:57:54,657 - worker.extractor - INFO - Extracting USD/BNB/BUY
2025-12-03 17:57:54,846 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:54,847 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/USDT/SELL
2025-12-03 17:57:54,847 - worker.extractor - INFO - Extracted 26 offers for COP/USDT/SELL
2025-12-03 17:57:54,848 - worker.extractor - INFO - Extracting USD/BNB/SELL
2025-12-03 17:57:55,156 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:55,436 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:55,438 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/USDT/SELL
2025-12-03 17:57:55,439 - worker.extractor - INFO - Extracted 26 offers for VES/USDT/SELL
2025-12-03 17:57:55,440 - worker.extractor - INFO - Extracting USD/USDC/BUY
2025-12-03 17:57:55,757 - worker.rate_limiter - WARNING - Rate limiter active: 150 waits, 225 total requests
2025-12-03 17:57:55,759 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:56,028 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:56,029 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDT/BUY
2025-12-03 17:57:56,030 - worker.extractor - INFO - Extracted 26 offers for USD/USDT/BUY
2025-12-03 17:57:56,031 - worker.extractor - INFO - Extracting USD/USDC/SELL
2025-12-03 17:57:56,358 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:56,644 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:56,645 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/USDT/BUY
2025-12-03 17:57:56,646 - worker.extractor - INFO - Extracted 26 offers for ARS/USDT/BUY
2025-12-03 17:57:56,958 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:57,251 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:57,559 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:57,852 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:57,853 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/BTC/SELL
2025-12-03 17:57:57,853 - worker.extractor - INFO - Extracted 26 offers for COP/BTC/SELL
2025-12-03 17:57:58,160 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:58,461 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:58,493 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/USDT/SELL
2025-12-03 17:57:58,511 - worker.extractor - INFO - Extracted 26 offers for ARS/USDT/SELL
2025-12-03 17:57:58,761 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:59,039 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:59,362 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:57:59,630 - worker.extractor - INFO - Response status: 200
2025-12-03 17:57:59,962 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:00,259 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:00,261 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BTC/BUY
2025-12-03 17:58:00,261 - worker.extractor - INFO - Extracted 26 offers for ARS/BTC/BUY
2025-12-03 17:58:00,562 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:00,902 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:00,905 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/BTC/BUY
2025-12-03 17:58:00,907 - worker.extractor - INFO - Extracted 25 offers for VES/BTC/BUY
2025-12-03 17:58:01,163 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:01,438 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:01,763 - worker.rate_limiter - WARNING - Rate limiter active: 160 waits, 235 total requests
2025-12-03 17:58:01,764 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:02,042 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:02,364 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:02,639 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:02,965 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:03,236 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:03,237 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDT/SELL
2025-12-03 17:58:03,239 - worker.extractor - INFO - Extracted 26 offers for USD/USDT/SELL
2025-12-03 17:58:03,575 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:03,859 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:03,860 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BNB/BUY
2025-12-03 17:58:03,860 - worker.extractor - INFO - Extracted 21 offers for ARS/BNB/BUY
2025-12-03 17:58:04,175 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:04,463 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:04,464 - worker.extractor - WARNING - Reached max pages per pair (5) for VES/BTC/SELL
2025-12-03 17:58:04,465 - worker.extractor - INFO - Extracted 26 offers for VES/BTC/SELL
2025-12-03 17:58:04,775 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:05,051 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:05,053 - worker.extractor - WARNING - Reached max pages per pair (5) for COP/BTC/BUY
2025-12-03 17:58:05,053 - worker.extractor - INFO - Extracted 25 offers for COP/BTC/BUY
2025-12-03 17:58:05,376 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:05,643 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:05,644 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/ETH/SELL
2025-12-03 17:58:05,644 - worker.extractor - INFO - Extracted 25 offers for ARS/ETH/SELL
2025-12-03 17:58:05,978 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:06,252 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:06,578 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:06,841 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:07,180 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:07,494 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:07,780 - worker.rate_limiter - WARNING - Rate limiter active: 170 waits, 245 total requests
2025-12-03 17:58:07,782 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:08,071 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:08,381 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:08,653 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:08,994 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:09,296 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:09,297 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/ETH/BUY
2025-12-03 17:58:09,298 - worker.extractor - INFO - Extracted 22 offers for ARS/ETH/BUY
2025-12-03 17:58:09,595 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:09,866 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:09,871 - worker.extractor - WARNING - Reached max pages per pair (5) for ARS/BNB/SELL
2025-12-03 17:58:09,881 - worker.extractor - INFO - Extracted 25 offers for ARS/BNB/SELL
2025-12-03 17:58:10,198 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:10,475 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:10,799 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:11,064 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:11,399 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:11,677 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:12,000 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:12,282 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:12,614 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:12,883 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:13,214 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:13,492 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:13,815 - worker.rate_limiter - WARNING - Rate limiter active: 180 waits, 255 total requests
2025-12-03 17:58:13,815 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:14,091 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:14,415 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:14,691 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:15,015 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:15,287 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:15,616 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:15,903 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:16,217 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:16,490 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:16,818 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:17,120 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:17,418 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:17,676 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:18,019 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:18,295 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:18,643 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:18,957 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:19,243 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:19,505 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:19,844 - worker.rate_limiter - WARNING - Rate limiter active: 190 waits, 265 total requests
2025-12-03 17:58:19,844 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:20,109 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:20,444 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:20,736 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:21,045 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:21,313 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:21,315 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BTC/BUY
2025-12-03 17:58:21,315 - worker.extractor - INFO - Extracted 25 offers for USD/BTC/BUY
2025-12-03 17:58:21,645 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:21,911 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:22,246 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:22,575 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:22,846 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:23,117 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:23,447 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:23,723 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:24,056 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:24,374 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:24,376 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BTC/SELL
2025-12-03 17:58:24,379 - worker.extractor - INFO - Extracted 25 offers for USD/BTC/SELL
2025-12-03 17:58:24,656 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:24,955 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:24,956 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/ETH/BUY
2025-12-03 17:58:24,957 - worker.extractor - INFO - Extracted 25 offers for USD/ETH/BUY
2025-12-03 17:58:25,257 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:25,533 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:25,534 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/ETH/SELL
2025-12-03 17:58:25,535 - worker.extractor - INFO - Extracted 25 offers for USD/ETH/SELL
2025-12-03 17:58:25,858 - worker.rate_limiter - WARNING - Rate limiter active: 200 waits, 275 total requests
2025-12-03 17:58:25,858 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:26,115 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:26,115 - worker.extractor - INFO - No offers found for USD/BNB/BUY
2025-12-03 17:58:26,116 - worker.extractor - INFO - Extracted 20 offers for USD/BNB/BUY
2025-12-03 17:58:26,458 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:26,735 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:26,740 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/BNB/SELL
2025-12-03 17:58:26,741 - worker.extractor - INFO - Extracted 25 offers for USD/BNB/SELL
2025-12-03 17:58:27,059 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:27,345 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:27,346 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDC/BUY
2025-12-03 17:58:27,346 - worker.extractor - INFO - Extracted 25 offers for USD/USDC/BUY
2025-12-03 17:58:27,659 - worker.extractor - INFO - Binance API request to https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search
2025-12-03 17:58:27,930 - worker.extractor - INFO - Response status: 200
2025-12-03 17:58:27,931 - worker.extractor - WARNING - Reached max pages per pair (5) for USD/USDC/SELL
2025-12-03 17:58:27,932 - worker.extractor - INFO - Extracted 25 offers for USD/USDC/SELL
2025-12-03 17:58:27,944 - worker.extractor - INFO - Total offers extracted: 689
2025-12-03 17:58:27,945 - worker.loader - INFO - Starting to load 689 offers for batch 90a3fd84-908f-47de-8c22-7a1d12a2d22d...
2025-12-03 18:02:58,278 - worker.loader - INFO - Successfully loaded 689 offers for batch 90a3fd84-908f-47de-8c22-7a1d12a2d22d.
2025-12-03 18:02:58,658 - __main__ - INFO - P2P data extraction job finished successfully.