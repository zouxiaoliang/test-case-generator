# coding=utf8

import argparse
import os
from jinja2.nativetypes import NativeEnvironment, Template

__author__ = "zouxiaoliang"

TEST_CASE_H_FILE = """
#ifndef {{class_name.upper()}}_TEST_H
#define {{class_name.upper()}}_TEST_H

#include <cppunit/extensions/HelperMacros.h>

class {{class_name}}_TestCase : public CPPUNIT_NS::TestFixture
{
    CPPUNIT_TEST_SUITE( {{class_name}}_TestCase );
    CPPUNIT_TEST(helloworld_test);
    CPPUNIT_TEST_SUITE_END();

public:
    void setUp();
    void tearDown(); 

protected:
    void test_helloworld();
};

#endif // {{class_name.upper()}}_TEST_H

"""

TEST_CASE_CPP_FILE = """
#include <cppunit/config/SourcePrefix.h>

CPPUNIT_TEST_SUITE_REGISTRATION( {{class_name}}_TestCase );

void {{class_name}}_TestCase::setUp()
{

}

void {{class_name}}_TestCase::tearDown()
{

}

void {{class_name}}_TestCase::test_helloworld()
{

}

"""


def _main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--class-name", '-c', type=str, default="HelloWorld")
    parser.add_argument("--test-class-path", '-d', type=str, default=".")

    args = parser.parse_args()

    class_name = args.class_name                # type: str
    test_class_path = args.test_class_path      # type: str

    if not os.path.exists(test_class_path):
        print "test class path:{} not exists!!!".format(test_class_path)
        return -1

    env = NativeEnvironment()
    h_render = env.from_string(TEST_CASE_H_FILE)  # type: Template
    cpp_render = env.from_string(TEST_CASE_CPP_FILE)  # type: Template

    test_h_file = os.path.join(test_class_path, "{}.h".format(class_name))
    with open(test_h_file, mode="wb") as writer:
        writer.write(h_render.render(class_name=class_name).strip())
        writer.write("\n")
    pass

    test_cpp_file = os.path.join(test_class_path, "{}.cpp".format(class_name))
    with open(test_cpp_file, mode="wb") as writer:
        writer.write(cpp_render.render(class_name=class_name).strip())
        writer.write("\n")
    pass


if __name__ == "__main__":
    exit(_main())
