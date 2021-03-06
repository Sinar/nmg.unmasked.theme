# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import nmg.unmasked.theme


class NmgUnmaskedThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=nmg.unmasked.theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'nmg.unmasked.theme:default')


NMG_UNMASKED_THEME_FIXTURE = NmgUnmaskedThemeLayer()


NMG_UNMASKED_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(NMG_UNMASKED_THEME_FIXTURE,),
    name='NmgUnmaskedThemeLayer:IntegrationTesting',
)


NMG_UNMASKED_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(NMG_UNMASKED_THEME_FIXTURE,),
    name='NmgUnmaskedThemeLayer:FunctionalTesting',
)


NMG_UNMASKED_THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        NMG_UNMASKED_THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='NmgUnmaskedThemeLayer:AcceptanceTesting',
)
