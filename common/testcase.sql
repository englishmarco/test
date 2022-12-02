/*
 Navicat Premium Data Transfer

 Source Server         : test
 Source Server Type    : MySQL
 Source Server Version : 80013
 Source Host           : localhost:3306
 Source Schema         : testbase

 Target Server Type    : MySQL
 Target Server Version : 80013
 File Encoding         : 65001

 Date: 28/07/2020 18:40:38
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for testcase
-- ----------------------------
DROP TABLE IF EXISTS `testcase`;
CREATE TABLE `testcase`  (
  `case_id` int(255) NOT NULL,
  `case_num` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `method` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `body` json NULL,
  `headers` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `assert` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `status` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `token` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`case_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of testcase
-- ----------------------------
INSERT INTO `testcase` VALUES (1, 'test_HQXSXX_001', '获取学生信息', '/api/user/stu_info', 'get', '{"stu_name": "黑黑"}', NULL, 'error_cod=0', '200', '');
INSERT INTO `testcase` VALUES (2, 'test_DLXSZH_002', '登录学生账号001', '/api/user/login', 'post', '{"passwd": "aA123456", "username": "niuhanyang"}', NULL, 'error_cod=0', '200', NULL);
INSERT INTO `testcase` VALUES (3, 'test_DLXSZH_003', '登录学生账号002', '/api/user/login', 'post', '{"passwd": "123456", "username": "admin"}', NULL, 'error_cod=500', '200', NULL);

-- ----------------------------
-- Table structure for testcase_cjxm
-- ----------------------------
DROP TABLE IF EXISTS `testcase_cjxm`;
CREATE TABLE `testcase_cjxm`  (
  `case_id` int(255) NOT NULL,
  `case_num` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `method` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `body` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `headers` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `assert` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `status` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `token` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`case_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of testcase_cjxm
-- ----------------------------
INSERT INTO `testcase_cjxm` VALUES (1, 'test_CJXM_001', '注册接口', '/api/user/user_reg', 'POST', '{\'username\':\'abctest\',\'pwd\':\'Aa123456\',\'cpwd\':\'Aa123456\'}', NULL, '{\'error_code\':0},{\'error_code\':3005}', '200', NULL);
INSERT INTO `testcase_cjxm` VALUES (2, 'test_CJXM_002', '登录', '/api/user/login', 'POST', '{ \'username\': \'mytest\',\'passwd\': \'Abc123\'}', NULL, '{\'error_code\':0}', '200', NULL);
INSERT INTO `testcase_cjxm` VALUES (3, 'test_CJXM_003', '添加奖品(需上传文件)', '/api/product/add', 'POST', '{\'name\': \'奖品名字2020\', \'sign\': \'b44109efbfe1007c1ad93a757d78e459\', \'userid\': \'78926\'}', NULL, '{\'msg\':\'必须是管理员才可以添加奖品\'}', '200', NULL);
INSERT INTO `testcase_cjxm` VALUES (4, 'test_CJXM_004', '抽奖接口', '/api/product/choice', 'GET', '{\'sign\': \'b44109efbfe1007c1ad93a757d78e459\', \'userid\': \'78926\'}', NULL, '{\'error_code\':0},{\'error_code\':1099}', '200', NULL);
INSERT INTO `testcase_cjxm` VALUES (5, 'test_CJXM_005', '查看中奖记录', '/api/user/win_record', 'GET', '{\'sign\': \'b44109efbfe1007c1ad93a757d78e459\', \'userid\': \'78926\'}', NULL, '{\'error_code\':0}', '200', NULL);
INSERT INTO `testcase_cjxm` VALUES (6, 'test_CJXM_006', '获取所有奖品信息', '/api/product/all', 'GET', NULL, NULL, '{\'error_code\':0}', '200', NULL);

-- ----------------------------
-- Table structure for testcase_ndxs
-- ----------------------------
DROP TABLE IF EXISTS `testcase_ndxs`;
CREATE TABLE `testcase_ndxs`  (
  `case_id` int(255) NOT NULL,
  `case_num` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `method` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `body` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `headers` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `assert` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `status` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `token` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`case_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of testcase_ndxs
-- ----------------------------
INSERT INTO `testcase_ndxs` VALUES (1, 'test_NDXS_001', '获取学生信息', '/api/user/stu_info', 'GET', '{\'stu_name\':\'小草\'}', NULL, '{\'error_code\':0}', NULL, NULL);
INSERT INTO `testcase_ndxs` VALUES (2, 'test_NDXS_002', '登录', '/api/user/login', 'POST', '{\'username\':\'mytest\',\'passwd\':\'Abc123\'}', NULL, '{\'error_code\':0}', NULL, NULL);
INSERT INTO `testcase_ndxs` VALUES (3, 'test_NDXS_003', '添加学生信息', '/api/user/add_stu', 'POST', '{\'name\': \'mytest\', \'grade\': \'计算机2020班\', \'phone\': \'13512341234\'}', NULL, '{\'msg\':\'手机号已经存在\'}', NULL, '');
INSERT INTO `testcase_ndxs` VALUES (4, 'test_NDXS_004', '学生金币充值', '/api/user/gold_add', 'POST', '{\'stu_id\':\'100002630\',\'gold\': 1}', NULL, '{\'msg\':\'请登陆\'}', NULL, 'b44109efbfe1007c1ad93a757d78e459');
INSERT INTO `testcase_ndxs` VALUES (5, 'test_NDXS_005', '获取所有学生信息', '/api/user/all_stu', 'GET', NULL, '{\'Referer\':\'http://api.nnzhp.cn/\'}', NULL, NULL, NULL);
INSERT INTO `testcase_ndxs` VALUES (6, 'test_NDXS_006', '文件上传', '/api/file/file_upload', 'POST', NULL, NULL, '{\'msg\':\'操作成功\'}', NULL, NULL);

SET FOREIGN_KEY_CHECKS = 1;
