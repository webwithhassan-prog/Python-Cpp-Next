import React from "react";

const TermsAndConditions = () => {
  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <div className="bg-white border-b sticky top-0 z-10">
        <div className="max-w-4xl mx-auto px-6 py-12">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">
            Terms & Conditions
          </h1>
          <p className="text-gray-600">Last Updated: May 24, 2026</p>
        </div>
      </div>

      <div className="max-w-4xl mx-auto px-6 py-10">
        <div className="prose prose-lg max-w-none text-gray-700 leading-relaxed">
          <p className="text-xl mb-10">
            Welcome to our platform. By accessing or using our services, you
            agree to be bound by these Terms and Conditions.
          </p>

          {/* Section 1 */}
          <section className="mb-12">
            <h2 className="text-2xl font-semibold text-gray-900 mb-4">
              1. Acceptance of Terms
            </h2>
            <p>
              By using this website and our services, you confirm that you have
              read, understood, and agree to be legally bound by these Terms and
              Conditions, along with our Privacy Policy.
            </p>
          </section>

          {/* Section 2 */}
          <section className="mb-12">
            <h2 className="text-2xl font-semibold text-gray-900 mb-4">
              2. User Accounts
            </h2>
            <p className="mb-4">
              You are responsible for maintaining the confidentiality of your
              account and password. You agree to accept responsibility for all
              activities that occur under your account.
            </p>
            <ul className="list-disc pl-6 space-y-2">
              <li>You must be at least 18 years old to use our services.</li>
              <li>
                You agree to provide accurate and complete information when
                registering.
              </li>
              <li>
                You must notify us immediately of any unauthorized use of your
                account.
              </li>
            </ul>
          </section>

          {/* Section 3 */}
          <section className="mb-12">
            <h2 className="text-2xl font-semibold text-gray-900 mb-4">
              3. User Conduct
            </h2>
            <p className="mb-4">You agree not to:</p>
            <ul className="list-disc pl-6 space-y-2">
              <li>Violate any applicable laws or regulations</li>
              <li>Infringe on any intellectual property rights</li>
              <li>Transmit any harmful code, viruses, or malware</li>
              <li>Engage in any fraudulent or misleading activity</li>
              <li>Harass, threaten, or abuse other users</li>
            </ul>
          </section>

          {/* Section 4 */}
          <section className="mb-12">
            <h2 className="text-2xl font-semibold text-gray-900 mb-4">
              4. Intellectual Property
            </h2>
            <p>
              All content, logos, and trademarks on this platform are the
              property of the company. You may not use, copy, or distribute any
              content without prior written permission.
            </p>
          </section>

          {/* Section 5 */}
          <section className="mb-12">
            <h2 className="text-2xl font-semibold text-gray-900 mb-4">
              5. Termination
            </h2>
            <p>
              We reserve the right to suspend or terminate your account at any
              time, with or without notice, for any reason, including breach of
              these terms.
            </p>
          </section>

          {/* Section 6 */}
          <section className="mb-12">
            <h2 className="text-2xl font-semibold text-gray-900 mb-4">
              6. Limitation of Liability
            </h2>
            <p>
              Our services are provided "as is". We shall not be liable for any
              indirect, incidental, or consequential damages arising from your
              use of the platform.
            </p>
          </section>

          <div className="mt-16 pt-8 border-t text-center text-sm text-gray-500">
            <p>
              If you have any questions about these Terms & Conditions, please
              contact us at{" "}
              <span className="text-blue-600 hover:underline">
                support@example.com
              </span>
              .
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default TermsAndConditions;
