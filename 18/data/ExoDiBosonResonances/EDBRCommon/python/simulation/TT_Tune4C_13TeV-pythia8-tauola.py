import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#       '/store/mc/Spring14miniaod/RSGravToZZ_kMpl01_M-1000_Tune4C_13TeV-pythia8/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/00CEB50F-9D07-E411-9DBB-002590182FD8.root',
#       '/store/mc/Spring14miniaod/RSGravToZZ_kMpl01_M-1000_Tune4C_13TeV-pythia8/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/70529AC9-3707-E411-98D0-0025902CF9E2.root',
#       '/store/mc/Spring14miniaod/RSGravToZZ_kMpl01_M-1000_Tune4C_13TeV-pythia8/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/7CEB3A30-3607-E411-964D-003048C7109E.root',
#       '/store/mc/Spring14miniaod/RSGravToZZ_kMpl01_M-1000_Tune4C_13TeV-pythia8/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/FCB22594-3B07-E411-8C3D-0025902D959A.root' ] );
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/063013AD-9907-E411-8135-0026189438BD.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/08C034C3-9807-E411-BD14-002618943986.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/0A05AAC0-9807-E411-992E-002618943821.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/0E64727A-9A07-E411-9945-002618943807.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/0E6E23B1-9907-E411-8492-002618943915.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/1018DED5-9A07-E411-820C-002618943904.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/16708C3C-9B07-E411-9F23-003048FF9AC6.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/1824AFAB-9907-E411-B67C-0026189438A9.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/18D6BAC1-9807-E411-B3CF-002618943821.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/1C806FE0-9907-E411-8F80-002618943915.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/26F30DAC-9907-E411-925E-002618943915.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/2A7AA6C0-9807-E411-8FE9-002618943821.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/326A536F-9A07-E411-B2C8-00304867904A.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/38FFD75E-9A07-E411-BF7B-002618943865.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/3CC20AAC-9907-E411-8C47-0026189437F8.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/40521C43-9907-E411-BE41-00261894384F.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/40BC61C1-9807-E411-8AB0-00261894385A.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/4209F474-9A07-E411-B2ED-00261894393D.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/423F9386-9A07-E411-B180-002618FDA265.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/4CB407AD-9907-E411-9378-0026189438F5.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/5C1834C2-9807-E411-99FC-002618943972.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/5C7C00BF-9807-E411-B7EE-00261894389F.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/60F265AC-9907-E411-8355-002618943809.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/66968A92-9907-E411-A2FE-002618943896.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/66DD43C0-9807-E411-AF29-002618943896.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/66E15FC3-9807-E411-BAA5-002618943858.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/689AE3E8-9807-E411-A04D-0025905A48D6.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/704B12C3-9A07-E411-AC5C-0025905A48D6.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/70CA28DE-9907-E411-9472-002618943875.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/7494FB6E-9A07-E411-A4F1-00261894384F.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/801CF6C3-9807-E411-8668-002618943858.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/82ECA89D-9907-E411-BA57-002618943900.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/849448AE-9907-E411-ACBA-002618943933.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/86EC19CD-9A07-E411-B3F2-002618943809.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/907750AD-9907-E411-9077-002618943869.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/9628A6AA-9907-E411-9B11-002618943865.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/9A3543AC-9907-E411-974B-002618943939.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/9E216EC2-9A07-E411-9090-002618943896.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/A822330D-9907-E411-9684-0025905964B2.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/AA4023DD-9A07-E411-BDEC-0025905938AA.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/B47A71AB-9907-E411-9469-0026189438FE.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/B4B9AEF1-9A07-E411-B685-0025905A6068.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/B4E323AE-9907-E411-B3B6-0026189438B1.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/B8FBB374-9A07-E411-B41B-0025905964B4.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/BADFBAAB-9907-E411-9DD6-002618943915.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/C2F464F7-9A07-E411-B309-0025905A609E.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/C6D45707-9B07-E411-89A5-0025905938D4.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/CEBE30D3-9A07-E411-96A8-0026189438BD.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/D03585D3-9A07-E411-BE5D-0026189437F8.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/D04F6233-9907-E411-BD81-002618943807.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/D48D2AD7-9A07-E411-A55B-002618943896.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/D60D35C0-9807-E411-9B82-00261894389E.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/DA0D5DAC-9907-E411-8213-0026189438D7.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/DA2A80BB-9A07-E411-94CF-002618943900.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/DA3D2056-9807-E411-B75A-002618943896.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/E0741F82-9907-E411-A442-0025905A60CE.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/E07A5325-9907-E411-ADF0-0025905964C4.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/E40545C3-9807-E411-B4B6-00261894393A.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/E817B4C0-9807-E411-A8FD-002618943821.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/E89EF7D5-9A07-E411-B19F-002618943933.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/EE3CB9C2-9807-E411-85B7-002618943875.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/EE5AD1C3-9807-E411-A2E8-002618943915.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/F64F99C2-9807-E411-B21D-002618943972.root',
       '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/FAEEA4D0-9A07-E411-B36A-002618943869.root'] );




secFiles.extend( [
               ] )
